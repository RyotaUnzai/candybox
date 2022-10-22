import os
import core
from PySide2.QtUiTools import loadUiType, QUiLoader
from PySide2.QtWidgets import QWidget


class navigationWidget(QWidget):
    PB_Home = None
    PB_Message = None
    PB_Schedul = None
    PB_Setting = None
    PB_Account = None
    L_Appicon = None
    VBL_Top = None
    VBL_Bottom = None

    def __init__(self, parent=None, *args, **kwargs) -> None:

        super(navigationWidget, self).__init__(parent, *args, **kwargs)
        uiLoader = QUiLoader()
        __uiFilePath = os.path.join(core.PATH_VIEWS, "navigation", "navigation.ui")
        ui = uiLoader.load(__uiFilePath)
        self.ui = ui
        self.ui.setParent(parent)
        self.ui.setMaximumWidth(86)
        self.ui.setMinimumWidth(86)
        self.setObjectName("Navigation")
