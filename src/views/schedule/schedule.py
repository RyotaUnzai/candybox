import time
from PySide2 import QtWidgets, QtGui
from typing import Final, TypeVar

import QtCustom
import core

UI_FILE: Final = core.PATH_VIEWS / "schedule" / "schedule.ui"


class ScheduleWidget(QtWidgets.QWidget):
    Self = TypeVar("Self", bound="ScheduleWidget")

    def __init__(self: Self, parent: QtWidgets.QWidget = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.ui = QtCustom.ExUiLoader(UI_FILE)
        self.setObjectName("Schedule")
        self.__initUI()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.ui)

    @property
    def animationComboBox(self) -> QtCustom.QAnimationComboBox:
        return self.ui.animationComboBox

    @property
    def circularSliderA(self) -> QtCustom.QCircularSlider:
        return self.ui.circularSliderA

    @property
    def circularSliderB(self) -> QtCustom.QCircularSlider:
        return self.ui.circularSliderB

    @property
    def circularSliderC(self) -> QtCustom.QCircularSlider:
        return self.ui.circularSliderC

    @property
    def abstractProgressCircularA(self) -> QtCustom.QAbstractProgressCircular:
        return self.ui.abstractProgressCircularA

    @property
    def abstractProgressCircularB(self) -> QtCustom.QAbstractProgressCircular:
        return self.ui.abstractProgressCircularA

    @property
    def pushButtonA(self) -> QtWidgets.QPushButton:
        return self.ui.pushButtonA

    @property
    def pushButtonB(self) -> QtWidgets.QPushButton:
        return self.ui.pushButtonA

    @property
    def floatSlider(self) -> QtCustom.QFloatSlider:
        return self.ui.floatSlider

    @property
    def intSlider(self) -> QtCustom.QIntSlider:
        return self.ui.intSlider

    @property
    def labelHeading(self) -> QtWidgets.QLabel:
        return self.ui.labelHeading

    @property
    def label(self) -> QtWidgets.QLabel:
        return self.ui.label

    @property
    def scrollArea(self) -> QtWidgets.QScrollArea:
        return self.ui.scrollArea

    @property
    def scrollAreaWidgetContents(self) -> QtWidgets.QWidget:
        return self.ui.scrollAreaWidgetContents

    @property
    def flowLayout(self) -> QtCustom.QFlowLayout:
        return self.ui.QFlowLayout_FlowLayout

    def __initUI(self) -> None:
        self.__initAnimationComboBox()
        self.__initFlowLayout()
        self.__initCicularSliders()

    def __initAnimationComboBox(self) -> None:
        self.animationComboBox.PopupOffcet = (0, 10)
        self.animationComboBox.fade = True
        self.animationComboBox.slide = True
        self.animationComboBox.stretch = False
        [self.animationComboBox.addItem(f"Item {i}") for i in range(5)]

    def __initFlowLayout(self) -> None:
        [self.flowLayout.addWidget(QtWidgets.QPushButton(f"Btn {i}")) for i in range(50)]
        self.flowLayout.space = (15, 5)

    def __initCicularSliders(self) -> None:
        self.pushButtonA.clicked.connect(lambda: self.ProgressStart(self.AbstractProgressCircularA))
        self.abstractProgressCircularA.valueChanged.connect(self.ProgressStartCount)
        self.pushButtonB.clicked.connect(lambda: self.ProgressStart(self.AbstractProgressCircularB))
        self.abstractProgressCircularB.valueChanged.connect(self.ProgressStartCount)

        self.circularSliderB.progressColor = QtGui.QColor(128, 0, 255)
        self.circularSliderB.fontColor = "#888"
        self.circularSliderB.progressColorType = "gradation"
        self.circularSliderB.progressBlurColor = QtGui.QColor(255, 128, 0)
        self.circularSliderB.indicatorSubColor = QtGui.QColor(255, 128, 0)
        self.circularSliderB.value = 73
        self.circularSliderB.intensity = 100

        self.circularSliderC.progressColor = QtGui.QColor(0, 255, 128)
        self.circularSliderC.progressColorType = "blur"
        self.circularSliderC.indicatorSubColor = QtGui.QColor(255, 0, 128)
        self.circularSliderC.indicatorMainColor = QtGui.QColor(255, 0, 128)
        self.circularSliderC.value = 73

        self.abstractProgressCircularA.progressColorType = "gradation"
        self.abstractProgressCircularA.value = 73
        self.abstractProgressCircularB.progressColorType = "blur"
        self.abstractProgressCircularB.value = 73

    def ProgressStart(self, progressWidget) -> None:
        value: int = 0
        while value <= 100:
            time.sleep(0.1)
            progressWidget.setValue(value)
            value += 5

    def ProgressStartCount(self, value) -> None:
        print("ProgressCircular", value)


