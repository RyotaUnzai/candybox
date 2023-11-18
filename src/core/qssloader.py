import os
import re
from pathlib import Path, WindowsPath

import core


class HasMeta(type):
    def __new__(cls, name, bases, dict):
        dict["file"] = ""
        dict["style"] = ""
        dict["pattern"] = {"colon": r"(:[ ]+|:|[ ]+:)"}
        dict["patternPseudoRoot"] = {
            "main": r":root([ {]+)((\s+)(--)[a-zA-Z0-9:-]+[ ;0-9a-zA-Z#:]+)+[\s]+}",
            "key": r"--[a-zA-Z0-9- ]+",
            "value": r":[ #a-zA-Z0-9]+;",
            "var": r"(:|[ ]+:)",
            "sentance": r"(| +)--[a-zA-z0-9-: ]+([0-9a-zA-Z#:]+)",
        }
        dict["atRules"] = {
            "import": r"@import[a-zA-Z0-9\(\".-_<> ]+\);",
            "importFixStart": r'@import url("',
            "importFixEnd": r'");',
        }
        return super(HasMeta, cls).__new__(cls, name, bases, dict)


class QssLoader(object, metaclass=HasMeta):
    __styleSheet = ""
    __filePath = ""
    __fileDir = ""

    @property
    def fileDir(self):
        return self.__fileDir

    @property
    def filePath(self):
        return self.__filePath

    @filePath.setter
    def filePath(self, value):
        self.__filePath = value
        self.__fileDir = os.path.dirname(value)

    def searchFiles(self):
        if os.path.exists(self.rootPath):
            for file in os.listdir(self.rootPath):
                fullpath = os.path.join(self.rootPath, file)

                if os.path.isdir(fullpath):
                    self.searchFile(self.files)

                if file.split(".")[-1] == "qss":
                    self.files.append(fullpath)
        return self.files

    @property
    def styleSheet(self):
        return self.__styleSheet

    @styleSheet.getter
    def styleSheet(self):
        self.__styleSheet = core.readFile(self.filePath)

        self.atImport()
        self.PseudoRoot()
        return self.__styleSheet

    def atImport(self):
        pattern = re.compile(self.atRules["import"], re.MULTILINE | re.DOTALL)

        importContents = []
        for match in pattern.finditer(self.__styleSheet):
            importContents.append(match.group(0))

        for importContent in importContents:
            importPath: WindowsPath = importContent.replace(self.atRules["importFixStart"], "")
            importPath = importPath.replace(self.atRules["importFixEnd"], "")
            if not os.path.exists(importPath):
                importPath = Path(self.fileDir) / importPath
                if not importPath.exists():
                    continue

            qss = core.readFile(importPath.as_posix())
            self.__styleSheet = self.__styleSheet.replace(importContent, qss)

    def PseudoRoot(self):
        pattern = re.compile(self.patternPseudoRoot["main"], re.MULTILINE | re.DOTALL)

        rootVarContents = []
        for match in pattern.finditer(self.__styleSheet):
            rootVarContents.append(match.group(0))

        pattern = re.compile(self.patternPseudoRoot["sentance"], re.MULTILINE | re.DOTALL)
        rootVars = []
        for rootVarContent in rootVarContents:
            for match in pattern.finditer(rootVarContent):
                rootVars.append(match.group(0))

        for rootVar in rootVars:
            key, value = rootVar.split(":")
            key = key.replace(" ", "")
            value = value.replace(" ", "").replace(";", "")
            atRules = r"var\(([ ]+|)" + key + r"([ ]+|)\)"
            pattern = re.compile(atRules, re.MULTILINE | re.DOTALL)
            for match in pattern.finditer(self.__styleSheet):
                self.__styleSheet = self.__styleSheet.replace(match.group(0), value)

        for rootVarContent in rootVarContents:
            self.__styleSheet = self.__styleSheet.replace(rootVarContent, "")
