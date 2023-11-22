from PySide2 import QtWidgets, QtCore
from typing import TypeVar


class QExToolTip(QtWidgets.QWidget):
    Self = TypeVar("Self", bound="QExToolTip")
    layout: QtWidgets.QBoxLayout
    timer: QtCore.QTimer

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setWindowFlags(
            QtCore.Qt.ToolTip | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint
        )
        self.layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.RightToLeft)
        self.setLayout(self.layout)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.startFadeOut)

        self.fadeOutAnimation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.fadeOutAnimation.setDuration(1000)
        self.fadeOutAnimation.setStartValue(1.0)
        self.fadeOutAnimation.setEndValue(0.0)
        self.fadeOutAnimation.finished.connect(self.hide)

    def leaveEvent(self, event):
        self.timer.start()
        super().leaveEvent(event)

    def enterEvent(self, event):
        self.timer.stop()
        self.setWindowOpacity(1.0)
        self.show()
        super().enterEvent(event)

    def startFadeOut(self):
        if self.fadeOutAnimation.state() != QtCore.QAbstractAnimation.Running:
            self.fadeOutAnimation.start()
