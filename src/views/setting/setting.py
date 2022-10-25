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
    __TableView_Setting = None
    __TreeView_Setting = None

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

        self.TreeView_Setting = self.ui.TreeView_Setting
        self.TableView_Setting = self.ui.TableView_Setting
        self.TableView_Setting.setMinimumWidth(240)
        self.TableView_Setting.setMinimumWidth(240)

        # data = []
        # for i in range(5):
        #     data.append({'parent': 'hogehoge', 'key': 'homuhomu_' + str(i).zfill(3)})
        # for i in range(5):
        #     data.append({'parent': 'fugafuga', 'key': 'homuhomu_' + str(i).zfill(3)})

        # import models
        # self.model = models.settingTreeModel.SettingTreeModel()

    @property
    def TreeView_Setting(self) -> QTreeView:
        return self.__TreeView_Setting

    @TreeView_Setting.setter
    def TreeView_Setting(self, value):
        self.__TreeView_Setting = value

    @property
    def TableView_Setting(self) -> QTableView:
        return self.__TableView_Setting

    @TableView_Setting.setter
    def TableView_Setting(self, value):
        self.__TableView_Setting = value
