# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'schedule.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Schedule(object):
    def setupUi(self, Schedule):
        if not Schedule.objectName():
            Schedule.setObjectName(u"Schedule")
        Schedule.resize(257, 164)
        Schedule.setFrameShape(QFrame.StyledPanel)
        Schedule.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(Schedule)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Cb_qss = QComboBox(Schedule)
        self.Cb_qss.setObjectName(u"Cb_qss")

        self.gridLayout.addWidget(self.Cb_qss, 1, 0, 1, 1)

        self.L_Header1 = QLabel(Schedule)
        self.L_Header1.setObjectName(u"L_Header1")

        self.gridLayout.addWidget(self.L_Header1, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.dial = QDial(Schedule)
        self.dial.setObjectName(u"dial")

        self.gridLayout.addWidget(self.dial, 1, 1, 1, 1)


        self.retranslateUi(Schedule)

        QMetaObject.connectSlotsByName(Schedule)
    # setupUi

    def retranslateUi(self, Schedule):
        Schedule.setWindowTitle(QCoreApplication.translate("Schedule", u"Frame", None))
        self.L_Header1.setText(QCoreApplication.translate("Schedule", u"Schedule", None))
    # retranslateUi

