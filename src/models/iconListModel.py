
import os
import re

from PySide2 import QtCore, QtWidgets

import core
from core import utils

# from PySide2.QtCore import *
# from PySide2.QtWidgets import *


class IconFileSystemModel(QtWidgets.QFileSystemModel):
    def __init__(self, path=None, parent=None, *args, **kwargs):
        super(IconFileSystemModel, self).__init__(parent, *args, **kwargs)
        os.environ["QT_FILESYSTEMMODEL_WATCH_FILES"] = "1"
        if path:
            self.dir = path
            self.setRootPath(self.dir)
        self.setNameFilters(["*.json"])
        self.setNameFilterDisables(False)
        self.setReadOnly(True)


class IconListModel(QtCore.QAbstractListModel):
    fileSystemWatcher = QtCore.QFileSystemWatcher()

    def __init__(self, parent=None, data=[], *args, **kwargs):
        super(IconListModel, self).__init__(parent, *args, **kwargs)
        self.__items = data
        self.__inquiryItems = {}
        self.count = 0
        self.initItems()
        #self.setWatcher()
        #self.fileSystemWatcher.directoryChanged.connect(self.test)

    def initItems(self, reload: bool=False):
        if self.count < self.rowCount():
            self.count += 1
        else:
            self.count = 0
        for item in self.__items:
            if ":resource" in item["imageUrl"]:
                item["imageUrl"] = item["imageUrl"].replace(":resource", core.PATH_RESOURCE.as_posix()).replace("\\", "/")
            item["baseName"] = utils.getBasename(item["filePath"])
            item["displayName"] = item["baseName"].split(".")[0]


    def reload(self, path):
        self.initItems(reload=True)

    def rowCount(self, parent: QtCore.QModelIndex = QtCore.QModelIndex()):
        return len(self.__items)

    def data(self, index, role: QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        if not 0 <= index.row() < self.rowCount():
            return None

        if role == QtCore.Qt.DisplayRole:
            return self.__items[index.row()]["displayName"]
        elif role == core.ThumbnailImgPathRole:
            return self.__items[index.row()]["imageUrl"]
        elif role == core.FilePathRole:
            return self.__items[index.row()]["filePath"]
        elif role == core.AssetVersionRole:
            return self.__items[index.row()]["fileData"]["AssetVersion"]
        elif role == core.AuthorsRole:
            return self.__items[index.row()]["fileData"]["Authors"]
        else:
            return None

    def setData(self, value):
        self.__items = value
        self.initItems(reload=True)
        #     self.setWatcher()

        #     try:
        #         for path in self.fileSystemWatcher.directories():
        #             self.fileSystemWatcher.removePath(path)
        #     except:
        #         pass
        #     self.fileSystemWatcher.addPath(utils.getBasename(self.__items[0]["filePath"]))

        # def setWatcher(self):
        #     try:
        #         items = self.__items
        #         try:
        #             self.watcher.deleteLater()
        #         except Exception:
        #             pass
        #         self.watcher = QFileSystemWatcher(self)
        #         for item in items:
        #             self.watcher.addPath(item["filePath"])
        #             self.watcher.addPath(item["thumbnailImgPath"])
        #         self.watcher.fileChanged.connect(self.reload)
        #     except Exception:
        #         pass

    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        # return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable
