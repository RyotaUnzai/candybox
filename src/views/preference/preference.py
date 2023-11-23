from PySide2 import QtWidgets
from typing import Final, TypeVar

import core
import QtCustom

UI_FILE: Final = core.PATH_VIEWS / "preference" / "preference.ui"
_, baseClass = QtCustom.loadWindowUiType(UI_FILE)


class PreferenceWidget(_, baseClass):
    """A custom widget class for preference, inheriting from a dynamically loaded UI base class.

    This widget provides a user interface for application preference.
    """

    Self = TypeVar("Self", bound="PreferenceWidget")
    labelHeading1: QtWidgets.QLabel
    lineEdit: QtWidgets.QLineEdit
    tableView: QtWidgets.QTableView
    treeView: QtWidgets.QTreeView
    _minimumWidth: int = 240

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setObjectName("Preference")
        self.__initUI()

    def __initUI(self: Self) -> None:
        "Initializes and configures the UI elements of the widget."
        self.tableView.setMinimumWidth(self._minimumWidth)
        self.treeView.setMinimumWidth(self._minimumWidth)
