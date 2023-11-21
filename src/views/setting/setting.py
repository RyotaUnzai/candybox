from PySide2 import QtWidgets
from typing import Final, TypeVar

import core
import QtCustom

UI_FILE: Final = core.PATH_VIEWS / "setting" / "setting.ui"
_, baseClass = QtCustom.loadWindowUiType(UI_FILE)


class SettingWidget(_, baseClass):
    """A custom widget class for settings, inheriting from a dynamically loaded UI base class.

    This widget provides a user interface for application settings.
    """
    Self = TypeVar("Self", bound="SettingWidget")
    labelHeading: QtWidgets.QLabel
    lineEdit: QtWidgets.QLineEdit
    tableView: QtWidgets.QTableView
    treeView: QtWidgets.QTreeView
    _minimumWidth: int = 240

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setObjectName("Setting")
        self.__initUI()

    def __initUI(self) -> None:
        "Initializes and configures the UI elements of the widget."
        self.tableView.setMinimumWidth(self._minimumWidth)
        self.treeView.setMinimumWidth(self._minimumWidth)
