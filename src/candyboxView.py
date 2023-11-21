from PySide2 import QtWidgets, QtCore, QtGui

import views


class CandyBoxCentralWidget(QtWidgets.QWidget):
    navigation: views.NavigationWidget
    body: QtWidgets.QWidget
    home: views.HomeWidget
    message: views.MessageWidget
    schedule: views.ScheduleWidget
    preference: views.PreferenceWidget
    account: views.AccountWidget
    boxLayout: QtWidgets.QBoxLayout
    centralWidgetLayout: QtWidgets.QBoxLayout

    def __init__(self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
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

        # self.home.hide()
        self.message.hide()
        self.schedule.hide()
        self.preference.hide()
        self.account.hide()

    def __initUI(self) -> None:
        self.__initObjectNames()
        self.__initLayout()

    def __initObjectNames(self) -> None:
        self.body.setObjectName("Body")

    def __initLayout(self) -> None:
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
    cw: CandyBoxCentralWidget

    def __init__(self, parent: QtWidgets.QWidget = None, *args, **kwargs):
        super(CandyBoxMainWindow, self).__init__(parent, *args, **kwargs)
        self.cw = CandyBoxCentralWidget(self)
        self.__initUI()

    @property
    def centralWidget(self):
        return self.cw

    @property
    def navigation(self):
        return self.cw.navigation

    @property
    def body(self):
        return self.cw.body

    @property
    def home(self):
        return self.cw.home

    @property
    def message(self):
        return self.cw.message

    @property
    def schedule(self):
        return self.cw.schedule

    @property
    def preference(self):
        return self.cw.preference

    @property
    def account(self):
        return self.cw.account

    def __initUI(self) -> None:
        self.setCentralWidget(self.cw)
        self.resize(800, 600)

        self.setAutoFillBackground(True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.setWindowTitle("CandyBox")
        self.setObjectName("candybox")

    def paintEvent(self, event) -> None:
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
