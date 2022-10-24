import os
import core
from PySide2.QtWidgets import QWidget
from PySide2.QtUiTools import loadUiType, QUiLoader


class settingWidget(QWidget):

    def __init__(self, parent=None, *args, **kwargs) -> None:

        super(settingWidget, self).__init__(parent, *args, **kwargs)
        uiLoader = QUiLoader()
        __uiFilePath = os.path.join(core.PATH_VIEWS, "setting", "setting.ui")
        ui = uiLoader.load(__uiFilePath)
        self.ui = ui
        self.ui.setParent(parent)
        self.setObjectName("Setting")
