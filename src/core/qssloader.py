import re
import codecs
from typing import List, Union
from pathlib import Path, WindowsPath


class AtImportFix:
    """
    A class representing the start and end markers for @import URL format in QSS.

    Attributes:
    - start: The starting string of an @import URL in QSS.
    - end: The ending string of an @import URL in QSS.
    """

    start: str = r'@import url("'
    end: str = r'");'


class AtRulesModel:
    """
    A class representing different @rules in QSS, particularly for @import.

    Attributes:
    - atImport: A regex pattern to match the @import rule in QSS.
    - atImportFix: An instance of AtImportFix class to handle the start and end of @import URLs.
    """

    atImport: str = r"@import[a-zA-Z0-9\(\".-_<> ]+\);"
    atImportFix: AtImportFix = AtImportFix()


class PatternPseudoRootModel:
    """
    A class representing patterns for pseudo-root custom properties in QSS.

    Attributes:
    - main: A regex pattern to match the main structure of a :root rule.
    - key: A regex pattern to match the key part of a custom property.
    - value: A regex pattern to match the value part of a custom property.
    - var: A regex pattern to match the variable part of a custom property.
    - sentence: A regex pattern to match an entire custom property within the :root rule.
    """

    main: str = r":root([ {]+)((\s+)(--)[a-zA-Z0-9:-]+[ ;0-9a-zA-Z#:]+)+[\s]+}"
    key: str = r"--[a-zA-Z0-9- ]+"
    value: str = r":[ #a-zA-Z0-9]+;"
    var: str = r"(:|[ ]+:)"
    sentence: str = r"(| +)--[a-zA-z0-9-: ]+([0-9a-zA-Z#:]+)"


class PatternModel:
    """
    A class representing common patterns used in QSS.

    Attributes:
    - colon (str): A regex pattern to match a colon, which is used in QSS property declarations.
    """

    colon: str = r"(:[ ]+|:|[ ]+:)"


