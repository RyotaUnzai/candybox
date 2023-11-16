
import os
import re
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import models.utils as utils
import core

class iconFileSystemModel(QFileSystemModel):
    def __init__(self, path=None, parent=None, *args, **kwargs):
        super(iconFileSystemModel, self).__init__(parent, *args, **kwargs)
        os.environ["QT_FILESYSTEMMODEL_WATCH_FILES"] = "1"
        if path:
            self.dir = path
            self.setRootPath(self.dir)
        self.setNameFilters(["*.json"])
        self.setNameFilterDisables(False)
        self.setReadOnly(True)


class iconListModel(QAbstractListModel):
    fileSystemWatcher = QFileSystemWatcher()

    def __init__(self, parent=None, data=[], *args, **kwargs):
        super(iconListModel, self).__init__(parent, *args, **kwargs)
        self.__items = data
        self.__inquiryItems = {}
        self.count = 0
        self.initItems()
        #self.setWatcher()
        #self.fileSystemWatcher.directoryChanged.connect(self.test)

    def test(self):
        print ("ok")

    def initItems(self, reload=False):

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

    def rowCount(self, parent=QModelIndex()):
        return len(self.__items)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if not 0 <= index.row() < self.rowCount():
            return None

        if role == Qt.DisplayRole:
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
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        # return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
