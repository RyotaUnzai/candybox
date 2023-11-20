from typing import Final, Optional, Union, Type, Tuple, Callable
from PySide2 import QtWidgets, QtCore
from PySide2.QtUiTools import QUiLoader, loadUiType
from pathlib import WindowsPath

from .QFlowLayout import QFlowLayout
from .QFloatSlider import QFloatSlider
from .QIntSlider import QIntSlider
from .QProgressCircular import QProgressCircular
from .QAbstractProgressCircular import QAbstractProgressCircular
from .QCircularSlider import QCircularSlider
from .QAnimationComboBox import QAnimationComboBox


class QExUiLoader(QUiLoader):
    def createLayout(
        self, className: str, parent: Optional[QtCore.QObject] = ..., name: str = ...
    ) -> QtWidgets.QLayout:
        """Creates a new layout with the given parent and name using the class specified by className.

        The function is also used internally by the QUiLoader class whenever it creates a widget.
        Hence, you can subclass QUiLoader and reimplement this function to intervene process of constructing
        a user interface or widget. However, in your implementation, ensure that you call QUiLoader's version first.

        When using an extended layout, you must add the Flag of the layout you wish to use to the ObjectName
        in Qt Designer or other software. The Flag is to be a <CUSTOM_LAYOUT_CLASS_NAME>_.

        ExtendedLayout:
            QFlowLayout - Flag: QFlowLayout_
        """
        isCustom = True
        if "QFlowLayout_" in name:
            layout = QFlowLayout()
            name = name.replace("QFlowLayout_", "")
        else:
            isCustom = False
        if isCustom:
            layout.setObjectName(name)
            return layout

        return super(QExUiLoader, self).createLayout(className, parent, name)


Uiloader: Final = QExUiLoader()
Uiloader.registerCustomWidget(QAnimationComboBox)
Uiloader.registerCustomWidget(QFloatSlider)
Uiloader.registerCustomWidget(QIntSlider)
Uiloader.registerCustomWidget(QProgressCircular)
Uiloader.registerCustomWidget(QAbstractProgressCircular)
Uiloader.registerCustomWidget(QCircularSlider)


def ExUiLoader(file: Union[WindowsPath, str]) -> Type[QtWidgets.QMainWindow]:
    if isinstance(file, WindowsPath):
        file = file.as_posix()
    return Uiloader.load(file)


def loadWidgetUiType(file: Union[WindowsPath, str]) -> Tuple[
    Type[QtWidgets.QWidget],
    Type[QtWidgets.QWidget]
]:
    if isinstance(file, WindowsPath):
        file = file.as_posix()
    return loadUiType(file)


def loadWindowUiType(file: Union[WindowsPath, str]) -> Tuple[
    Type[QtWidgets.QMainWindow],
    Type[QtWidgets.QMainWindow]
]:
    if isinstance(file, WindowsPath):
        file = file.as_posix()
    return loadUiType(file)


LoadWidgetUiType = Callable[
    [str],
    Tuple[Type[QtWidgets.QWidget], Type[QtWidgets.QWidget]]
]
LoadWindowUiType = Callable[
    [str],
    Tuple[Type[QtWidgets.QMainWindow], Type[QtWidgets.QMainWindow]]
]
