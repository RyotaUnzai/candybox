import os
import core
from PySide2.QtWidgets import QWidget
from PySide2.QtUiTools import loadUiType, QUiLoader


class scheduleWidget(QWidget):

    def __init__(self, parent=None, *args, **kwargs) -> None:

        super(scheduleWidget, self).__init__(parent, *args, **kwargs)
        uiLoader = QUiLoader()
        __uiFilePath = os.path.join(core.PATH_VIEWS, "schedule", "schedule.ui")
        ui = uiLoader.load(__uiFilePath)
        self.ui = ui
        self.ui.setParent(parent)
        self.setObjectName("Schedule")
        # QAnimationComboBox
        self.ui.setStyleSheet("""
QFrame#Schedule {
    background-color: #fff;
}

        """)
