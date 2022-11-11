# PySide2
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class QFloatSlider(QWidget):
    """QFloatSlider widget

    The QFloatSlider widget is a widget that displays an float SpinBox and Slider.

    Slots:
        setRange(min, max)
        setValue(value)
        setDirection(direction)
        setOrientation(orientation)
        setValue(value)

    Signals:
        actionTriggered(action)
        rangeChanged(min, max)
        sliderMoved(value)
        sliderPressed()
        sliderReleased()
        valueChanged(value)
    """
    actionTriggered = Signal(float)
    valueChanged = Signal(float)
    sliderPressed = Signal(bool)
    sliderReleased = Signal(bool)
    rangeChanged = Signal(float, float)
    sliderMoved = Signal(float)
    __value = 0.0

    def __init__(self, parent=None, direction=None, *args, **kwargs):
        super(QFloatSlider, self).__init__(parent, *args, **kwargs)
        if direction is not None:
            self.__direction = direction
            if self.__direction == QBoxLayout.RightToLeft or self.__direction == QBoxLayout.LeftToRight:
                self.__slider = QSlider(Qt.Horizontal)
            else:
                self.__slider = QSlider(Qt.Vertical)
        else:
            self.__direction = QBoxLayout.LeftToRight
            self.__slider = QSlider(Qt.Horizontal)
        self.__spinBox = QDoubleSpinBox()
        self.__layout = QBoxLayout(self.__direction)

        self.__initUI()

    def __initUI(self):
        self.__spinBox.setMinimumWidth(70)
        self.__spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        # spinBox and slider Signals&Slots
        self.__spinBox.valueChanged[float].connect(self.__valueChangedCallback)
        self.__slider.valueChanged[int].connect(self.__valueChangedCallback)

        # slider Signals&Slots
        self.__slider.actionTriggered[int].connect(self.__actionTriggeredCallback)
        self.__slider.sliderPressed.connect(self.__sliderPressedCallback)
        self.__slider.sliderReleased.connect(self.__sliderReleasedCallback)
        self.__slider.rangeChanged[int, int].connect(self.__rangeChangedCallback)
        self.__slider.sliderMoved[int].connect(self.__sliderMovedCallback)

        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__layout.addWidget(self.__spinBox)
        self.__layout.addWidget(self.__slider)
        self.setLayout(self.__layout)

    def setPrefix(self, prefix):
        """This property holds the prefix of the spin box on QFloatSlider.
The prefix is prepended to the start of the displayed value. Typical use is to display a unit of measurement or a currency symbol.
To turn off the prefix display, set this property to an empty string. The default is no prefix.
The prefix is not displayed when value() == minimum() and specialValueText() is set.

If no prefix is set, returns an empty string.
        Args:
            prefix (_type_): _description_
        """
        self.__spinBox.setPrefix(prefix)

    def setSuffix(self, suffix):
        """This property holds the suffix of the spin box on QFloatSlider.
The suffix is appended to the end of the displayed value. Typical use is to display a unit of measurement or a currency symbol.
To turn off the suffix display, set this property to an empty string. The default is no suffix. The suffix is not displayed for the minimum() if specialValueText() is set.
If no suffix is set, returns an empty string.
        Args:
            suffix (str or unicode): _description_
        """
        self.__spinBox.setSuffix(suffix)

    def setSpecialValueText(self, txt):
        """This property holds the special-value text.
If set, the QFloatBox will display this text instead of a numeric value whenever the current value is equal to minimum().
Typical use is to indicate that this choice has a special (default) meaning.

        Args:
            txt (str or unicode): special-value text.
        """
        self.__spinBox.setSpecialValueText(txt)

    def setSingleStep(self, value):
        """This property holds the step value..
The smaller of two natural steps that a QFloatslider provides and typically corresponds to the user pressing an arrow key.
If the propety is modified during an auto repeating key event, behavior is undefined.
When a value other than QAbstractSpinBox.NoButtons is set in setButtonSymbols.
When the user uses the arrows to change the spin box's value the value will be incremented/decremented by the amount of the singleStep.
The default value is 1. Setting a singleStep value of less than 0 does nothing.

        Args:
            value (float): _description_
        """
        self.__spinBox.setSingleStep(value)
        self.__slider.setSingleStep(value)

    def value(self):
        """This property holds the value of the QFloatSlider.
will emit valueChanged() if the new value is different from the old one.

        Returns:
            float: the value of the QFloatSlider
        """
        return self.__value

    def setValue(self, value):
        """This property holds the value of the QFloatSlider
will emit valueChanged() if the new calue is different from the old one.

        Parameters:
            value: float
        """
        self.__value = value
        self.__spinBox.setValue(self.__value)

    def setDirection(self, direction):
        """Sets the direction of this layout to direction.

        QBoxLayout.LeftToRight: Horizontal from left to right.
        QBoxLayout.RightToLeft: Horizontal from right to left.
        QBoxLayout.TopToBottom: Vertical from top to bottom.
        QBoxLayout.BottomToTop: Vertical from bottom to top.

        Args:
            direction (Direction): _description_
        """
        if direction == QBoxLayout.RightToLeft or direction == QBoxLayout.LeftToRight:
            self.__slider.setOrientation(Qt.Horizontal)
        else:
            self.__slider.setOrientation(Qt.Vertical)
        self.__direction = direction
        self.__layout.setDirection(self.__direction)

    def setOrientation(self, orientation):
        """This property holds the orientation of the slider

The orientation must be Qt.Vertical or Qt.Horizontal(the default) .

        Args:
            orientation (orientation): _description_
        """
        self.__slider.setOrientation(orientation)

    def __actionTriggeredCallback(self, action):
        self.actionTriggered.emit(action)

    def __rangeChangedCallback(self, min, max):
        self.rangeChanged.emit(min, max)

    def __sliderMovedCallback(self, value):
        self.sliderMoved.emit(value * 0.01)

    def __sliderPressedCallback(self):
        self.sliderPressed.emit(self.__slider.isSliderDown())

    def __sliderReleasedCallback(self):
        self.sliderReleased.emit(self.__slider.isSliderDown())

    def __valueChangedCallback(self, value):
        sender = self.sender()
        if sender == self.__spinBox:
            try:
                self.__value = value
            except ZeroDivisionError:
                self.__value = 0
            self.__slider.blockSignals(True)
            self.__slider.setValue(value * 100)
            self.__slider.blockSignals(False)
        else:
            try:
                self.__value = value * 0.01
            except ZeroDivisionError:
                self.__value = 0
            self.__spinBox.blockSignals(True)
            self.__spinBox.setValue(self.__value)
            self.__spinBox.blockSignals(False)

        self.valueChanged.emit(self.__value)

    def buttonSymbols(self):
        """This enum type describes the symbols that can be displayed on the buttons in a spin box.

        QAbstractSpinBox.UpDownArrows: Little arrows in the classic style.
        QAbstractSpinBox.PlusMinus: + and - symbols.
        QAbstractSpinBox.NoButtons: Don't display buttons.
        """
        return self.__spinBox.ButtonSymbols()

    def ButtonSymbols(self):
        """This enum type describes the symbols that can be displayed on the buttons in a spin box.

        QAbstractSpinBox.UpDownArrows: Little arrows in the classic style.
        QAbstractSpinBox.PlusMinus: + and - symbols.
        QAbstractSpinBox.NoButtons: Don't display buttons.
        """
        return self.__spinBox.ButtonSymbols()

    def setButtonSymbols(self, bs=QAbstractSpinBox.NoButtons):
        """This property holds the current button symbol mode.
The possible values can be either UpDownArrows or PlusMinus.
The default is NoButtons.
Note that some styles might render PlusMinus and UpDownArrows identically.

        Args:
            bs ButtonSymbols: _description_. Defaults to QAbstractSpinBox.UpDownNoButtonsArrows.
        """
        self.__spinBox.setButtonSymbols(bs)

    def correctionMode(self):
        """This enum type describes the mode the spinbox will use to correct an Floatermediate value if editing finishes.

        QAbstractSpinBox.CorrectToPreviousValue: The spinbox will revert to the last valid value.
        QAbstractSpinBox.CorrectToNearestValue: The spinbox will revert to the nearest valid value.
        """
        return self.__spinBox.CorrectionMode()

    def CorrectionMode(self):
        """This enum type describes the mode the spinbox will use to correct an Floatermediate value if editing finishes.

        QAbstractSpinBox.CorrectToPreviousValue: The spinbox will revert to the last valid value.
        QAbstractSpinBox.CorrectToNearestValue: The spinbox will revert to the nearest valid value.
        """
        return self.__spinBox.CorrectionMode()

    def setCorrectionMode(self, cm=QAbstractSpinBox.CorrectToPreviousValue):
        """This property holds the mode to correct an Floatermediate value if editing finishes.
The default mode is CorrectToPreviousValue.

        Args:
            cm (CorrectionMode): _description_. Defaults to QAbstractSpinBox.CorrectToPreviousValue.
        """
        self.__spinBox.setCorrectionMode(cm)

    def setRange(self, min, max):
        """Convenience function to set the minimum, and maximum values with a single function call.

        Args:
            min (float): minimum value
            max (float): maximum value
        """
        self.__spinBox.setRange(min, max)
        self.__slider.setRange(min, max)

    def setSlider(self, value):
        self.__isSlider = value

    @property
    def slider(self):
        pass

    @slider.getter
    def slider(self):
        try:
            if self.__isSlider:
                return self.__slider
            return None
        except Exception:
            print("""# Error: AttributeError:
setSlider is not called.""")
            raise

    def setSpinbox(self, value):
        self.__isSpinbox = value

    @property
    def spinbox(self):
        pass

    @spinbox.getter
    def spinbox(self):
        try:
            if self.__isSpinbox:
                return self.__spinbox
            return None
        except Exception:
            print("""# Error: AttributeError:
setSpinbox is not called.""")
            raise

    def setSpinboxMinimumSize(self, *args):
        if len(args) == 2:
            self.__spinBox.setMinimumSize(args[0], args[1])
        else:
            self.__spinBox.setMinimumSize(args[0])

    def setSpinboxMinimumWidth(self, value):
        self.__spinBox.setMinimumWidth(value)

    def setSpinboxMinimumHeight(self, value):
        self.__spinBox.setMinimumWidth(value)

    def setSpinboxMaximumSize(self, *args):
        if len(args) == 2:
            self.__spinBox.setMaximumSize(args[0], args[1])
        else:
            self.__spinBox.setMaximumSize(args[0])

    def setSpinboxMaximumWidth(self, value):
        self.__spinBox.setMaximumWidth(value)

    def setSpinboxMaximumHeight(self, value):
        self.__spinBox.setMaximumWidth(value)

    def setSliderMinimumSize(self, *args):
        if len(args) == 2:
            self.__slider.setMinimumSize(args[0], args[1])
        else:
            self.__slider.setMinimumSize(args[0])

    def setSliderMinimumWidth(self, value):
        self.__slider.setMinimumWidth(value)

    def setSliderMinimumHeight(self, value):
        self.__slider.setMinimumWidth(value)

    def setSliderMaximumSize(self, *args):
        if len(args) == 2:
            self.__slider.setMaximumSize(args[0], args[1])
        else:
            self.__slider.setMaximumSize(args[0])

    def setSliderMaximumWidth(self, value):
        self.__slider.setMaximumWidth(value)

    def setSliderMaximumHeight(self, value):
        self.__slider.setMaximumWidth(value)

    def spinboxMinimumSize(self):
        return self.__spinBox.minimumSize()

    def spinboxMinimumWidth(self):
        return self.__spinBox.minimumWidth()

    def spinboxMinimumHeight(self):
        return self.__spinBox.minimumWidth()

    def spinboxMaximumSize(self):
        return self.__spinBox.maximumSize()

    def spinboxMaximumWidth(self):
        return self.__spinBox.maximumWidth()

    def spinboxMaximumHeight(self):
        return self.__spinBox.maximumWidth()

    def sliderMinimumSize(self):
        return self.__slider.minimumSize()

    def sliderMinimumWidth(self):
        return self.__slider.minimumWidth()

    def sliderMinimumHeight(self):
        return self.__slider.minimumWidth()

    def sliderMaximumSize(self):
        return self.__slider.maximumSize()

    def sliderMaximumWidth(self):
        return self.__slider.maximumWidth()

    def sliderMaximumHeight(self):
        return self.__slider.maximumWidth()
