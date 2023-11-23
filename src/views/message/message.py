from PySide2 import QtWidgets, QtCore
from typing import Final, TypeVar

import core
import QtCustom
from ..tooltip import ToolTipWidget

UI_FILE: Final = core.PATH_VIEWS / "message" / "message.ui"
_, baseClass = QtCustom.loadWindowUiType(UI_FILE)


class MessageWidget(_, baseClass):
    """A custom widget class for displaying messages, inheriting from a dynamically loaded UI base class.

    This widget is designed to provide a UI for displaying and interacting with messages.
    """

    Self = TypeVar("Self", bound="MessageWidget")
    checkBox: QtWidgets.QCheckBox
    labelHeading1: QtWidgets.QLabel
    listView: QtWidgets.QListView
    progressBar: QtWidgets.QProgressBar
    radioButton1: QtWidgets.QRadioButton
    radioButton2: QtWidgets.QRadioButton
    toolTip: ToolTipWidget

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.toolTip = ToolTipWidget(self)
        self.setupUi(self)
        self.setObjectName("Message")
        self.__initUI()

    def __initUI(self: Self) -> None:
        "Initializes and configures the UI elements of the widget."
        self.listView.setAutoFillBackground(True)
        self.listView.setFlow(QtWidgets.QListView.LeftToRight)
        self.listView.setViewMode(QtWidgets.QListView.IconMode)
        self.listView.setResizeMode(QtWidgets.QListView.Adjust)
        self.listView.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listView.setWrapping(True)
        self.listView.setMovement(QtWidgets.QListView.Static)
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listView.setSpacing(2)

        self.listView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listView.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, point):
        index = self.listView.indexAt(point)
        if not index.isValid():
            return

        self.toolTip.resize(300, 200)
        self.toolTip.labelAssetVersionValue.setText(str(index.data(core.AssetVersionRole)))
        self.toolTip.labelAuthorsValue.setText(str(index.data(core.AuthorsRole)))
        self.toolTip.labelDisplayNameValue.setText(str(index.data(QtCore.Qt.DisplayRole)))
        self.toolTip.labelFileUpdateTimeValue.setText(str(index.data(core.FileUpdateTimeRole)))
        self.toolTip.labelImageUrlValue.setText(str(index.data(core.ThumbnailImgPathRole)))
        self.toolTip.labelLastAuthorValue.setText(str(index.data(core.LastAuthorRole)))
        self.toolTip.labelFilePathValue.setText(str(index.data(core.FilePathRole)))

        point: QtCustom.QPointModel = QtCustom.QPointModel(point=self.listView.viewport().mapToGlobal(point))
        self.toolTip.move(point.x - 10, point.y - 20)
        self.toolTip.show()
