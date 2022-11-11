import os
import core
from PySide2.QtWidgets import QWidget, QPushButton

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

        for i in range(30):
            btn = QPushButton("%s" % i)
            self.FlowLayout.addWidget(btn)

        self.FlowLayout.space = (50, 10)

    @property
    def Cb_qss(self):
        return self.ui.Cb_qss

    @property
    def FlowLayout(self) -> QtCustom.QFlowLayout:
        return self.ui.QFlowLayout_FlowLayout
