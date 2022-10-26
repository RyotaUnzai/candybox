# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(479, 208)
        Home.setFrameShape(QFrame.StyledPanel)
        Home.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(Home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.PB_qss_02 = QPushButton(Home)
        self.PB_qss_02.setObjectName(u"PB_qss_02")
        self.PB_qss_02.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.PB_qss_02, 1, 2, 1, 1)

        self.spinBox = QSpinBox(Home)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 2, 2, 1, 1)

        self.Cb_qss = QComboBox(Home)
        self.Cb_qss.setObjectName(u"Cb_qss")

        self.gridLayout.addWidget(self.Cb_qss, 1, 0, 1, 1)

        self.SB_qss = QSpinBox(Home)
        self.SB_qss.setObjectName(u"SB_qss")

        self.gridLayout.addWidget(self.SB_qss, 2, 1, 1, 1)

        self.L_Header1 = QLabel(Home)
        self.L_Header1.setObjectName(u"L_Header1")

        self.gridLayout.addWidget(self.L_Header1, 0, 0, 1, 1)

        self.PB_qss_01 = QPushButton(Home)
        self.PB_qss_01.setObjectName(u"PB_qss_01")
        self.PB_qss_01.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.PB_qss_01, 1, 1, 1, 1)

        self.LW_qss = QListWidget(Home)
        QListWidgetItem(self.LW_qss)
        QListWidgetItem(self.LW_qss)
        QListWidgetItem(self.LW_qss)
        QListWidgetItem(self.LW_qss)
        QListWidgetItem(self.LW_qss)
        self.LW_qss.setObjectName(u"LW_qss")

        self.gridLayout.addWidget(self.LW_qss, 3, 0, 1, 3)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Frame", None))
        self.PB_qss_02.setText(QCoreApplication.translate("Home", u"PushButton", None))
        self.L_Header1.setText(QCoreApplication.translate("Home", u"Home", None))
        self.PB_qss_01.setText(QCoreApplication.translate("Home", u"PushButton", None))

        __sortingEnabled = self.LW_qss.isSortingEnabled()
        self.LW_qss.setSortingEnabled(False)
        ___qlistwidgetitem = self.LW_qss.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Home", u"DateA", None));
        ___qlistwidgetitem1 = self.LW_qss.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Home", u"DateB", None));
        ___qlistwidgetitem2 = self.LW_qss.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Home", u"DateC", None));
        ___qlistwidgetitem3 = self.LW_qss.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Home", u"DateD", None));
        ___qlistwidgetitem4 = self.LW_qss.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Home", u"DateE", None));
        self.LW_qss.setSortingEnabled(__sortingEnabled)

    # retranslateUi

