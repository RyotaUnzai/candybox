from PySide2 import QtWidgets
from typing import Final, TypeVar

import QtCustom
import core

UI_FILE: Final = core.PATH_VIEWS / "tooltip" / "tooltip.ui"


class ToolTipWidget(QtCustom.QExToolTip):
    Self = TypeVar("Self", bound="ToolTipWidget")

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.ui = QtCustom.ExUiLoader(UI_FILE)
        self.setObjectName("ToolTip")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.ui)
        self.setLayout(self.layout)

    @property
    def formLayout(self: Self) -> QtWidgets.QFormLayout:
        return self.ui.formLayout

    @property
    def labelAssetVersion(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelAssetVersion

    @property
    def labelAssetVersionValue(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelAssetVersionValue

    @property
    def labelAuthors(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelAuthors

    @property
    def labelAuthorsValue(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelAuthorsValue

    @property
    def labelDisplayName(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelDisplayName

    @property
    def labelDisplayNameValue(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelDisplayNameValue

    @property
    def labelFileUpdateTime(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelFileUpdateTime

    @property
    def labelFileUpdateTimeValue(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelFileUpdateTimeValue

    @property
    def labelImageUrl(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelImageUrl

    @property
    def labelImageUrlValue(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelImageUrlValue

    @property
    def labelLastAuthor(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelLastAuthor

    @property
    def labelLastAuthorValue(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelLastAuthorValue

    @property
    def labelFilePath(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelFilePath

    @property
    def labelFilePathValue(self: Self) -> QtWidgets.QLabel:
        return self.ui.labelFilePathValue
