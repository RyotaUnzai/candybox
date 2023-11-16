from PySide2 import QtCore, QtGui


def maskImage(
    imgPath=None, imgData=None, imgType="png", size=200,
    noPen=False, penSize=12, penColor="#ffc408", penStyle="inside"
):
    if imgPath is not None:
        imgData = open(imgPath, "rb").read()

    image = QtGui.QImage.fromData(imgData, imgType)
    image.convertToFormat(QtGui.QImage.Format_ARGB32)

    imgsize = min(image.width(), image.height())
    rect = QtCore.QRect(
        (image.width() - imgsize) / 2.0,
        (image.height() - imgsize) / 2.0,
        imgsize,
        imgsize,
    )
    image = image.copy(rect)

    out_img = QtGui.QImage(imgsize, imgsize, QtGui.QImage.Format_ARGB32)
    out_img.fill(QtCore.Qt.transparent)

    brush = QtGui.QBrush(image)
    painter = QtGui.QPainter(out_img)
    painter.setBrush(brush)
    painter.setPen(QtCore.Qt.NoPen)
    painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
    penSizeHalf = penSize / 2.0
    painter.drawEllipse(
        0, 0,
        imgsize, imgsize
    )
    painter.end()

    pr = QtGui.QWindow().devicePixelRatio()
    Pixmap = QtGui.QPixmap.fromImage(out_img)
    Pixmap.setDevicePixelRatio(pr)
    size *= pr
    Pixmap = Pixmap.scaled(size, size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
    if noPen is False:
        extendSize = size + (penSize * 2.0)
        if penStyle == "center":
            out_img = QtGui.QImage(extendSize, extendSize, QtGui.QImage.Format_ARGB32)

            out_img.fill(QtCore.Qt.transparent)
            brush = QtGui.QBrush(Pixmap)
            Paint = QtGui.QPainter(out_img)
            Paint.setBrush(brush)
            Paint.setBrushOrigin(penSize, penSize)

            Paint.setPen(QtGui.QPen(QtGui.QColor(penColor), penSize, QtCore.Qt.SolidLine))
            Paint.setRenderHint(QtGui.QPainter.Antialiasing, True)
            Paint.drawEllipse(
                penSize, penSize,
                extendSize - penSize * 2, extendSize - penSize * 2
            )
            Paint.end()

            pr = QtGui.QWindow().devicePixelRatio()
            NewPixmap = QtGui.QPixmap.fromImage(out_img)
            NewPixmap.setDevicePixelRatio(pr)
            return NewPixmap
        elif penStyle == "outside":
            out_img = QtGui.QImage(extendSize, extendSize, QtGui.QImage.Format_ARGB32)
            out_img.fill(QtCore.Qt.transparent)
            brush = QtGui.QBrush(Pixmap)
            Paint = QtGui.QPainter(out_img)
            Paint.setBrush(brush)
            Paint.setBrushOrigin(penSize, penSize)

            Paint.setPen(QtGui.QPen(QtGui.QColor(penColor), penSize, QtCore.Qt.SolidLine))
            Paint.setRenderHint(QtGui.QPainter.Antialiasing, True)
            Paint.drawEllipse(
                penSizeHalf + 1, penSizeHalf + 1,
                extendSize - penSize - 2, extendSize - penSize - 2
            )
            Paint.end()

            pr = QtGui.QWindow().devicePixelRatio()
            NewPixmap = QtGui.QPixmap.fromImage(out_img)
            NewPixmap.setDevicePixelRatio(pr)
            return NewPixmap
        else:
            Paint = QtGui.QPainter(Pixmap)
            Paint.setPen(QtGui.QPen(QtGui.QColor(penColor), penSize, QtCore.Qt.SolidLine))
            Paint.setRenderHint(QtGui.QPainter.Antialiasing, True)
            Paint.drawEllipse(
                penSize / 2.0, penSize / 2.0,
                size - penSize, size - penSize
            )
            Paint.end()

    return Pixmap
