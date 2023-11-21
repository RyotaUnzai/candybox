from PySide2 import QtWidgets

from models import (
    SettingTreeModel,
    IconModel,
    IconListModel
)


class CandyBoxBodyItemModel:
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
