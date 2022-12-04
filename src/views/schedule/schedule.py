import os
import core
import time
from PySide2.QtWidgets import QWidget, QPushButton, QGridLayout
from PySide2.QtGui import QColor

import QtCustom


class scheduleWidget(QWidget):

    def __init__(self, parent=None, *args, **kwargs) -> None:

        super(scheduleWidget, self).__init__(parent, *args, **kwargs)
        uiLoader = QtCustom.QExUiLoader()
        __uiFilePath = os.path.join(core.PATH_VIEWS, "schedule", "schedule.ui")
        ui = uiLoader.load(__uiFilePath)
        self.ui = ui
        self.ui.setParent(parent)
        self.setObjectName("Schedule")

        self.Cb_qss.PopupOffcet = (0, 10)
        self.Cb_qss.fade = True
        self.Cb_qss.slide = True
        self.Cb_qss.stretch = False
        for i in range(5):
            self.Cb_qss.addItem("Item %s" % i)

        for i in range(5):
            btn = QPushButton("%s" % i)
            self.FlowLayout.addWidget(btn)

        self.FlowLayout.space = (50, 10)

        self.APC_PushButtonA.clicked.connect(lambda: self.ProgressStart(self.AbstractProgressCircularA))
        self.AbstractProgressCircularA.valueChanged.connect(self.ProgressStartCount)
        self.APC_PushButtonB.clicked.connect(lambda: self.ProgressStart(self.AbstractProgressCircularB))
        self.AbstractProgressCircularB.valueChanged.connect(self.ProgressStartCount)

        self.CircularSliderB.progressColor = QColor(128, 0, 255)
        self.CircularSliderB.fontColor = "#888"
        self.CircularSliderB.progressColorType = "gradation"
        self.CircularSliderB.progressBlurColor = QColor(255, 128, 0)
        self.CircularSliderB.indicatorSubColor = QColor(255, 128, 0)
        self.CircularSliderB.value = 73
        self.CircularSliderB.intensity = 100

        self.CircularSliderC.progressColor = QColor(0, 255, 128)
        self.CircularSliderC.progressColorType = "blur"
        self.CircularSliderC.indicatorSubColor = QColor(255, 0, 128)
        self.CircularSliderC.indicatorMainColor = QColor(255, 0, 128)
        self.CircularSliderC.value = 73

        self.AbstractProgressCircularA.progressColorType = "gradation"
        self.AbstractProgressCircularA.value = 73
        self.AbstractProgressCircularB.progressColorType = "blur"
        self.AbstractProgressCircularB.value = 73

    def ProgressStart(self, progressWidget):
        value: int = 0
        while value <= 100:
            time.sleep(0.1)
            progressWidget.setValue(value)
            value += 5

    def ProgressStartCount(self, value):
        print("ProgressCircular", value)

    @property
    def CircularSliderC(self) -> QtCustom.QCircularSlider:
        return self.ui.CircularSliderC

    @property
    def CircularSliderB(self) -> QtCustom.QCircularSlider:
        return self.ui.CircularSliderB

    @property
    def GridLayout(self) -> QGridLayout:
        return self.ui.gridLayout

    @property
    def AbstractProgressCircularA(self) -> QtCustom.QAbstractProgressCircular:
        return self.ui.AbstractProgressCircularA

    @property
    def AbstractProgressCircularB(self) -> QtCustom.QAbstractProgressCircular:
        return self.ui.AbstractProgressCircularB

    @property
    def APC_PushButtonA(self) -> QPushButton:
        return self.ui.APC_PushButtonA

    @property
    def APC_PushButtonB(self) -> QPushButton:
        return self.ui.APC_PushButtonB

    @property
    def Cb_qss(self):
        return self.ui.Cb_qss

    @property
    def FlowLayout(self) -> QtCustom.QFlowLayout:
        return self.ui.QFlowLayout_FlowLayout
