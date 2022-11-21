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

        self.APC_PushButton.clicked.connect(self.ProgressStart)
        self.AbstractProgressCircular.valueChanged.connect(self.ProgressStartCount)

        self.CircularSliderB.progressColor = QColor(128, 0, 255)
        self.CircularSliderB.fontColor = "#888"
        self.CircularSliderB.progressColorType = "gradation"
        self.CircularSliderB.progressBlurColor = QColor(255, 128, 0)
        self.CircularSliderB.indicatorSubColor = QColor(255, 128, 0)

        self.CircularSliderC.progressColor = QColor(0, 255, 128)
        self.CircularSliderC.progressColorType = "blur"
        self.CircularSliderC.indicatorSubColor = QColor(255, 0, 128)
        self.CircularSliderC.indicatorMainColor = QColor(255, 0, 128)

        self.ui.AbstractProgressCircularB.progressColorType = "blur"
        self.ui.AbstractProgressCircularB.value = 73

    def ProgressStart(self):
        value: int = 0
        while value <= 100:
            time.sleep(0.1)
            self.AbstractProgressCircular.setValue(value)
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
    def AbstractProgressCircular(self) -> QtCustom.QAbstractProgressCircular:
        return self.ui.AbstractProgressCircular

    @property
    def APC_PushButton(self) -> QPushButton:
        return self.ui.APC_PushButton

    @property
    def Cb_qss(self):
        return self.ui.Cb_qss

    @property
    def FlowLayout(self) -> QtCustom.QFlowLayout:
        return self.ui.QFlowLayout_FlowLayout
