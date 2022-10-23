import os
import core
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtUiTools import QUiLoader

import QtCustom


class homeWidget(QWidget):

    def __init__(self, parent=None, *args, **kwargs) -> None:

        super(homeWidget, self).__init__(parent, *args, **kwargs)
        uiLoader = QUiLoader()
        __uiFilePath = os.path.join(core.PATH_VIEWS, "home", "home.ui")
        ui = uiLoader.load(__uiFilePath)
        self.ui = ui
        self.ui.setParent(parent)
        self.setObjectName("Home")
        self.createQAnimationComboBox()
        self.changeWidget()
        # self.ui.Cb_qss.deleteLater()

    def createQAnimationComboBox(self):
        self.ComboBox = QtCustom.QAnimationComboBox(self.ui)
        self.ComboBox_ListView = QListView(self.ui)
        self.ComboBox_ListView.setObjectName("Cb_qss")
        self.ComboBox_ListView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ComboBox.setView(self.ComboBox_ListView)
        self.ComboBox_LineEdit = QLineEdit(self.ui)
        self.ComboBox_LineEdit.setObjectName("Cb_qss")
        self.ComboBox_LineEdit.setReadOnly(True)
        self.ComboBox.setLineEdit(self.ComboBox_LineEdit)
        self.ComboBox.setObjectName("Cb_qss")
        self.ComboBox.PopupOffcet = (0, 10)
        self.ComboBox.fade = True
        self.ComboBox.slide = False
        self.ComboBox.stretch = True
        for i in range(5):
            self.ComboBox.addItem("Item %s" % i)

    def changeWidget(self):
        for num in range(self.ui.gridLayout.count()):
            item = self.ui.gridLayout.itemAt(num)
            try:
                widget = item.widget()
                objectName = widget.objectName()
                if objectName == "Cb_qss":
                    pos = self.ui.gridLayout.getItemPosition(num)
            except BaseException:
                pass

        self.ui.Cb_qss.deleteLater()
        self.ui.Cb_qss = self.ComboBox
        self.ui.gridLayout.addWidget(
            self.ui.Cb_qss, pos[0], pos[1], pos[2], pos[3]
        )