class QssLoader:
    """
    A loader class for processing QSS (Qt Stylesheet) files.

    This class is designed to handle the loading and processing of QSS files. It supports handling
    @import rules and pseudo-root custom properties. The class also provides functionality to search
    for QSS files in a specified directory.
    """

    __styleSheet: str
    "stylesheet content."
    __filePath: WindowsPath
    "The file path of the current QSS file being processed."
    __fileDir: WindowsPath
    "The directory of the current QSS file."
    file: Union[WindowsPath, str]
    "A path or string representing the file to be processed."
    files: List[WindowsPath] = []
    "A list of paths representing found QSS files."
    style: str = ""
    "A string representing additional styles to be applied."
    rootPath: WindowsPath
    "The root path to search for QSS files."
    pattern: PatternModel = PatternModel()
    "A pattern model for common QSS patterns."
    patternPseudoRoot: PatternPseudoRootModel = PatternPseudoRootModel()
    "A pattern model for pseudo-root custom properties in QSS."
    atRules: AtRulesModel = AtRulesModel()
    "A model representing different @rules in QSS."

    @staticmethod
    def readFile(path: Union[WindowsPath, str], decoding: str = "utf-8-sig") -> str:
        """
        Reads the content of a file.

        Parameters:
            path: Path to the file to be read.
            decoding: The character encoding for reading the file. Defaults to 'utf-8-sig'.

        Returns:
            The content of the file as a string.
        """
        try:
            with codecs.open(path, "r", encoding=decoding) as file:
                return file.read()
        except FileNotFoundError:
            raise IOError(f"File not found: {path}")
        except PermissionError:
            raise IOError(f"Permission denied when reading file: {path}")
        except UnicodeDecodeError:
            raise IOError(f"Unicode decoding error in file: {path}")

    @property
    def styleSheet(self) -> str:
        "stylesheet content."
        return self.__styleSheet

    @property
    def fileDir(self) -> WindowsPath:
        "The directory of the current QSS file."
        return self.__fileDir

    @property
    def filePath(self) -> WindowsPath:
        "The file path of the current QSS file being processed."
        return self.__filePath

    @filePath.setter
    def filePath(self, value: Union[WindowsPath, str]) -> None:
        self.__filePath = Path(value) if isinstance(value, str) else value
        self.__fileDir = self.__filePath.parent
        self.__processStyleSheet()

    def __processStyleSheet(self) -> None:
        """
        Processes the stylesheet by handling @import rules and pseudo-root variables.
        This method combines the tasks of reading the stylesheet, processing @import rules,
        and handling pseudo-root variables.

        Raises:
            IOError: If there is an error in reading the file or processing the stylesheet.
        """
        try:
            self.__styleSheet = self.readFile(self.__filePath)
            self.__atImport()
            self.__pseudoRoot()
        except IOError as e:
            raise IOError(f"Error processing stylesheet: {e}")

    def searchQSSFiles(self) -> List[WindowsPath]:
        """
        Searches for and lists all QSS (Qt Stylesheet) files in the specified root directory.

        This method iterates over the files in the `rootPath` directory of the class. It checks each file to determine
        if it has a `.qss` extension, indicating a Qt Stylesheet file. All such files are collected and returned in a list.

        Returns:
            List[WindowsPath]: A list of paths to the found QSS files. This list may be empty if no QSS files are found.
        """
        self.files.clear()
        if self.rootPath.exists():
            for file in self.rootPath.iterdir():
                filePath = Path(file)
                if filePath.suffix.lower() == ".qss":
                    self.files.append(filePath)

        return self.files

    def __atImport(self) -> None:
        """
        Processes @import rules in the stylesheet by importing the styles from external QSS files.
        """
        pattern = re.compile(self.atRules.atImport, re.MULTILINE | re.DOTALL)

        importContents = []
        for match in pattern.finditer(self.__styleSheet):
            importContents.append(match.group(0))

        for importContent in importContents:
            qssFileName: str = importContent.replace(self.atRules.atImportFix.start, "")
            qssFileName = qssFileName.replace(self.atRules.atImportFix.end, "")
            importPath: WindowsPath = Path(self.fileDir) / qssFileName
            if not importPath.exists():
                continue

            qss = self.readFile(importPath)
            self.__styleSheet = self.__styleSheet.replace(importContent, qss)

    def __setRootVarContents(self) -> List[str]:
        """
        Identifies and sets the root variable contents in the stylesheet.

        Returns:
            List[str]: A list of all the root variable content strings found in the stylesheet.
        """
        pattern = re.compile(self.patternPseudoRoot.main, re.MULTILINE | re.DOTALL)
        self.__rootVarContents = []
        for match in pattern.finditer(self.__styleSheet):
            self.__rootVarContents.append(match.group(0))
        return self.__rootVarContents

    def __setRootVars(self) -> List[str]:
        """
        Extracts and sets the root variables from the root variable contents.

        Returns:
            List[str]: A list of root variables extracted from the root variable contents.
        """
        pattern = re.compile(self.patternPseudoRoot.sentence, re.MULTILINE | re.DOTALL)
        self.__rootVars = []
        for rootVarContent in self.__rootVarContents:
            for match in pattern.finditer(rootVarContent):
                self.__rootVars.append(match.group(0))

    def __replaceVars(self):
        """
        Replaces the variables in the stylesheet with their corresponding values.
        This method operates on the root variables identified in the stylesheet.
        """
        for rootVar in self.__rootVars:
            key, value = rootVar.split(":")
            key = key.replace(" ", "")
            value = value.replace(" ", "").replace(";", "")
            atRules = r"var\(([ ]+|)" + key + r"([ ]+|)\)"
            pattern = re.compile(atRules, re.MULTILINE | re.DOTALL)
            for match in pattern.finditer(self.__styleSheet):
                self.__styleSheet = self.__styleSheet.replace(match.group(0), value)

    def __repalceRootVarContents(self):
        """
        Removes the root variable contents from the stylesheet.
        This method is called after replacing all the variables with their values.
        """
        for rootVarContent in self.__rootVarContents:
            self.__styleSheet = self.__styleSheet.replace(rootVarContent, "")

    def __pseudoRoot(self) -> None:
        """
        Processes pseudo-root custom properties in the stylesheet.
        This involves identifying root variable contents, extracting variables,
        replacing them with their values, and then removing the root variable contents.
        """
        self.__setRootVarContents()
        self.__setRootVars()
        self.__replaceVars()
        self.__repalceRootVarContents()
