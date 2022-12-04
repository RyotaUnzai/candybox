# PySide2
from .QAbstractProgressCircular import *
import math


class QCircularSlider(QAbstractProgressCircular):
    _indicatorSize = 20
    _indicatorMainColor = QColor("#fff")
    _indicatorSubColor = QColor("#fff")
    _intensity = 20

    def __init__(self, parent=None):
        super().__init__(parent)
        self.indicatorSize = 20
        self._indicatorMainColor = QColor("#fff")
        self._indicatorSubColor = QColor("#fff")
        self._intensity = 20

    @property
    def intensity(self):
        return self._intensity

    @intensity.setter
    def intensity(self, value):
        self._intensity = value

    @property
    def indicatorMainColor(self):
        return self._indicatorMainColor

    @indicatorMainColor.setter
    def indicatorMainColor(self, value):
        self._indicatorMainColor = value

    @property
    def indicatorSubColor(self):
        return self._indicatorSubColor

    @indicatorSubColor.setter
    def indicatorSubColor(self, value):
        self._indicatorSubColor = value

    @property
    def indicatorSize(self):
        return self._indicatorSize

    @indicatorSize.setter
    def indicatorSize(self, value):
        self._indicatorSize = value

    def mouseReleaseEvent(self, event):
        self.mousePosX = event.globalX()
        self.mousePosY = event.y()

    def moveEvent(self, event: QMoveEvent) -> None:
        return super().moveEvent(event)

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.update()
        return super().resizeEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.addValue = int((event.globalX() - self.mousePosX) / self.intensity)
        self.value = self.value + self.addValue
        if self.value < 0:
            self.value = 0
        elif self.value > 100:
            self.value = 100
        self._path.lineTo(event.pos())
        self.update()
        return super().mouseMoveEvent(event)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.mousePosX = event.globalX()
        self._path.moveTo(event.pos())
        self.update()
        return super().mousePressEvent(event)

    def paintEvent(self, event: QPaintEvent) -> None:
        outLength = min(self.width(), self.height())
        circluarRadius = outLength - self.indicatorSize
        inLength = outLength - self.progressWidth - self.indicatorSize / 2
        margin = self.indicatorSize / 2
        value = self.value * 360 / self.maximum
        painter = QPainter(self)
        self._path = QPainterPath()
        painter.setRenderHint(QPainter.Antialiasing)

        if self.enableBackground:
            self._createEmptyBar(painter, margin, margin, circluarRadius, circluarRadius, 0, 360 * 16)

        if self.enableText:
            self._createText(painter, 0, 0, inLength + self.fontSize / 2 * 3, self.height() - self.fontSize / 3, Qt.AlignCenter, f"{self.value}")

        self._createProgressBar(painter, outLength, margin, margin, circluarRadius, circluarRadius, -90 * 16, -value * 16)

        self._createIndicator(painter, circluarRadius, value)

        painter.end()

    def _createProgressBar(
        self, painter: QPainter, qreal: int,
        x: int, y: int, width: int, height: int, startAngle: int, spanAngle: int
    ):
        if self.progressColorType == "blur":
            progressColor = QRadialGradient(qreal / 2, qreal / 2, qreal / 2)
            progressColor.setColorAt(1 - ((self.progressWidth / qreal) * 4), self.progressBlurColor)
            progressColor.setColorAt(1 - (self.progressWidth / qreal * 2), self.progressColor)
            progressColor.setColorAt(1, self.progressBlurColor)

        elif self.progressColorType == "gradation":
            self.rounded = False
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

    def _createIndicator(self, painter: QPainter, lenght: int, angle: int):
        #    /|
        #  C/ |
        #  /  |A
        # /   |
        # ⁻⁻⁻⁻⁻
        #   B
        radius = lenght / 2
        # C * Sinθ = A
        sinTheta = math.sin(math.radians(angle))
        x = int(-radius * sinTheta)
        # C * Cosθ = b
        cosTheta = math.cos(math.radians(angle))
        y = int(radius * cosTheta)

        indicatorPos = (x + radius, y + radius)

        pen = QPen(self.indicatorMainColor, 2, Qt.SolidLine)
        painter.setBrush(Qt.NoBrush)
        painter.setPen(pen)
        painter.drawEllipse(indicatorPos[0] + 1, indicatorPos[1] + 1, self.indicatorSize - 2, self.indicatorSize - 2)

        painter.setBrush(QBrush(self.indicatorSubColor))
        painter.drawEllipse(indicatorPos[0] + 5, indicatorPos[1] + 5, self.indicatorSize - 10, self.indicatorSize - 10)
