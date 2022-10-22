from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


def maskImage(
    imgPath=None, imgData=None, imgType="png", size=200,
    noPen=False, penSize=12, penColor="#ffc408", penStyle="inside"
):
    if imgPath is not None:
        imgData = open(imgPath, "rb").read()

    image = QImage.fromData(imgData, imgType)
    image.convertToFormat(QImage.Format_ARGB32)

    imgsize = min(image.width(), image.height())
    rect = QRect(
        (image.width() - imgsize) / 2.0,
        (image.height() - imgsize) / 2.0,
        imgsize,
        imgsize,
    )
    image = image.copy(rect)

    out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
    out_img.fill(Qt.transparent)

    brush = QBrush(image)
    painter = QPainter(out_img)
    painter.setBrush(brush)
    painter.setPen(Qt.NoPen)
    painter.setRenderHint(QPainter.Antialiasing, True)
    penSizeHalf = penSize / 2.0
    painter.drawEllipse(
        0, 0,
        imgsize, imgsize
    )
    painter.end()

    pr = QWindow().devicePixelRatio()
    Pixmap = QPixmap.fromImage(out_img)
    Pixmap.setDevicePixelRatio(pr)
    size *= pr
    Pixmap = Pixmap.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    if noPen is False:
        extendSize = size + (penSize * 2.0)
        if penStyle == "center":
            out_img = QImage(extendSize, extendSize, QImage.Format_ARGB32)

            out_img.fill(Qt.transparent)
            brush = QBrush(Pixmap)
            Paint = QPainter(out_img)
            Paint.setBrush(brush)
            Paint.setBrushOrigin(penSize, penSize)

            Paint.setPen(QPen(QColor(penColor), penSize, Qt.SolidLine))
            Paint.setRenderHint(QPainter.Antialiasing, True)
            Paint.drawEllipse(
                penSize, penSize,
                extendSize - penSize * 2, extendSize - penSize * 2
            )
            Paint.end()

            pr = QWindow().devicePixelRatio()
            NewPixmap = QPixmap.fromImage(out_img)
            NewPixmap.setDevicePixelRatio(pr)
            return NewPixmap
        elif penStyle == "outside":
            out_img = QImage(extendSize, extendSize, QImage.Format_ARGB32)
            out_img.fill(Qt.transparent)
            brush = QBrush(Pixmap)
            Paint = QPainter(out_img)
            Paint.setBrush(brush)
            Paint.setBrushOrigin(penSize, penSize)

            Paint.setPen(QPen(QColor(penColor), penSize, Qt.SolidLine))
            Paint.setRenderHint(QPainter.Antialiasing, True)
            Paint.drawEllipse(
                penSizeHalf + 1, penSizeHalf + 1,
                extendSize - penSize - 2, extendSize - penSize - 2
            )
            Paint.end()

            pr = QWindow().devicePixelRatio()
            NewPixmap = QPixmap.fromImage(out_img)
            NewPixmap.setDevicePixelRatio(pr)
            return NewPixmap
        else:
            Paint = QPainter(Pixmap)
            Paint.setPen(QPen(QColor(penColor), penSize, Qt.SolidLine))
            Paint.setRenderHint(QPainter.Antialiasing, True)
            Paint.drawEllipse(
                penSize / 2.0, penSize / 2.0,
                size - penSize, size - penSize
            )
            Paint.end()

    return Pixmap
