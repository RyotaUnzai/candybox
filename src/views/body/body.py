from PySide2 import QtWidgets
from typing import Final, TypeVar

import core
import QtCustom

UI_FILE: Final = core.PATH_VIEWS / "body" / "body.ui"
_, baseClass = QtCustom.loadWindowUiType(UI_FILE)


class BodyWidget(_, baseClass):
    """A widget class for the body section of a graphical user interface.

    This class is derived from a base UI class, providing a specific interface 
    for the body section of an application. It is designed to be a flexible and 
    integral part of the application's user interface.
    """
    Self = TypeVar("Self", bound="BodyWidget")

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setObjectName("Body")
