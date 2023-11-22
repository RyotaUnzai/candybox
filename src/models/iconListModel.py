from PySide2 import QtCore, QtWidgets

import core
from .iconModel import IconModel
from typing import Any, List, Union, TypeVar


class IconListModel(QtCore.QAbstractListModel):
    Self = TypeVar("Self", bound="IconListModel")
    __items:  List[IconModel]
    count: int = 0
    currentItem: IconModel

    def __init__(self: Self, parent: Any = None, items: List[IconModel] = [], *args, **kwargs):
        super(IconListModel, self).__init__(parent, *args, **kwargs)
        self.__items = items
        self.currentItem = self.__items[0]
        self.__initItems()

    def __initItems(self: Self, reload: bool = False) -> None:
        if self.count < self.rowCount():
            self.count += 1
        else:
            self.count = 0

    def setData(self: Self, value) -> None:
        self.__items = value
        self.__initItems(reload=True)

    def reload(self: Self, path) -> None:
        self.__initItems(reload=True)

    def rowCount(self: Self, parent: QtCore.QModelIndex = QtCore.QModelIndex()) -> int:
        return len(self.__items)

    def data(self: Self, index: QtCore.QModelIndex, role: int) -> Any:
        self.currentItem = self.__items[index.row()]
        if not index.isValid():
            return None
        if not 0 <= index.row() < self.rowCount():
            return None
        return self.__checkRole(role)

    def __checkRole(self: Self, role) -> Any:
        if role == QtCore.Qt.DisplayRole:
            return self.currentItem.displayName
        elif role == core.ThumbnailImgPathRole:
            return self.currentItem.imageUrl
        elif role == core.FilePathRole:
            return self.currentItem.filePath
        elif role == core.AssetVersionRole:
            return self.currentItem.assetVersion
        elif role == core.AuthorsRole:
            return self.currentItem.authors

        return None

    def flags(self: Self, index: QtCore.QModelIndex):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
