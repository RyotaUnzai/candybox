from PySide2 import QtWidgets
from typing import Final, TypeVar

import QtCustom
import core

UI_FILE: Final = core.PATH_VIEWS / "home" / "home.ui"


class HomeWidget(QtWidgets.QWidget):
    """A widget class for the home section of a graphical user interface.

    This class manages the home interface's layout and components, dynamically loading the UI from a file.
    It provides access to various UI elements through properties, enabling easy interaction with the home UI.
    """
    Self = TypeVar("Self", bound="HomeWidget")

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.ui = QtCustom.ExUiLoader(UI_FILE)
        self.ui.setParent(self)
        self.setObjectName("Home")
        self.__initUI()

    def __initUI(self: Self) -> None:
        "Initializes and configures the UI elements of the widget."
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.ui)
        self.setLayout(self.layout)

    @property
    def animationComboBox(self: Self) -> QtCustom.QAnimationComboBox:
        "Access animationComboBox component from the UI."
        return self.ui.animationComboBox

    @property
    def labelHeading(self: Self) -> QtWidgets.QLabel:
        "Access labelHeading component from the UI."
        return self.ui.labelHeading

    @property
    def listWidget(self: Self) -> QtWidgets.QListWidget:
        "Access listWidget component from the UI."
        return self.ui.listWidget

    @property
    def pushButtonQss1(self: Self) -> QtWidgets.QPushButton:
        "Access pushButtonQss1 component from the UI."
        return self.ui.pushButtonQss1

    @property
    def pushButtonQss2(self: Self) -> QtWidgets.QPushButton:
        "Access pushButtonQss2 component from the UI."
        return self.ui.pushButtonQss2

    @property
    def spinBox(self: Self) -> QtWidgets.QSpinBox:
        "Access spinBox component from the UI."
        return self.ui.spinBox

    @property
    def spinBoxQss(self: Self) -> QtWidgets.QSpinBox:
        "Access spinBoxQss component from the UI."
        return self.ui.spinBoxQss
