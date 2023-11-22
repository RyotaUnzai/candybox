from PySide2 import QtWidgets, QtGui
from typing import Final, TypeVar, Tuple, Dict

import core
import QtCustom

UI_FILE: Final = core.PATH_VIEWS / "navigation" / "navigation.ui"
_, baseClass = QtCustom.loadWidgetUiType(UI_FILE)


class NavigationWidget(_, baseClass):
    """A custom widget class for navigation, inheriting from a dynamically loaded UI base class.

    This widget is designed to provide a UI for navigation purposes in an application.
    """
    Self = TypeVar("Self", bound="NavigationWidget")
    verticalLayoutTop: QtWidgets.QVBoxLayout
    verticalLayoutBottom: QtWidgets.QVBoxLayout
    verticalSpacerTop: QtWidgets.QSpacerItem
    verticalSpacerBottom: QtWidgets.QSpacerItem
    horizontalSpacer: QtWidgets.QSpacerItem
    labelAppIcon: QtWidgets.QLabel
    pushButtonAccount: QtWidgets.QPushButton
    pushButtonHome: QtWidgets.QPushButton
    pushButtonMessage: QtWidgets.QPushButton
    pushButtonSchedule: QtWidgets.QPushButton
    pushButtonPreference: QtWidgets.QPushButton
    pushButtons: Tuple[Tuple[int, QtWidgets.QPushButton]]
    _absWidth: int = 100

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setObjectName("Navigation")
        self.pushButtons = (
            (0, self.pushButtonAccount),
            (1, self.pushButtonHome),
            (2, self.pushButtonMessage),
            (3, self.pushButtonSchedule),
            (4, self.pushButtonPreference)
        )
        self.__initUI()

    def __initUI(self: Self) -> None:
        "Initializes and configures the UI elements of the widget."
        self.setMaximumWidth(self._absWidth)
        self.setMinimumWidth(100)

        [pushButton.clicked.connect(self._on_button_clicked) for num, pushButton in self.pushButtons]

    def _on_button_clicked(self: Self) -> None:
        """Handles button click events for the navigation widget.

        When a navigation button is clicked, this method unchecks all buttons
        and then sets the clicked button as checked.
        This method ensures that only one button can be active (checked) at a time.
        """
        sender: QtWidgets.QPushButton = self.sender()
        if isinstance(sender, QtWidgets.QPushButton):
            [pushButton.setChecked(False) for num, pushButton in self.pushButtons]
            sender.setChecked(True)

    def setFont(self: Self, font: QtGui.QFont) -> None:
        for num, pushButton in self.pushButtons:
            pushButton.setFont(font)

    def setText(self: Self, data: Dict[int, str]) -> None:
        for num, pushButton in self.pushButtons:
            pushButton.setText(data[num])

    def setIconText(self: Self, font: QtGui.QFont, iconText: str, iconSize: int) -> None:
        font.setPixelSize(iconSize)
        self.labelAppIcon.setFont(font)
        self.labelAppIcon.setText(iconText)
