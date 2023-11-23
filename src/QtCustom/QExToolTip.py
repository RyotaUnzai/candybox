from PySide2 import QtWidgets, QtCore, QtGui
from typing import TypeVar, Final


class QExToolTip(QtWidgets.QWidget):
    Self = TypeVar("Self", bound="QExToolTip")
    layout: QtWidgets.QBoxLayout
    timer: QtCore.QTimer
    fadeOutAnimation: QtCore.QPropertyAnimation
    backgroundColor: Final = QtGui.QColor("#2b2b2b")
    round: int = 8
    opacity: float = 0.95

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.timer = QtCore.QTimer(self)
        self.fadeOutAnimation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.ToolTip | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.__initAnimation()

    def __initAnimation(self: Self) -> None:
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.startFadeOut)
        self.fadeOutAnimation.setDuration(500)
        self.fadeOutAnimation.setStartValue(1.0)
        self.fadeOutAnimation.setEndValue(0.0)
        self.fadeOutAnimation.finished.connect(self.hide)

    def paintEvent(self: Self, event: QtGui.QPaintEvent, *args, **kwargs):
        painter: QtGui.QPainter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setOpacity(self.opacity)
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QBrush(self.backgroundColor))
        painter.drawRoundedRect(self.rect(), self.round, self.round)
        painter.end()

    def leaveEvent(self: Self, event) -> None:
        self.timer.start()
        super().leaveEvent(event)

    def enterEvent(self: Self, event) -> None:
        self.setWindowOpacity(1.0)
        self.show()
        super().enterEvent(event)

    def show(self: Self, *args, **kwargs) -> None:
        self.timer.setInterval(1000)
        self.timer.stop()
        return super().show(**kwargs)

    def startFadeOut(self: Self) -> None:
        if self.fadeOutAnimation.state() != QtCore.QAbstractAnimation.Running:
            self.fadeOutAnimation.start()
