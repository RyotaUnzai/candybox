from QtCustom import loadWindowUiType
import core
from PySide2 import QtWidgets
from typing import Final, TypeVar

UI_FILE: Final = core.PATH_VIEWS / "account" / "account.ui"
_, baseClass = loadWindowUiType(UI_FILE)


class AccountWidget(_, baseClass):
    """A widget class for user account management in a graphical user interface.

    This class is a customized widget derived from a base UI class, designed to provide an interface
    for account-related actions. It includes components like checkboxes, labels, and buttons.
    """

    Self = TypeVar("Self", bound="AccountWidget")
    checkBox: QtWidgets.QCheckBox
    labelHeading1: QtWidgets.QLabel
    pushButton: QtWidgets.QPushButton
    verticalSpacer: QtWidgets.QSpacerItem

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setObjectName("Account")
