from PySide2 import QtWidgets
from typing import Final, TypeVar, Tuple

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
    pushButtons: Tuple[QtWidgets.QPushButton]
    _absWidth: int = 100

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setObjectName("Navigation")
        self.__initUI()

    def __initUI(self) -> None:
        "Initializes and configures the UI elements of the widget."
        self.setMaximumWidth(self._absWidth)
        self.setMinimumWidth(100)
        self.pushButtonAccount.clicked.connect(self._on_button_clicked)
        self.pushButtonHome.clicked.connect(self._on_button_clicked)
        self.pushButtonMessage.clicked.connect(self._on_button_clicked)
        self.pushButtonSchedule.clicked.connect(self._on_button_clicked)
        self.pushButtonPreference.clicked.connect(self._on_button_clicked)
        self.pushButtons = (
            self.pushButtonAccount,
            self.pushButtonHome,
            self.pushButtonMessage,
            self.pushButtonSchedule,
            self.pushButtonPreference
        )

    def _on_button_clicked(self) -> None:
        """Handles button click events for the navigation widget.

        When a navigation button is clicked, this method unchecks all buttons and then sets the clicked button as checked.
        This method ensures that only one button can be active (checked) at a time.
        """
        sender: QtWidgets.QPushButton = self.sender()
        if isinstance(sender, QtWidgets.QPushButton):
            [pushButton.setChecked(False) for pushButton in self.pushButtons]
            sender.setChecked(True)
