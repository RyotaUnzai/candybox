from PySide2 import QtWidgets

from models import (
    SettingTreeModel,
    IconModel,
    IconListModel
)


class BodyItemModel:
    __widgetItems = {}

    def setBodyWidgetItems(self, layout: QtWidgets.QBoxLayout) -> None:
        self.__widgetItems = {}
        for num in range(layout.count()):
            item = layout.itemAt(num)
            widget = item.widget()
            self.__widgetItems[widget.objectName()] = widget

    def showHideWidget(self, widgetType: str, layout: QtWidgets.QBoxLayout) -> None:
        for num in range(layout.count()):
            item = layout.itemAt(num)
            widget = item.widget()
            objectName = widget.objectName()
            if widgetType != objectName:
                widget.hide()
            else:
                widget.show()

    @property
    def widgetItems(self) -> dict:
        return self.__widgetItems


class CandyBoxModels:
    bodyItemModel: BodyItemModel
    iconListModel: IconListModel
    settingTreeModel: SettingTreeModel

    def __init__(self) -> None:
        self.bodyItemModel = BodyItemModel()

    def setIconListModel(self, data) -> None:
        self.iconListModel = IconListModel(data)

    def setSettingTreeModel(self, data):
        self.settingTreeModel = SettingTreeModel(data)

    def createIconModel(self, **kwargs):
        return IconModel(**kwargs)
