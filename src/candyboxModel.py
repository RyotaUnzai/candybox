from PySide2.QtWidgets import *

from models import *
from candyboxView import *


class candyBoxBodyItemModel(object):
    __widgetItems = {}

    def setBodyWidgetItems(self, layout: QBoxLayout) -> None:
        self.__widgetItems = {}
        for num in range(layout.count()):
            item = layout.itemAt(num)
            widget = item.widget()
            self.__widgetItems[widget.objectName()] = widget

    def showHideWidget(self, widgetType: str, layout: QBoxLayout) -> None:
        for num in range(layout.count()):
            item = layout.itemAt(num)
            widget = item.widget()
            objectName = widget.objectName()
            print(widgetType)
            if widgetType != objectName:
                widget.hide()
            else:
                widget.show()
                try:
                    widget.ui.show()
                except:
                    pass
    @property
    def widgetItems(self):
        return self.__widgetItems
