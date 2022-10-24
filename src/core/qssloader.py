import os
import re
import models


class hasMeta(type):
    def __new__(cls, name, bases, dict):
        dict["file"] = ""
        dict["style"] = ""
        dict["pattern"] = {
            "colon": r"(:[ ]+|:|[ ]+:)"
        }
        dict["patternPseudoRoot"] = {
            "main": r":root([ {]+)((\s+)(--)[a-zA-Z0-9:-]+[ ;0-9a-zA-Z#:]+)+[\s]+}",
            "key": r"--[a-zA-Z0-9- ]+",
            "value": r":[ #a-zA-Z0-9]+;",
            "var": r"(:|[ ]+:)",
            "sentance": r"(| +)--[a-zA-z0-9-: ]+([0-9a-zA-Z#:]+)"
        }
        dict["atRules"] = {
            "import": r"@import[a-zA-Z0-9\(\".-_<> ]+\);",
            "importFixStart": r'@import url("',
            "importFixEnd": r'");',
        }
        return super(hasMeta, cls).__new__(cls, name, bases, dict)


class qssLoader(object, metaclass=hasMeta):
    __styleSheet = ""
    __filePath = ""
    __fileDir = ""

    def __init__(self):
        pass

    @property
    def fileDir(self):
        return self.__fileDir

    @property
    def filePath(self):
        pass

    @filePath.setter
    def filePath(self, value):
        self.__filePath = value
        self.__fileDir = models.getDirname(value)

    @filePath.getter
    def filePath(self):
        return self.__filePath

    def searchFiles(self):
        if os.path.exists(self.rootPath):
            for file in os.listdir(self.rootPath):
                fullpath = os.path.join(self.rootPath, file)

                if os.path.isdir(fullpath):
                    self.searchFile(self.files)

                if file.split('.')[-1] == 'qss':
                    self.files.append(fullpath)
        return self.files

    @property
    def styleSheet(self):
        pass

    @styleSheet.getter
    def styleSheet(self):
        self.__styleSheet = models.readFile(self.filePath)

        self.atImport()
        self.PseudoRoot()
        return self.__styleSheet

    def atImport(self):
        pattern = re.compile(self.atRules["import"], re.MULTILINE | re.DOTALL)

        importContents = []
        for match in pattern.finditer(self.__styleSheet):
            importContents.append(match.group(0))

        for importContent in importContents:
            importPath = importContent.replace(self.atRules["importFixStart"], "")
            importPath = importPath.replace(self.atRules["importFixEnd"], "")
            if not os.path.exists(importPath):
                importPath = models.refreshPath(self.fileDir, importPath)
                if not os.path.exists(importPath):
                    continue

            qss = models.readFile(importPath)
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
