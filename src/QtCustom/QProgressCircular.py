# PySide2
from .QAbstractProgressCircular import *


class QProgressCircular(QAbstractProgressCircular):

    def __init__(self, parent=None):
        super(QProgressCircular, self).__init__(parent)

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
            self._createText(
                painter, 0, 0,
                inLength + self.fontSize, self.height() - self.fontSize / 3,
                Qt.AlignCenter, f"{self.value}{self.suffix}"
            )
        self._createProgressBar(painter, outLength, margin, margin, inLength, inLength, -90 * 16, -value * 16)

        painter.end()
