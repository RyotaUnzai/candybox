from PySide2 import QtCore, QtGui, QtWidgets


class BaseItem(object):
    def __init__(self, data=None, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return 1

    def data(self, column):
        if self.itemData is None:
            return ""
        return self.itemData['key']

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)
        return 0

    def clear(self):
        self.childItems = []


class SettingTreeItem(BaseItem):

    def __init__(self, data, parent=None):
        super(SettingTreeItem, self).__init__(data=data, parent=parent)


class SettingTreeModel(QtCore.QAbstractItemModel):
    def __init__(self, items=[], parent=None):
        super(SettingTreeModel, self).__init__(parent)

        self.__items = items
        self.rootItem = BaseItem()
        self.page = 0
        self.showItemCount = 20
        self.setItems(items)

    def setItems(self, items):

        self.__items = items
        self.setupModelData()

    def addItem(self, item):

        self.__items.append(item)
        self.setupModelData()

    def columnCount(self, parent):

        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role):

        if not index.isValid():
            return None
        if role != QtCore.Qt.DisplayRole:
            return None
        item = index.internalPointer()
        return item.data(index.column())

    def flags(self, index):

        if not index.isValid():
            return QtCore.Qt.NoItemFlags
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.rootItem.data(section)
        return None

    def index(self, row, column, parent):

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()
        childItem = index.internalPointer()
        parentItem = childItem.parent()
        if parentItem == self.rootItem:
            return QtCore.QModelIndex()
        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):

        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()
        return parentItem.childCount()

    def setupModelData(self):
        """
        表示用のItemを再構築する
        """
        self.rootItem.clear()
        parents = {}
        for item in self.__items:
            if item['parent'] in parents:
                p = parents[item['parent']]
            else:
                p = SettingTreeItem(item, self.rootItem)
                self.rootItem.appendChild(p)
                parents[item['parent']] = p
            settingTreeItem = SettingTreeItem(item, p)
            p.appendChild(settingTreeItem)
        self.layoutChanged.emit()
