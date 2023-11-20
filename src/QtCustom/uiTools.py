from PySide2 import QtWidgets
from PySide2.QtUiTools import loadUiType
from pathlib import WindowsPath
from typing import Callable, Tuple, Type, Union


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
