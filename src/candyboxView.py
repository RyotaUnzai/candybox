from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import views


class candyBoxCentralWidget(QWidget):
    __navigation = None
    __body = None

    def __init__(self, parent=None, *args, **kwargs) -> None:
        super(candyBoxCentralWidget, self).__init__(parent, *args, **kwargs)
        self.navigation = views.navigationWidget(self)
        self.navigation.setObjectName("navigation")
        self.body = views.bodyWidget(self)

        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(self.navigation.ui)
        self.hbox.addWidget(self.body)
        self.setLayout(self.hbox)

    @ property
    def navigation(self) -> views.navigationWidget:
        return self.__navigation

    @ navigation.setter
    def navigation(self, value):
        self.__navigation = value

    @ property
    def body(self) -> views.bodyWidget:
        return self.__body

    @ body.setter
    def body(self, value):
        self.__body = value


class candyBoxMainWindow(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(candyBoxMainWindow, self).__init__(parent, *args, **kwargs)

        self.setWindowTitle("CandyBox")
        self.setObjectName("candybox")
        self.cw = candyBoxCentralWidget(self)
        self.setCentralWidget(self.cw)
        self.resize(800, 600)

    #     self.setAutoFillBackground(True)
    #     self.setAttribute(Qt.WA_TranslucentBackground, True)

    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     painter.setRenderHint(QPainter.Antialiasing)
    #     path = QPainterPath()

    #     painter.setPen(Qt.NoPen)
    #     lGrad = QLinearGradient(90, 114, 117, 114)
    #     lGrad.setColorAt(0.0, QColor("#2c2b30"))
    #     lGrad.setColorAt(0.499999999, QColor("#2c2b30"))
    #     lGrad.setColorAt(0.5, QColor("#18181b"))
    #     lGrad.setColorAt(1.0, QColor("#2c2b30"))
    #     painter.setBrush(QBrush(lGrad))
    #     painter.drawRect(0, 0, self.geometry().width(), self.geometry().height())
    #     painter.setPen(Qt.NoPen)
    #     painter.setBrush(QColor("#00b8b8"))
    #     painter.drawRect(0, 0, 104, 87)
    #     path.addRoundedRect(0, 0, 104, 100, 0, 0)
    #     painter.end()
