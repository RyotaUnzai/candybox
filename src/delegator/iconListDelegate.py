# -*- coding: utf-8 -*-
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtSvg import *
from PySide2.QtWidgets import *

import core
import models


class iconListDelegate(QStyledItemDelegate):
    isDrawDisplayName = True
    itemSize = 100
    space = 2
    frameRoundSize = 8
    frameSize = itemSize - (space * 2)
    textFrameSize = frameSize - (frameRoundSize * 2)
    imageSize = 60
    fontSize = 10

    def __init__(self, parent=None, *args, **kwargs):
        super(iconListDelegate, self).__init__(parent, *args, **kwargs)
        self.imageDict = {}

        self.count = 0
        self.__viewGeometry = QRect()

    def setStyle(self, option, index):
        basePosX = option.rect.x() + self.space
        basePosY = option.rect.y() + self.space

        self.viewGeometry = option
        self.isDrawDisplayName = True
        self.frameColor = QColor("#3c3c3c")

        if option.state & QStyle.State_MouseOver:
            self.frameLineColor = QColor("#0088FF")
        elif option.state & QStyle.State_Selected:
            self.frameLineColor = QColor("#1174CB")
        else:
            self.isDrawDisplayName = False
            self.frameLineColor = QColor("#3c3c3c")

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
            # set displayName
            self.drawText(
                rect=self.textRect, text=index.data(Qt.DisplayRole), fontSize=self.fontSize,
                align=Qt.AlignBottom | Qt.AlignLeft
            )
            self.drawText(
                rect=self.textRect, text=index.data(core.LastAuthorRole),
                fontSize=self.fontSize,
                align=Qt.AlignCenter | Qt.AlignLeft,
            )

            self.drawQStyleOptionButtonFrame(self.frameRect)

    def createImageDict(self, index, keyName):
        ThumbnailImgPath = index.data(core.ThumbnailImgPathRole)
        self.imageDict[keyName] = {
            "btn": QStyleOptionButton(),
            "image": QPixmap(ThumbnailImgPath)
        }

    def createButton(self, index, keyName):
        # if keyName not in self.imageDict:
        self.createImageDict(index, keyName)
        btn = self.imageDict[keyName]["btn"]
        btn.iconSize = QSize(self.frameSize, self.frameSize)
        btn.icon = self.imageDict[keyName]["image"]
        btn.rect = self.baseRect
        btn.state = QStyle.State_Enabled
        btn.color = btn.palette.setColor(QPalette.Button, QColor(self.frameColor))
        QApplication.style().drawControl(QStyle.CE_PushButton, btn, self.painter)

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
