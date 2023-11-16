# -*- coding: utf-8 -*-
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtSvg import *
from PySide2.QtWidgets import *

import core
import models

from pathlib import WindowsPath

class iconListDelegate(QStyledItemDelegate):
    _referenceButton = None
    isDrawDisplayName = True
    itemSize = 100
    space = 2
    frameRoundSize = 8
    frameSize = itemSize - (space * 2)
    textFrameSize = frameSize - (frameRoundSize * 2)
    imageSize = 60
    fontSize = 10
    _frameColor = QColor("#3c3c3c")
    _frameLineColor = QColor("#3c3c3c")
    _backgroundColor = QColor(0, 0, 0, 0)

    def __init__(self, parent=None, *args, **kwargs):
        super(iconListDelegate, self).__init__(parent, *args, **kwargs)
        self.imageDict = {}
        self._referenceButton = QPushButton()

        self.count = 0
        self.__viewGeometry = QRect()

    @property
    def frameColor(self):
        return self._frameColor

    @property
    def backgroundColor(self):
        return self._backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, value):
        if "mouseOver" == value:
            self._backgroundColor = QColor(0, 184, 184, 10)
        elif "selected" == value:
            self._backgroundColor = QColor(0, 0, 0, 0)
        else:
            self._backgroundColor = QColor(0, 0, 0, 0)

    @property
    def frameLineColor(self):
        return self._frameLineColor

    @frameLineColor.setter
    def frameLineColor(self, value):
        if "mouseOver" == value:
            self._frameLineColor = QColor("#00b8b8")
        elif "selected" == value:
            self._frameLineColor = QColor("#00E7B8")
        else:
            self._frameLineColor = QColor("#3c3c3c")

    def setStyle(self, option, index):
        basePosX = option.rect.x() + self.space
        basePosY = option.rect.y() + self.space

        self.viewGeometry = option
        self.isDrawDisplayName = True

        if option.state & QStyle.State_MouseOver:
            self.frameLineColor = "mouseOver"
            self.backgroundColor = "mouseOver"
        elif option.state & QStyle.State_Selected:
            self.frameLineColor = "selected"
            self.backgroundColor = "selected"
        else:
            self.isDrawDisplayName = False
            self.frameLineColor = None
            self.backgroundColor = None

        self.baseRect = QRect(
            basePosX + (self.space / 2.0),
            basePosY + (self.space / 2.0),
            self.frameSize - self.space,
            self.frameSize - self.space
        )
        self.frameRect = QRect(
            basePosX,
            basePosY,
            self.frameSize,
            self.frameSize
        )
        self.textRect = QRectF(
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
                rect=self.textRect, text=index.data(Qt.DisplayRole), fontSize=self.fontSize,
                align=Qt.AlignBottom | Qt.AlignLeft
            )
        else:
            self.drawText(
                rect=self.textRect, text=index.data(Qt.DisplayRole), fontSize=self.fontSize,
                color=QColor("#666666"), align=Qt.AlignBottom | Qt.AlignLeft
            )

    def createButton(self, index, keyName):
        if keyName not in self.imageDict:
            ThumbnailImgPath: WindowsPath = index.data(core.ThumbnailImgPathRole)
            self.imageDict[keyName] = {
                "btn": QStyleOptionButton(),
                "image": QPixmap(ThumbnailImgPath.as_posix()),
            }
            btn = self.imageDict[keyName]["btn"]
            btn.state = QStyle.State_Enabled
            btn.icon = self.imageDict[keyName]["image"]
            btn.iconSize = QSize(self.frameSize, self.frameSize)
            btn.color = btn.palette.setColor(QPalette.Button, QColor(self.frameColor))
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
            QStyle.CE_PushButton, btn, self.painter, self.referenceButton
        )
        # Dont' need
        # QApplication.style().drawControl(QStyle.CE_PushButton, btn, self.painter)

    def drawQStyleOptionButtonFrame(self, rect):
        self.painter.setRenderHint(QPainter.Antialiasing, True)
        self.painter.setPen(QPen(self.frameLineColor, 2, Qt.SolidLine))
        self.painter.setBrush(Qt.NoBrush)
        self.painter.drawRoundRect(
            rect, self.frameRoundSize, self.frameRoundSize
        )

    def drawThumbnailImg(self, rect, index, lineColor, image):
        self.painter.setRenderHint(QPainter.Antialiasing, True)
        ThumbnailImgPath = index.data(core.ThumbnailImgPathRole)
        image = QIcon(ThumbnailImgPath).pixmap(QSize(self.frameSize, self.frameSize))
        self.painter.drawPixmap(rect, image)

    def drawFrame(self, rect, color, lineColor, space=0):
        self.painter.setRenderHint(QPainter.Antialiasing, True)
        self.painter.setBrush(QBrush(color))
        self.painter.setPen(QPen(lineColor, 2, Qt.SolidLine))
        self.painter.drawRoundRect(
            rect, self.frameRoundSize, self.frameRoundSize
        )

    def drawText(
        self, rect, text="", fontSize=16,
        color=QColor("#060606"), align=Qt.AlignCenter
    ):
        self.painter.setRenderHint(QPainter.Antialiasing, True)
        font = QFont()
        font.setPixelSize(fontSize)
        self.painter.setPen(QPen(color))
        self.painter.setFont(font)
        self.painter.drawText(rect, align, text)

    def sizeHint(self, option, index, *args, **kwargs):
        size = super(iconListDelegate, self).sizeHint(option, index)
        size.setHeight(self.itemSize)
        size.setWidth(self.itemSize)
        return size
