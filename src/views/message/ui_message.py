# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'message.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Message(object):
    def setupUi(self, Message):
        if not Message.objectName():
            Message.setObjectName(u"Message")
        Message.resize(622, 268)
        Message.setFrameShape(QFrame.StyledPanel)
        Message.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(Message)
        self.gridLayout.setObjectName(u"gridLayout")
        self.PBar_qss = QProgressBar(Message)
        self.PBar_qss.setObjectName(u"PBar_qss")
        self.PBar_qss.setMaximum(0)
        self.PBar_qss.setValue(0)
        self.PBar_qss.setTextVisible(False)
        self.PBar_qss.setInvertedAppearance(False)

        self.gridLayout.addWidget(self.PBar_qss, 1, 1, 1, 1)

        self.L_Header1 = QLabel(Message)
        self.L_Header1.setObjectName(u"L_Header1")

        self.gridLayout.addWidget(self.L_Header1, 0, 0, 1, 1)

        self.checkBox = QCheckBox(Message)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.radioButton = QRadioButton(Message)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 1)

        self.radioButton_2 = QRadioButton(Message)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 3, 0, 1, 1)


        self.retranslateUi(Message)

        QMetaObject.connectSlotsByName(Message)
    # setupUi

    def retranslateUi(self, Message):
        Message.setWindowTitle(QCoreApplication.translate("Message", u"Frame", None))
        self.L_Header1.setText(QCoreApplication.translate("Message", u"Message", None))
        self.checkBox.setText(QCoreApplication.translate("Message", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("Message", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("Message", u"RadioButton", None))
    # retranslateUi

