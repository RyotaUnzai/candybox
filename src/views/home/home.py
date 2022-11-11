import os
import core
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *


import QtCustom


class homeWidget(QWidget):

    def __init__(self, parent=None, *args, **kwargs) -> None:

        super(homeWidget, self).__init__(parent, *args, **kwargs)
        uiLoader = QtCustom.QExUiLoader()
        __uiFilePath = os.path.join(core.PATH_VIEWS, "home", "home.ui")
        ui = uiLoader.load(__uiFilePath)
        self.ui = ui
        self.ui.setParent(parent)
        self.setObjectName("Home")

        self.ComboBox_ListView = QListView(self.ui)
        self.ComboBox_ListView.setObjectName("Cb_qss")
        self.ComboBox_ListView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ComboBox_LineEdit = QLineEdit(self.ui)
        self.ComboBox_LineEdit.setObjectName("Cb_qss")
        self.ComboBox_LineEdit.setReadOnly(True)

        self.Cb_qss.setView(self.ComboBox_ListView)
        self.Cb_qss.setLineEdit(self.ComboBox_LineEdit)
        self.Cb_qss.PopupOffcet = (0, 10)
        self.Cb_qss.fade = True
        self.Cb_qss.slide = False
        self.Cb_qss.stretch = True
        for i in range(5):
            self.Cb_qss.addItem("Item %s" % i)

    @property
    def Cb_qss(self):
        return self.ui.Cb_qss
