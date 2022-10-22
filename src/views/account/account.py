import os
import core
from PySide2.QtWidgets import QWidget
from PySide2.QtUiTools import loadUiType, QUiLoader

from QCustom import QAnimationComboBox


class accountWidget(QWidget):

    def __init__(self, parent=None, *args, **kwargs) -> None:

        super(accountWidget, self).__init__(parent, *args, **kwargs)
        uiLoader = QUiLoader()
        __uiFilePath = os.path.join(core.PATH_VIEWS, "account", "account.ui")
        ui = uiLoader.load(__uiFilePath)
        self.ui = ui
        self.ui.setParent(parent)
        self.setObjectName("Account")
        # QAnimationComboBox
