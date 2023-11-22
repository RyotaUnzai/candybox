from PySide2 import QtCore, QtGui, QtWidgets
from typing import TypeVar, Dict
from pathlib import WindowsPath

import core
from QtCustom import QRectModel, QStyleOptionButtonModel
from models import Vector2Model


class iconListDelegate(QtWidgets.QStyledItemDelegate):
    Self = TypeVar("Self", bound="iconListDelegate")
    _referenceButton: QtWidgets.QPushButton
    isDrawDisplayName: bool = True
    itemSize: int = 100
    space: int = 2
    frameRoundSize: int = 8
    frameSize: int = itemSize - (space * 2)
    textFrameSize: int = frameSize - (frameRoundSize * 2)
    imageSize: int = 60
    fontSize: int = 10
    imageDict: Dict[str, QStyleOptionButtonModel]
    state: QtWidgets.QStyle
    lastState: QtWidgets.QStyle = None
    baseRect: QtCore.QRect
    frameRect: QtCore.QRect
    textRect: QtCore.QRectF
    painter: QtGui.QPainter
    option: QtWidgets.QStyleOptionViewItem
    index: QtCore.QModelIndex
    state = QtWidgets.QStyle
    keyName: str
    styleOptionButton: QtWidgets.QStyleOptionButton

    def __init__(self: Self, parent=None, *args, **kwargs):
        super(iconListDelegate, self).__init__(parent, *args, **kwargs)
        self.imageDict = {}
        self._referenceButton = QtWidgets.QPushButton()

    @property
    def referenceButton(self: Self):
        return self._referenceButton

    @property
    def frameColor(self: Self) -> QtGui.QColor:
        return QtGui.QColor("#3c3c3c")

    @property
    def backgroundColor(self: Self) -> QtGui.QColor:
        if self.state & QtWidgets.QStyle.State_MouseOver:
            return QtGui.QColor(0, 184, 184, 10)
        return QtGui.QColor(0, 0, 0, 0)

    @property
    def isDrawDisplayName(self: Self) -> bool:
        if self.state & QtWidgets.QStyle.State_MouseOver:
            return True
        elif self.state & QtWidgets.QStyle.State_Selected:
            return True
        return False

    @property
    def frameLineColor(self: Self) -> QtGui.QColor:
        if self.state & QtWidgets.QStyle.State_MouseOver:
            return QtGui.QColor("#00b8b8")
        elif self.state & QtWidgets.QStyle.State_Selected:
            return QtGui.QColor("#00E7B8")
        return QtGui.QColor("#3c3c3c")

    @property
    def fontColor(self: Self) -> QtGui.QColor:
        if self.isDrawDisplayName:
            return QtGui.QColor("#000")
        return QtGui.QColor("#666")

    def paint(
        self: Self,
        painter: QtGui.QPainter,
        option: QtWidgets.QStyleOptionViewItem,
        index: QtCore.QModelIndex
    ) -> None:
        self.painter = painter
        self.option = option
        self.index = index
        self.state = self.option.state
        self.keyName = f"{index.row()}, {index.column()}"
        self.setStyle()
        self.createButton()
        self.drawText(
            rect=self.textRect,
            text=index.data(QtCore.Qt.DisplayRole),
            fontSize=self.fontSize,
            color=self.fontColor,
            align=QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft
        )

    def setStyle(self: Self) -> None:
        optionModel = QRectModel(rect=self.option.rect)
        self.basePosition = Vector2Model(array=(optionModel.x + self.space, optionModel.y + self.space))
        self.baseRect = QtCore.QRect(
            self.basePosition.x + (self.space / 2.0), self.basePosition.y + (self.space / 2.0),
            self.frameSize - self.space, self.frameSize - self.space
        )
        self.frameRect = QtCore.QRect(
            self.basePosition.x, self.basePosition.y,
            self.frameSize, self.frameSize
        )
        self.textRect = QtCore.QRectF(
            self.basePosition.x + self.frameRoundSize, self.basePosition.y + self.frameRoundSize,
            self.textFrameSize, self.textFrameSize
        )

    def createButton(self: Self) -> None:
        if self.keyName in self.imageDict:
            self.styleOptionButton = self.imageDict[self.keyName].button
            self.styleOptionButton.rect = self.baseRect
        else:
            ThumbnailImgPath: WindowsPath = self.index.data(core.ThumbnailImgPathRole)

            self.imageDict[self.keyName] = QStyleOptionButtonModel(
                **{
                    "button": QtWidgets.QStyleOptionButton(),
                    "pixmap": QtGui.QPixmap(ThumbnailImgPath.as_posix()),
                }
            )
            self.styleOptionButton: QtWidgets.QStyleOptionButton = self.imageDict[self.keyName].button
            self.styleOptionButton.state = QtWidgets.QStyle.State_Enabled
            self.styleOptionButton.icon = self.imageDict[self.keyName].pixmap
            self.styleOptionButton.iconSize = QtCore.QSize(self.frameSize, self.frameSize)
            self.styleOptionButton.color = self.styleOptionButton.palette.setColor(
                QtGui.QPalette.Button, QtGui.QColor(self.frameColor)
            )
        self.__setReferenceButtonStyleSheet()
        self.__setReferenceButton()

    def __setReferenceButton(self) -> None:
        self.referenceButton.style().drawControl(
            QtWidgets.QStyle.CE_PushButton,
            self.styleOptionButton,
            self.painter,
            self.referenceButton
        )

    def __setReferenceButtonStyleSheet(self) -> None:
        self.referenceButton.setStyleSheet(f"""
QPushButton{{
    border: 2px solid;
    border-radius: 5px;
    border-color: rgba{self.frameLineColor.getRgb()};
    background-color: rgba{self.backgroundColor.getRgb()};
}}

QPushButton:pressed{{
    background-color: rgba{self.backgroundColor.getRgb()};
}}
        """)

    def drawText(
        self: Self,
        rect: QtCore.QRect,
        text: str = "",
        fontSize: int = 16,
        color: QtGui.QColor = QtGui.QColor("#060606"),
        align: QtCore.Qt = QtCore.Qt.AlignCenter
    ) -> None:
        self.painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        font = QtGui.QFont()
        font.setPixelSize(fontSize)
        self.painter.setPen(QtGui.QPen(color))
        self.painter.setFont(font)
        self.painter.drawText(rect, align, text)

    def sizeHint(
        self,
        option: QtWidgets.QStyleOptionViewItem,
        index: QtCore.QModelIndex,
        *args, **kwargs
    ) -> QtCore.QSize:
        size: QtCore.QSize = super(iconListDelegate, self).sizeHint(option, index)
        size.setHeight(self.itemSize)
        size.setWidth(self.itemSize)
        return size
