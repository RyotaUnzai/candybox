from PySide2.QtUiTools import QUiLoader
from .QAnimationComboBox import *
from .QFlowLayout import *
from .QFloatSlider import *
from .QIntSlider import *
import typing
import PySide2


class QExUiLoader(QUiLoader):
    def createWidget(
        self, className: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
        name: str = ...
    ) -> PySide2.QtWidgets.QWidget:
        u"""Creates a new widget with the given parent and name using the class specified by className.
        You can use this function to create any of the widgets returned by the availableWidgets() function.

        The function is also used internally by the QUiLoader class whenever it creates a widget.
        Hence, you can subclass QUiLoader and reimplement this function to intervene process of constructing
        a user interface or widget. However, in your implementation, ensure that you call QUiLoader's version first.

        ExtendedWidgets:
            QAnimationComboBox
            QFloatSlider
            QIntSlider
        """
        isCustom = True
        if className == "QAnimationComboBox":
            widget = QAnimationComboBox(parent)
        elif className == "QFloatSlider":
            widget = QFloatSlider(parent)
        elif className == "QIntSlider":
            widget = QIntSlider(parent)
        else:
            isCustom = False
        if isCustom:
            widget.setObjectName(name)
            return widget

        return super().createWidget(className, parent, name)

    def createLayout(
        self, className: str, parent: typing.Optional[PySide2.QtCore.QObject] = ...,
        name: str = ...
    ) -> PySide2.QtWidgets.QLayout:
        u"""Creates a new layout with the given parent and name using the class specified by className.

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
