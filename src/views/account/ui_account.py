# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_L_Header1(object):
    def setupUi(self, L_Header1):
        if not L_Header1.objectName():
            L_Header1.setObjectName(u"L_Header1")
        L_Header1.resize(710, 240)
        L_Header1.setFrameShape(QFrame.StyledPanel)
        L_Header1.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(L_Header1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.L_qss = QLabel(L_Header1)
        self.L_qss.setObjectName(u"L_qss")

        self.gridLayout.addWidget(self.L_qss, 0, 0, 1, 1)

        self.checkBox = QCheckBox(L_Header1)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.PB_qss = QPushButton(L_Header1)
        self.PB_qss.setObjectName(u"PB_qss")

        self.gridLayout.addWidget(self.PB_qss, 2, 0, 1, 1)


        self.retranslateUi(L_Header1)

        QMetaObject.connectSlotsByName(L_Header1)
    # setupUi

    def retranslateUi(self, L_Header1):
        L_Header1.setWindowTitle(QCoreApplication.translate("L_Header1", u"Frame", None))
        self.L_qss.setText(QCoreApplication.translate("L_Header1", u"Acount", None))
        self.checkBox.setText(QCoreApplication.translate("L_Header1", u"CheckBox", None))
        self.PB_qss.setText(QCoreApplication.translate("L_Header1", u"Check", None))
    # retranslateUi

