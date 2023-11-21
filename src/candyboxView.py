from PySide2 import QtWidgets, QtCore, QtGui
from typing import TypeVar

import views


class CandyBoxCentralWidget(QtWidgets.QWidget):
    Self = TypeVar("Self", bound="CandyBoxCentralWidget")
    navigation: views.NavigationWidget
    body: QtWidgets.QWidget
    home: views.HomeWidget
    message: views.MessageWidget
    schedule: views.ScheduleWidget
    preference: views.PreferenceWidget
    account: views.AccountWidget
    boxLayout: QtWidgets.QBoxLayout
    centralWidgetLayout: QtWidgets.QBoxLayout

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> Self:
        super(CandyBoxCentralWidget, self).__init__(parent, *args, **kwargs)
        self.navigation = views.NavigationWidget(self)
        self.body = QtWidgets.QWidget(self)
        self.home = views.HomeWidget(self)
        self.message = views.MessageWidget(self)
        self.schedule = views.ScheduleWidget(self)
        self.preference = views.PreferenceWidget(self)
        self.account = views.AccountWidget(self)
        self.boxLayout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom, self)
        self.centralWidgetLayout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight, self)

        self.__initUI()

    def __initUI(self: Self) -> None:
        self.__initObjectNames()
        self.__initLayout()

    def __initObjectNames(self: Self) -> None:
        self.body.setObjectName("Body")

    def __initLayout(self: Self) -> None:
        self.body.setLayout(self.boxLayout)

        self.boxLayout.addWidget(self.home)
        self.boxLayout.addWidget(self.message)
        self.boxLayout.addWidget(self.schedule)
        self.boxLayout.addWidget(self.preference)
        self.boxLayout.addWidget(self.account)

        self.centralWidgetLayout.addWidget(self.navigation)
        self.centralWidgetLayout.addWidget(self.body)
        self.setLayout(self.centralWidgetLayout)


class CandyBoxMainWindow(QtWidgets.QMainWindow):
    Self = TypeVar("Self", bound="CandyBoxMainWindow")
    cw: CandyBoxCentralWidget

    def __init__(self: Self,parent: QtWidgets.QWidget = None, *args, **kwargs):
        super(CandyBoxMainWindow, self).__init__(parent, *args, **kwargs)
        self.cw = CandyBoxCentralWidget(self)
        self.__initUI()

    def __initUI(self: Self) -> None:
        self.setAutoFillBackground(True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.resize(800, 600)
        self.setWindowTitle("CandyBox")
        self.setObjectName("Candybox")

        self.setCentralWidget(self.cw)
        self.__initShowSection()

    def __initShowSection(self: Self) -> None:
        # self.home.hide()
        self.message.hide()
        self.schedule.hide()
        self.preference.hide()
        self.account.hide()

    def paintEvent(self: Self, event) -> None:
        painter: QtGui.QPainter = QtGui.QPainter(self)
        painterPath: QtGui.QPainterPath = QtGui.QPainterPath()
        linearGradient: QtGui.QLinearGradient = QtGui.QLinearGradient(90, 114, 117, 114)

        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        painter.setPen(QtCore.Qt.NoPen)
        linearGradient.setColorAt(0.0, QtGui.QColor("#2c2b30"))
        linearGradient.setColorAt(0.499999999, QtGui.QColor("#2c2b30"))
        linearGradient.setColorAt(0.5, QtGui.QColor("#18181b"))
        linearGradient.setColorAt(1.0, QtGui.QColor("#2c2b30"))

        painter.setBrush(QtGui.QBrush(linearGradient))
        painter.drawRect(0, 0, self.geometry().width(), self.geometry().height())
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QColor("#00b8b8"))
        painter.drawRect(0, 0, 104, 87)
        painterPath.addRoundedRect(0, 0, 104, 87, 0, 0)
        painter.end()

        super(CandyBoxMainWindow, self).paintEvent(event)

    @property
    def centralWidget(self: Self) -> QtWidgets.QWidget:
        return self.cw

    @property
    def navigation(self: Self) -> views.NavigationWidget:
        return self.cw.navigation

    @property
    def body(self: Self) -> QtWidgets.QWidget:
        return self.cw.body

    @property
    def boxLayout(self: Self) -> QtWidgets.QBoxLayout:
        return self.cw.boxLayout

    @property
    def home(self: Self) -> views.HomeWidget:
        return self.cw.home

    @property
    def message(self: Self) -> views.MessageWidget:
        return self.cw.message

    @property
    def schedule(self: Self) -> views.ScheduleWidget:
        return self.cw.schedule

    @property
    def preference(self: Self) -> views.NavigationWidget:
        return self.cw.preference

    @property
    def account(self: Self) -> views.AccountWidget:
        return self.cw.account
