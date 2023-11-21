from PySide2 import QtWidgets, QtGui
from typing import Final, TypeVar
import time

import QtCustom
import core

UI_FILE: Final = core.PATH_VIEWS / "schedule" / "schedule.ui"


class ScheduleWidget(QtWidgets.QWidget):
    """A custom widget class for scheduling, inheriting from QtWidgets.QWidget.

    This widget provides a user interface for scheduling.
    """
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
        "Access animationComboBox component from the UI."
        return self.ui.animationComboBox

    @property
    def circularSliderA(self) -> QtCustom.QCircularSlider:
        "Access circularSliderA component from the UI."
        return self.ui.circularSliderA

    @property
    def circularSliderB(self) -> QtCustom.QCircularSlider:
        "Access circularSliderB component from the UI."
        return self.ui.circularSliderB

    @property
    def circularSliderC(self) -> QtCustom.QCircularSlider:
        "Access circularSliderC component from the UI."
        return self.ui.circularSliderC

    @property
    def abstractProgressCircularA(self) -> QtCustom.QAbstractProgressCircular:
        "Access abstractProgressCircularA component from the UI."
        return self.ui.abstractProgressCircularA

    @property
    def abstractProgressCircularB(self) -> QtCustom.QAbstractProgressCircular:
        "Access abstractProgressCircularB component from the UI."
        return self.ui.abstractProgressCircularA

    @property
    def pushButtonA(self) -> QtWidgets.QPushButton:
        "Access pushButtonA component from the UI."
        return self.ui.pushButtonA

    @property
    def pushButtonB(self) -> QtWidgets.QPushButton:
        "Access pushButtonB component from the UI."
        return self.ui.pushButtonA

    @property
    def floatSlider(self) -> QtCustom.QFloatSlider:
        "Access floatSlider component from the UI."
        return self.ui.floatSlider

    @property
    def intSlider(self) -> QtCustom.QIntSlider:
        "Access intSlider component from the UI."
        return self.ui.intSlider

    @property
    def labelHeading(self) -> QtWidgets.QLabel:
        "Access labelHeading component from the UI."
        return self.ui.labelHeading

    @property
    def label(self) -> QtWidgets.QLabel:
        "Access label component from the UI."
        return self.ui.label

    @property
    def scrollArea(self) -> QtWidgets.QScrollArea:
        "Access scrollArea component from the UI."
        return self.ui.scrollArea

    @property
    def scrollAreaWidgetContents(self) -> QtWidgets.QWidget:
        "Access scrollAreaWidgetContents component from the UI."
        return self.ui.scrollAreaWidgetContents

    @property
    def flowLayout(self) -> QtCustom.QFlowLayout:
        "Access flowLayout component from the UI."
        return self.ui.QFlowLayout_FlowLayout

    def __initUI(self) -> None:
        "Initializes and configures the UI elements of the widget."
        self.__initAnimationComboBox()
        self.__initFlowLayout()
        self.__initCircularSliders()

    def __initAnimationComboBox(self) -> None:
        "Initializes and configures the animation combo box."
        self.animationComboBox.PopupOffset = (0, 10)
        self.animationComboBox.fade = True
        self.animationComboBox.slide = True
        self.animationComboBox.stretch = False
        [self.animationComboBox.addItem(f"Item {i}") for i in range(5)]

    def __initFlowLayout(self) -> None:
        "Initializes and configures the flow layout."
        [self.flowLayout.addWidget(
            QtWidgets.QPushButton(f"Btn {i}")) for i in range(50)]
        self.flowLayout.space = (15, 5)

    def __initCircularSliders(self) -> None:
        "Initializes and configures the circular sliders."
        self.pushButtonA.clicked.connect(
            lambda: self.progressStart(self.abstractProgressCircularA))
        self.abstractProgressCircularA.valueChanged.connect(
            self.progressStartCount)
        self.pushButtonB.clicked.connect(
            lambda: self.progressStart(self.abstractProgressCircularB))
        self.abstractProgressCircularB.valueChanged.connect(
            self.progressStartCount)

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

    def progressStart(self, progressWidget) -> None:
        "Initiates a progress simulation for a given progress widget."
        value: int = 0
        while value <= 100:
            time.sleep(0.1)
            progressWidget.setValue(value)
            value += 5

    def progressStartCount(self, value) -> None:
        "A callback function that prints the current progress value."
        print(f"count: {value}")
