from QtCustom import loadWindowUiType
import core
from PySide2 import QtWidgets
from typing import Final, TypeVar

UI_FILE: Final = core.PATH_VIEWS / "account" / "account.ui"
_, baseClass = loadWindowUiType(UI_FILE)



class AccountWidget(_, baseClass):
    Self = TypeVar("Self", bound="AccountWidget")
    checkBox: QtWidgets.QCheckBox
    labelHeading: QtWidgets.QLabel
    pushButton: QtWidgets.QPushButton
    verticalSpacer: QtWidgets.QSpacerItem

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super(AccountWidget, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setObjectName("Account")
        