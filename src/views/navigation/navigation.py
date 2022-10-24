import os
import core
from PySide2.QtUiTools import loadUiType, QUiLoader
from PySide2.QtWidgets import QWidget, QButtonGroup


class navigationWidget(QWidget):
    PB_Home = None
    PB_Message = None
    PB_Schedule = None
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
        self.ui.setMaximumWidth(100)
        self.ui.setMinimumWidth(100)
        self.setObjectName("Navigation")

        self.ui.PB_Home.clicked.connect(self._on_button_clicked)
        self.ui.PB_Message.clicked.connect(self._on_button_clicked)
        self.ui.PB_Schedule.clicked.connect(self._on_button_clicked)
        self.ui.PB_Setting.clicked.connect(self._on_button_clicked)
        self.ui.PB_Account.clicked.connect(self._on_button_clicked)

    def _on_button_clicked(self):
        sender = self.sender()
        if sender != self.ui.PB_Home:
            self.ui.PB_Home.setChecked(False)
        else:
            self.ui.PB_Home.setChecked(True)
        if sender != self.ui.PB_Message:
            self.ui.PB_Message.setChecked(False)
        else:
            self.ui.PB_Message.setChecked(True)
        if sender != self.ui.PB_Schedule:
            self.ui.PB_Schedule.setChecked(False)
        else:
            self.ui.PB_Schedule.setChecked(True)
        if sender != self.ui.PB_Setting:
            self.ui.PB_Setting.setChecked(False)
        else:
            self.ui.PB_Setting.setChecked(True)
        if sender != self.ui.PB_Account:
            self.ui.PB_Account.setChecked(False)
        else:
            self.ui.PB_Account.setChecked(True)
