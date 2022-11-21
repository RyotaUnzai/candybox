# PySide2
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class QProgressCircular(QWidget):
    __value = 73
    __enableText = True
    __fontFamily = "Segoe UI"
    __suffix = "%"
    __progressWidth = 10
    __enableBackground = True
    __isRounded = True
    __fontSize = 12
    __maxValue = 100
    __progressColor = "#0088FF"
    __fontColor = "#0088FF"
    __backgroundColor = "#44475a"
    __path = QPainterPath()
    __progressColorType = "flat"
    __progressBlurColor = QColor(0, 0, 0, 0)
    newPoint = Signal(QPoint)

    def __init__(self, parent=None):
        super(QProgressCircular, self).__init__(parent)
        self.setMinimumSize(100, 100)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Background, "#00000000")
        self.setPalette(palette)

    @property
    def progressBlurColor(self):
        return self.__progressBlurColor

    @progressBlurColor.setter
    def progressBlurColor(self, value):
        self.__progressBlurColor = value

    @property
    def progressColorType(self):
        return self.__progressColorType

    @progressColorType.setter
    def progressColorType(self, value):
        self.__progressColorType = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def enableText(self):
        return self.__enableText

    @enableText.setter
    def enableText(self, value):
        self.__enableText = value

    @property
    def fontFamily(self):
        return self.__fontFamily

    @fontFamily.setter
    def fontFamily(self, value):
        self.__fontFamily = value

    @property
    def suffix(self):
        return self.__suffix

    @suffix.setter
    def suffix(self, value):
        self.__suffix = value

    @property
    def progressWidth(self):
        return self.__progressWidth

    @progressWidth.setter
    def progressWidth(self, value):
        self.__progressWidth = value

    @property
    def enableBackground(self):
        return self.__enableBackground

    @enableBackground.setter
    def enableBackground(self, value):
        self.__enableBackground = value

    @property
    def isRounded(self):
        return self.__isRounded

    @isRounded.setter
    def isRounded(self, value):
        self.__isRounded = value

    @property
    def fontSize(self):
        return self.__fontSize

    @fontSize.setter
    def fontSize(self, value):
        self.__fontSize = value

    @property
    def maxValue(self):
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, value):
        self.__maxValue = value

    @property
    def progressColor(self):
        return self.__progressColor

    @progressColor.setter
    def progressColor(self, value):
        self.__progressColor = value

    @property
    def fontColor(self):
        return self.__fontColor

    @fontColor.setter
    def fontColor(self, value):
        self.__fontColor = value

    @property
    def backgroundColor(self):
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, value):
        self.__backgroundColor = value

    # SET VALUE
    def set_value(self, value):
        self.value = value
        self.repaint()  # Render progress bar after change value

    def mouseReleaseEvent(self, event):
        self.mousePosX = event.globalX()
        self.mousePosY = event.y()

    def moveEvent(self, event: QMoveEvent) -> None:
        return super(QProgressCircular, self).moveEvent(event)

    def mousePressEvent(self, event):
        self.mousePosX = event.globalX()
        self.__path.moveTo(event.pos())
        self.update()

    def mouseMoveEvent(self, event):
        self.addValue = int((event.globalX() - self.mousePosX) / 10)
        self.value = self.value + self.addValue
        if self.value < 0:
            self.value = 0
        elif self.value > 100:
            self.value = 100
        self.__path.lineTo(event.pos())
        self.update()

    def resizeEvent(self, event):
        self.update()

    def paintEvent(self, event):
        outLength = min(self.width(), self.height())
        inLength = outLength - self.progressWidth
        margin = self.progressWidth / 2
        value = self.value * 360 / self.maxValue
        painter = QPainter(self)

        # PAINTER
        self.__path = QPainterPath()
        # painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # CREATE RECTANGLE

        # PEN
        pen = QPen(QColor(self.__backgroundColor), self.progressWidth, Qt.SolidLine)

        # ENABLE BG
        if self.enableBackground:
            pen = QPen(QColor(self.__backgroundColor), self.progressWidth, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawArc(margin, margin, inLength, inLength, 0, 360 * 16)

        # CREATE TEXT
        if self.enableText:
            font = QFont(self.fontFamily, self.fontSize)
            font.setBold(True)
            painter.setFont(font)
            pen = QPen(QColor(self.fontColor), self.progressWidth, Qt.SolidLine)
            painter.setPen(pen)
            text = f"{self.value}"
            textLength = len(text)
            if textLength == 1:
                rect = QRect(0, 0, inLength + (self.fontSize * textLength), self.height() - self.fontSize / 3)
            elif textLength == 2:
                rect = QRect(0, 0, inLength + (self.fontSize * (textLength - 1)), self.height() - self.fontSize / 3)
            elif textLength == 3:
                rect = QRect(0, 0, inLength + (self.fontSize * (textLength - 2)), self.height() - self.fontSize / 3)
            painter.drawText(rect, Qt.AlignCenter, text)

        if self.progressColorType == "blur":
            progressColor = QRadialGradient(QPointF(outLength / 2, outLength / 2), outLength / 2)
            progressColor.setColorAt(1 - ((self.progressWidth / outLength) * 2), self.progressBlurColor)
            progressColor.setColorAt(1 - (self.progressWidth / outLength), self.progressColor)
            progressColor.setColorAt(1, self.progressBlurColor)
        elif self.progressColorType == "gradation":

            progressColor = QConicalGradient(QPointF(outLength / 2, outLength / 2), 310)
            # self.progressColor.setAlpha(255)
            progressColor.setColorAt(0, self.progressColor)
            # self.progressColor.setAlpha(0)
            progressColor.setColorAt(0.50, self.progressBlurColor)
            progressColor.setColorAt(0.90, self.progressBlurColor)
            progressColor.setColorAt(1, self.progressColor)
        else:
            progressColor = QColor(self.progressColor)

        pen = QPen(progressColor, self.progressWidth, Qt.SolidLine)
        # Set Round Cap
        if self.isRounded:
            pen.setCapStyle(Qt.RoundCap)

        painter.setPen(pen)
        painter.drawArc(margin, margin, inLength, inLength, -90 * 16, -value * 16)
        painter.end()

        # progressColor = QConicalGradient(QPointF(outLength / 2, outLength / 2), 270)

        # brush = QBrush(progressColor)
        # painter.setBrush(brush)
        # pen = QPen()
        # pen.setStyle(Qt.NoPen)
        # painter.setPen(pen)

        # painter.drawEllipse(0, 0, outLength, outLength)
