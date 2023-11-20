from PySide2 import QtWidgets
from typing import Final, TypeVar

import core
import QtCustom

UI_FILE: Final = core.PATH_VIEWS / "body" / "body.ui"
_, baseClass = QtCustom.loadWindowUiType(UI_FILE)


class BodyWidget(_, baseClass):
    Self = TypeVar("Self", bound="BodyWidget")

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super(BodyWidget, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setObjectName("Body")
