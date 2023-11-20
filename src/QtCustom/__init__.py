

from .QAnimationComboBox import QAnimationComboBox
from .QFlowLayout import QFlowLayout
from .QExUiLoader import *
from .QFloatSlider import QFloatSlider
from .QIntSlider import QIntSlider
from .QProgressCircular import QProgressCircular
from .QAbstractProgressCircular import QAbstractProgressCircular
from .QCircularSlider import QCircularSlider

from PySide2 import QtWidgets
from PySide2.QtUiTools import loadUiType, QUiLoader
from pathlib import WindowsPath
from typing import Callable, Tuple, Type, Union, Final


def loadWidgetUiType(file: Union[WindowsPath, str]) -> Tuple[Type[QtWidgets.QWidget], Type[QtWidgets.QWidget]]:
    if isinstance(file, WindowsPath):
        file = file.as_posix()
    return loadUiType(file)


def loadWindowUiType(file: Union[WindowsPath, str]) -> Tuple[Type[QtWidgets.QMainWindow], Type[QtWidgets.QMainWindow]]:
    if isinstance(file, WindowsPath):
        file = file.as_posix()
    return loadUiType(file)


LoadWidgetUiType = Callable[[str], Tuple[Type[QtWidgets.QWidget],  Type[QtWidgets.QWidget]]]
LoadWindowUiType = Callable[[str], Tuple[Type[QtWidgets.QMainWindow],  Type[QtWidgets.QMainWindow]]]

Uiloader: Final = QUiLoader()
Uiloader.registerCustomWidget(QAnimationComboBox)
Uiloader.registerCustomWidget(QFlowLayout)
Uiloader.registerCustomWidget(QFloatSlider)
Uiloader.registerCustomWidget(QIntSlider)
Uiloader.registerCustomWidget(QProgressCircular)
Uiloader.registerCustomWidget(QAbstractProgressCircular)
Uiloader.registerCustomWidget(QCircularSlider)


def ExUiLoader(file: Union[WindowsPath, str]) -> Type[QtWidgets.QMainWindow]:
    if isinstance(file, WindowsPath):
        file = file.as_posix()
    return Uiloader.load(file)
