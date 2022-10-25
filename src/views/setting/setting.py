import os
import core
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import loadUiType, QUiLoader


class settingWidgetFilter(QObject):
    def eventFilter(self, widget, event):
        if event.type() == QEvent.Resize:
            Width = int(widget.size().width() / 30) * 10
            if Width <= 120:
                Width = 120
            elif Width >= 300:
                Width = 300
            widget.TreeView_Setting.setMinimumWidth(Width)
            widget.TreeView_Setting.setMaximumWidth(Width)


class settingWidget(QWidget):

    def __init__(self, parent=None, *args, **kwargs) -> None:

        super(settingWidget, self).__init__(parent, *args, **kwargs)
        uiLoader = QUiLoader()
        __uiFilePath = os.path.join(core.PATH_VIEWS, "setting", "setting.ui")
        ui = uiLoader.load(__uiFilePath)
        self.ui = ui
        self.ui.setParent(parent)
        self.setObjectName("Setting")
        self.__filter = settingWidgetFilter()
        self.ui.installEventFilter(self.__filter)
        self.ui.TableView_Setting.setMinimumWidth(240)
