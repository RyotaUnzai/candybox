from PySide2 import QtWidgets
from typing import Final, TypeVar

import QtCustom
import core

UI_FILE: Final = core.PATH_VIEWS / "home" / "home.ui"


class HomeWidget(QtWidgets.QWidget):
    Self = TypeVar("Self", bound="HomeWidget")

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super(HomeWidget, self).__init__(parent, *args, **kwargs)
        self.ui = QtCustom.ExUiLoader(UI_FILE)
        self.setObjectName("Home")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.ui)

    @property
    def animationComboBox(self) -> QtCustom.QAnimationComboBox:
        return self.ui.animationComboBox

    @property
    def labelHeading(self) -> QtWidgets.QLabel:
        return self.ui.labelHeading

    @property
    def listWidget(self) -> QtWidgets.QListWidget:
        return self.ui.listWidget

    @property
    def pushButtonQss1(self) -> QtWidgets.QPushButton:
        return self.ui.pushButtonQss1

    @property
    def pushButtonQss2(self) -> QtWidgets.QPushButton:
        return self.ui.pushButtonQss2

    @property
    def spinBox(self) -> QtWidgets.QSpinBox:
        return self.ui.spinBox

    @property
    def spinBoxQss(self) -> QtWidgets.QSpinBox:
        return self.ui.spinBoxQss
