# PySide2
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class QAbstractProgressCircular(QWidget):
    _value = 0
    _enableText = True
    _fontFamily = "Segoe UI"
    _suffix = "%"
    _progressWidth = 10
    _enableBackground = True
    _isRounded = True
    _fontSize = 12
    _minimum = 0
    _maximum = 100
    _progressColor = "#0088FF"
    _fontColor = "#0088FF"
    _backgroundColor = "#44475a"
    _path = QPainterPath()
    _progressColorType = "flat"
    _progressBlurColor = QColor(0, 0, 0, 0)
    valueChanged = Signal(int)

    def __init__(self, parent=None):
        super(QAbstractProgressCircular, self).__init__(parent)
        self.value = 0
        self.enableText = True
        self.fontFamily = "Segoe UI"
        self.suffix = "%"
        self.progressWidth = 10
        self.enableBackground = True
        self.isRounded = True
        self.fontSize = 12
        self.minimum = 0
        self.maximum = 100
        self.progressColor = "#0088FF"
        self.fontColor = "#0088FF"
        self.backgroundColor = "#44475a"
        self.path = QPainterPath()
        self.progressColorType = "flat"
        self.progressBlurColor = QColor(0, 0, 0, 0)
        self.setMinimumSize(100, 100)
        self.font = QFont(self.fontFamily, self.fontSize)
        self.font.setBold(True)

        self.valueChanged[int].connect(self._valueChangedCallback)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Background, "#00000000")
        self.setPalette(palette)

    def isRounded(self, value: bool):
        self._isRounded = value

    @property
    def rounded(self):
        return self._isRounded

    @rounded.setter
    def rounded(self, value):
        self._isRounded = value

    @Slot(int)
    def _valueChangedCallback(self, value):
        return value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def setValue(self, value):
        self.value = value
        self.valueChanged.emit(self.value)
        self.repaint()

    def setMinimum(self, value):
        self._minimum = value

    def setMaximum(self, value):
        self._maximum = value

    def setRange(self, minimum: int, maximum: int):
        self._minimum = minimum
        self._maximum = maximum

    @property
    def minimum(self):
        return self._minimum

    @minimum.setter
    def minimum(self, value):
        self._minimum = value

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, value):
        self._maximum = value

    @property
    def progressBlurColor(self):
        return self._progressBlurColor

    @progressBlurColor.setter
    def progressBlurColor(self, value):
        self._progressBlurColor = value

    @property
    def progressColorType(self):
        return self._progressColorType

    @progressColorType.setter
    def progressColorType(self, value):
        self._progressColorType = value

    @property
    def enableText(self):
        return self._enableText

    @enableText.setter
    def enableText(self, value):
        self._enableText = value

    @property
    def fontFamily(self):
        return self._fontFamily

    @fontFamily.setter
    def fontFamily(self, value):
        self._fontFamily = value

    @property
    def suffix(self):
        return self._suffix

    @suffix.setter
    def suffix(self, value):
        self._suffix = value

    @property
    def progressWidth(self):
        return self._progressWidth

    @progressWidth.setter
    def progressWidth(self, value):
        self._progressWidth = value

    @property
    def enableBackground(self):
        return self._enableBackground

    @enableBackground.setter
    def enableBackground(self, value):
        self._enableBackground = value

    @property
    def fontSize(self):
        return self._fontSize

    @fontSize.setter
    def fontSize(self, value):
        self._fontSize = value

    @property
    def progressColor(self):
        return self._progressColor

    @progressColor.setter
    def progressColor(self, value):
        self._progressColor = value

    @property
    def fontColor(self):
        return self._fontColor

    @fontColor.setter
    def fontColor(self, value):
        self._fontColor = value

    @property
    def backgroundColor(self):
        return self._backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, value):
        self._backgroundColor = value

    def paintEvent(self, event: QPaintEvent) -> None:
        outLength = min(self.width(), self.height())
        inLength = outLength - self.progressWidth
        margin = self.progressWidth / 2
        value = self.value * 360 / self.maximum
        painter = QPainter(self)
        self._path = QPainterPath()
        painter.setRenderHint(QPainter.Antialiasing)
        if self.enableBackground:
            self._createEmptyBar(painter, margin, margin, inLength, inLength, 0, 360 * 16)

        if self.enableText:
            self._createText(painter, 0, 0, inLength + self.fontSize, self.height() - self.fontSize / 3, Qt.AlignCenter, f"{self.value}")
        self._createProgressBar(painter, outLength, margin, margin, inLength, inLength, -90 * 16, -value * 16)

        painter.end()
        return super().paintEvent(event)

    def _createProgressBar(
        self, painter: QPainter, qreal: int,
        x: int, y: int, width: int, height: int, startAngle: int, spanAngle: int
    ):
        if self.progressColorType == "blur":
            progressColor = QRadialGradient(qreal / 2, qreal / 2, qreal / 2)
            progressColor.setColorAt(1 - ((self.progressWidth / qreal) * 2), self.progressBlurColor)
            progressColor.setColorAt(1 - (self.progressWidth / qreal), self.progressColor)
            progressColor.setColorAt(1, self.progressBlurColor)

        elif self.progressColorType == "gradation":
            #self.rounded = False
            progressColor = QConicalGradient(QPointF(qreal / 2, qreal / 2), 270)
            progressColor.setColorAt(0, self.progressBlurColor)
            progressColor.setColorAt(0.001, self.progressColor)
            progressColor.setColorAt(1, self.progressBlurColor)
        else:
            progressColor = QColor(self.progressColor)
        pen = QPen(progressColor, self.progressWidth, Qt.SolidLine)
        if self.rounded:
            pen.setCapStyle(Qt.RoundCap)
        else:
            pen.setCapStyle(Qt.FlatCap)

        painter.setPen(pen)
        painter.drawArc(x, x, width, height, startAngle, spanAngle)

    def _createText(self, painter: QPainter, x: int, y: int, width: int, height: int, flags: int, text: str):
        painter.setFont(self.font)
        pen = QPen(QColor(self.fontColor), self.progressWidth, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawText(x, y, width, height, flags, text)

    def _createEmptyBar(self, painter: QPainter, x: int, y: int, width: int, height: int, startAngle: int, spanAngle: int):
        pen = QPen(QColor(self._backgroundColor), self.progressWidth, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawArc(x, y, width, height, startAngle, spanAngle)
