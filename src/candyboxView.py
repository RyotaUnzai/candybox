from PySide2 import QtWidgets, QtCore, QtGui

import views


class candyBoxCentralWidget(QtWidgets.QWidget):
    navigation: views.navigationWidget
    bodyWidget: QtWidgets.QWidget
    message: views.MessageWidget
    settingWidget: views.settingWidget
    boxLayout: QtWidgets.QBoxLayout
    centralWidgetLayout: QtWidgets.QBoxLayout

    def __init__(self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super(candyBoxCentralWidget, self).__init__(parent, *args, **kwargs)
        self.navigation = views.navigationWidget(self)
        self.bodyWidget = QtWidgets.QWidget(self)
        self.home = views.HomeWidget(self)
        self.message = views.MessageWidget(self)
        self.schedule = views.ScheduleWidget(self)
        self.settingWidget = views.settingWidget(self)
        self.account = views.AccountWidget(self)
        self.boxLayout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom, self)
        self.centralWidgetLayout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight, self)
        self.__initUI()

    def __initUI(self) -> None:
        self.bodyWidget.setObjectName("bodyWidget")
        self.navigation.setObjectName("navigation")
        self.scheduleUI = self.schedule.ui
        self.settingUI = self.settingWidget.ui

        self.__initLayout()

        self.home.hide()
        self.message.hide()
        # self.scheduleUI.hide()
        self.settingUI.hide()
        self.account.hide()

    def __initLayout(self) -> None:
        self.bodyWidget.setLayout(self.boxLayout)

        self.boxLayout.addWidget(self.home)
        self.boxLayout.addWidget(self.message)
        self.boxLayout.addWidget(self.scheduleUI)
        self.boxLayout.addWidget(self.settingUI)
        self.boxLayout.addWidget(self.account)

        self.centralWidgetLayout.addWidget(self.navigation.ui)
        self.centralWidgetLayout.addWidget(self.bodyWidget)
        self.setLayout(self.centralWidgetLayout)


class candyBoxMainWindow(QtWidgets.QMainWindow):
    cw: candyBoxCentralWidget

    def __init__(self, parent: QtWidgets.QWidget = None, *args, **kwargs):
        super(candyBoxMainWindow, self).__init__(parent, *args, **kwargs)
        self.cw = candyBoxCentralWidget(self)
        self.__initUI()

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

        super(candyBoxMainWindow, self).paintEvent(event)