# class scheduleWidget(QWidget):

#     def __init__(self, parent=None, *args, **kwargs) -> None:

#         super(scheduleWidget, self).__init__(parent, *args, **kwargs)
#         uiLoader = QtCustom.QExUiLoader()
#         __uiFilePath = os.path.join(core.PATH_VIEWS, "schedule", "schedule.ui")
#         ui = uiLoader.load(__uiFilePath)
#         self.ui = ui
#         self.ui.setParent(parent)
#         self.setObjectName("Schedule")

#         self.Cb_qss.PopupOffcet = (0, 10)
#         self.Cb_qss.fade = True
#         self.Cb_qss.slide = True
#         self.Cb_qss.stretch = False
#         for i in range(5):
#             self.Cb_qss.addItem("Item %s" % i)

#         for i in range(50):
#             btn =
#             self.FlowLayout.addWidget(btn)

#         # self.FlowLayout.space = (15, 50)

#         self.APC_PushButtonA.clicked.connect(lambda: self.ProgressStart(self.AbstractProgressCircularA))
#         self.AbstractProgressCircularA.valueChanged.connect(self.ProgressStartCount)
#         self.APC_PushButtonB.clicked.connect(lambda: self.ProgressStart(self.AbstractProgressCircularB))
#         self.AbstractProgressCircularB.valueChanged.connect(self.ProgressStartCount)

#         self.CircularSliderB.progressColor = QColor(128, 0, 255)
#         self.CircularSliderB.fontColor = "#888"
#         self.CircularSliderB.progressColorType = "gradation"
#         self.CircularSliderB.progressBlurColor = QColor(255, 128, 0)
#         self.CircularSliderB.indicatorSubColor = QColor(255, 128, 0)
#         self.CircularSliderB.value = 73
#         self.CircularSliderB.intensity = 100

#         self.CircularSliderC.progressColor = QColor(0, 255, 128)
#         self.CircularSliderC.progressColorType = "blur"
#         self.CircularSliderC.indicatorSubColor = QColor(255, 0, 128)
#         self.CircularSliderC.indicatorMainColor = QColor(255, 0, 128)
#         self.CircularSliderC.value = 73

#         self.AbstractProgressCircularA.progressColorType = "gradation"
#         self.AbstractProgressCircularA.value = 73
#         self.AbstractProgressCircularB.progressColorType = "blur"
#         self.AbstractProgressCircularB.value = 73

#     def ProgressStart(self, progressWidget):
#         value: int = 0
#         while value <= 100:
#             time.sleep(0.1)
#             progressWidget.setValue(value)
#             value += 5

#     def ProgressStartCount(self, value):
#         print("ProgressCircular", value)

#     @property
#     def CircularSliderC(self) -> QtCustom.QCircularSlider:
#         return self.ui.CircularSliderC

#     @property
#     def CircularSliderB(self) -> QtCustom.QCircularSlider:
#         return self.ui.CircularSliderB

#     @property
#     def GridLayout(self) -> QGridLayout:
#         return self.ui.gridLayout

#     @property
#     def AbstractProgressCircularA(self) -> QtCustom.QAbstractProgressCircular:
#         return self.ui.AbstractProgressCircularA

#     @property
#     def AbstractProgressCircularB(self) -> QtCustom.QAbstractProgressCircular:
#         return self.ui.AbstractProgressCircularB

#     @property
#     def APC_PushButtonA(self) -> QPushButton:
#         return self.ui.APC_PushButtonA

#     @property
#     def APC_PushButtonB(self) -> QPushButton:
#         return self.ui.APC_PushButtonB

#     @property
#     def Cb_qss(self):
#         return self.ui.Cb_qss

#     @property
#     def FlowLayout(self) -> QtCustom.QFlowLayout:
#         return self.ui.QFlowLayout_FlowLayout
