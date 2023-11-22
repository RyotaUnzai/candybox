
from PySide2 import QtCore, QtGui, QtWidgets

import core
import models

from pathlib import WindowsPath


class iconListDelegate(QtWidgets.QStyledItemDelegate):
    _referenceButton = None
    isDrawDisplayName = True
    itemSize = 100
    space = 2
    frameRoundSize = 8
    frameSize = itemSize - (space * 2)
    textFrameSize = frameSize - (frameRoundSize * 2)
    imageSize = 60
    fontSize = 10
    _frameColor = QtGui.QColor("#3c3c3c")
    _frameLineColor = QtGui.QColor("#3c3c3c")
    _backgroundColor = QtGui.QColor(0, 0, 0, 0)

    def __init__(self, parent=None, *args, **kwargs):
        super(iconListDelegate, self).__init__(parent, *args, **kwargs)
        self.imageDict = {}
        self._referenceButton = QtWidgets.QPushButton()

        self.count = 0
        self.__viewGeometry = QtCore.QRect()

    @property
    def frameColor(self):
        return self._frameColor

    @property
    def backgroundColor(self):
        return self._backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, value):
        if "mouseOver" == value:
            self._backgroundColor = QtGui.QColor(0, 184, 184, 10)
        elif "selected" == value:
            self._backgroundColor = QtGui.QColor(0, 0, 0, 0)
        else:
            self._backgroundColor = QtGui.QColor(0, 0, 0, 0)

    @property
    def frameLineColor(self):
        return self._frameLineColor

    @frameLineColor.setter
    def frameLineColor(self, value):
        if "mouseOver" == value:
            self._frameLineColor = QtGui.QColor("#00b8b8")
        elif "selected" == value:
            self._frameLineColor = QtGui.QColor("#00E7B8")
        else:
            self._frameLineColor = QtGui.QColor("#3c3c3c")

    def setStyle(self, option, index):
        basePosX = option.rect.x() + self.space
        basePosY = option.rect.y() + self.space

        self.viewGeometry = option
        self.isDrawDisplayName = True

        if option.state & QtWidgets.QStyle.State_MouseOver:
            self.frameLineColor = "mouseOver"
            self.backgroundColor = "mouseOver"
        elif option.state & QtWidgets.QStyle.State_Selected:
            self.frameLineColor = "selected"
            self.backgroundColor = "selected"
        else:
            self.isDrawDisplayName = False
            self.frameLineColor = None
            self.backgroundColor = None

        self.baseRect = QtCore.QRect(
            basePosX + (self.space / 2.0),
            basePosY + (self.space / 2.0),
            self.frameSize - self.space,
            self.frameSize - self.space
        )
        self.frameRect = QtCore.QRect(
            basePosX,
            basePosY,
            self.frameSize,
            self.frameSize
        )
        self.textRect = QtCore.QRectF(
            basePosX + self.frameRoundSize,
            basePosY + self.frameRoundSize,
            self.textFrameSize, self.textFrameSize
        )

    @ property
    def referenceButton(self):
        return self._referenceButton

    def selected(self, index):
        return "none"
        # return index.data(BQtUtil.FilePathRole)

    @ property
    def viewGeometry(self):
        return self.__viewGeometry

    @ viewGeometry.setter
    def viewGeometry(self, option):
        self.__viewGeometry = option.widget.geometry()

    def paint(self, painter, option, index):
        self.painter = painter
        # self.painter.save()
        self.setStyle(option, index)
        # create button
        keyName = "%s, %s" % (index.row(), index.column())
        self.createButton(index, keyName)
        if self.isDrawDisplayName:
            self.drawText(
                rect=self.textRect, text=index.data(QtCore.Qt.DisplayRole), fontSize=self.fontSize,
                align=QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft
            )
        else:
            self.drawText(
                rect=self.textRect, text=index.data(QtCore.Qt.DisplayRole), fontSize=self.fontSize,
                color=QtGui.QColor("#666666"), align=QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft
            )

    def createButton(self, index, keyName):
        if keyName not in self.imageDict:
            ThumbnailImgPath: WindowsPath = index.data(core.ThumbnailImgPathRole)
            self.imageDict[keyName] = {
                "btn": QtWidgets.QStyleOptionButton(),
                "image": QtGui.QPixmap(ThumbnailImgPath.as_posix()),
            }
            btn = self.imageDict[keyName]["btn"]
            btn.state = QtWidgets.QStyle.State_Enabled
            btn.icon = self.imageDict[keyName]["image"]
            btn.iconSize = QtCore.QSize(self.frameSize, self.frameSize)
            btn.color = btn.palette.setColor(QtGui.QPalette.Button, QtGui.QColor(self.frameColor))
        else:
            btn = self.imageDict[keyName]["btn"]
            btn.rect = self.baseRect
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

        self.referenceButton.style().drawControl(
            QtWidgets.QStyle.CE_PushButton, btn, self.painter, self.referenceButton
        )
        # Dont' need
        # QApplication.style().drawControl(QtWidgets.QStyle.CE_PushButton, btn, self.painter)

    def drawQStyleOptionButtonFrame(self, rect):
        self.painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        self.painter.setPen(QtGui.QPen(self.frameLineColor, 2, QtCore.Qt.SolidLine))
        self.painter.setBrush(QtCore.Qt.NoBrush)
        self.painter.drawRoundRect(
            rect, self.frameRoundSize, self.frameRoundSize
        )

    def drawThumbnailImg(self, rect, index, lineColor, image):
        self.painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        ThumbnailImgPath = index.data(core.ThumbnailImgPathRole)
        image = QtGui.QIcon(ThumbnailImgPath).pixmap(QtCore.QSize(self.frameSize, self.frameSize))
        self.painter.drawPixmap(rect, image)

    def drawFrame(self, rect, color, lineColor, space=0):
        self.painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        self.painter.setBrush(QtGui.QBrush(color))
        self.painter.setPen(QtGui.QPen(lineColor, 2, QtCore.Qt.SolidLine))
        self.painter.drawRoundRect(
            rect, self.frameRoundSize, self.frameRoundSize
        )

    def drawText(
        self, rect, text="", fontSize=16,
        color=QtGui.QColor("#060606"), align=QtCore.Qt.AlignCenter
    ):
        self.painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        font = QtGui.QFont()
        font.setPixelSize(fontSize)
        self.painter.setPen(QtGui.QPen(color))
        self.painter.setFont(font)
        self.painter.drawText(rect, align, text)

    def sizeHint(self, option, index, *args, **kwargs):
        size = super(iconListDelegate, self).sizeHint(option, index)
        size.setHeight(self.itemSize)
        size.setWidth(self.itemSize)
        return size
