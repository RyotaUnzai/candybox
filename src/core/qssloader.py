import sys
import os


class qssLoader(object):
    files = []
    __styleSheet = ""

    def __init__(self, rootPath="", *args, **kwargs):
        self.rootPath = rootPath
        self.searchFiles()

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
        self.__styleSheet = ""
        for file in sorted(self.files):

            with open(file, "r") as f:
                self.__styleSheet += f.read()
                self.__styleSheet += "\n"

        return self.__styleSheet

        # @styleSheet.setter
        # def styleSheet(self, value):
        #     self.__styleSheet = value
        #     self.__styleSheet = ""
        #     for file in self.files:

        #         with open(file, "r") as f:
        #             self.styleSheet += f.read()
