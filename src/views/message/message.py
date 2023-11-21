from PySide2 import QtWidgets, QtCore
from typing import Final, TypeVar

import core
import QtCustom

UI_FILE: Final = core.PATH_VIEWS / "message" / "message.ui"
_, baseClass = QtCustom.loadWindowUiType(UI_FILE)


class MessageWidget(_, baseClass):
    """A custom widget class for displaying messages, inheriting from a dynamically loaded UI base class.

    This widget is designed to provide a UI for displaying and interacting with messages.
    """
    Self = TypeVar("Self", bound="MessageWidget")
    checkBox: QtWidgets.QCheckBox
    labelHeading: QtWidgets.QLabel
    listView: QtWidgets.QListView
    progressBar: QtWidgets.QProgressBar
    radioButton1: QtWidgets.QRadioButton
    radioButton2: QtWidgets.QRadioButton

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setObjectName("Message")
        self.__initUI()

    def __initUI(self) -> None:
        "Initializes and configures the UI elements of the widget."
        self.listView.setAutoFillBackground(True)
        self.listView.setFlow(QtWidgets.QListView.LeftToRight)
        self.listView.setViewMode(QtWidgets.QListView.IconMode)
        self.listView.setResizeMode(QtWidgets.QListView.Adjust)
        self.listView.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listView.setWrapping(True)
        self.listView.setMovement(QtWidgets.QListView.Static)
        self.listView.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection
        )
        self.listView.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.listView.setSpacing(2)
