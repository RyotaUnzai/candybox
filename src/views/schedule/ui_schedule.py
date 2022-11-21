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

from QAnimationComboBox import QAnimationComboBox
from QIntSlider import QIntSlider
from QFloatSlider import QFloatSlider
from QAbstractProgressCircular import QAbstractProgressCircular
from QCircularSlider import QCircularSlider


class Ui_Schedule(object):
    def setupUi(self, Schedule):
        if not Schedule.objectName():
            Schedule.setObjectName(u"Schedule")
        Schedule.resize(696, 484)
        Schedule.setFrameShape(QFrame.StyledPanel)
        Schedule.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(Schedule)
        self.gridLayout.setObjectName(u"gridLayout")
        self.IntSlider = QIntSlider(Schedule)
        self.IntSlider.setObjectName(u"IntSlider")
        self.IntSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.IntSlider, 3, 0, 1, 1)

        self.dial = QDial(Schedule)
        self.dial.setObjectName(u"dial")

        self.gridLayout.addWidget(self.dial, 1, 1, 1, 1)

        self.Cb_qss = QAnimationComboBox(Schedule)
        self.Cb_qss.setObjectName(u"Cb_qss")

        self.gridLayout.addWidget(self.Cb_qss, 1, 0, 1, 1)

        self.L_Header1 = QLabel(Schedule)
        self.L_Header1.setObjectName(u"L_Header1")

        self.gridLayout.addWidget(self.L_Header1, 0, 0, 1, 1)

        self.FloatSlider = QFloatSlider(Schedule)
        self.FloatSlider.setObjectName(u"FloatSlider")
        self.FloatSlider.setMaximum(100)
        self.FloatSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.FloatSlider, 2, 0, 1, 1)

        self.QFlowLayout_FlowLayout = QVBoxLayout()
        self.QFlowLayout_FlowLayout.setObjectName(u"QFlowLayout_FlowLayout")

        self.gridLayout.addLayout(self.QFlowLayout_FlowLayout, 9, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AbstractProgressCircular = QAbstractProgressCircular(Schedule)
        self.AbstractProgressCircular.setObjectName(u"AbstractProgressCircular")
        self.AbstractProgressCircular.setValue(24)

        self.horizontalLayout.addWidget(self.AbstractProgressCircular)

        self.APC_PushButton = QPushButton(Schedule)
        self.APC_PushButton.setObjectName(u"APC_PushButton")

        self.horizontalLayout.addWidget(self.APC_PushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.CircularSliderA = QCircularSlider(Schedule)
        self.CircularSliderA.setObjectName(u"CircularSliderA")
        self.CircularSliderA.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.CircularSliderA)

        self.CircularSliderB = QCircularSlider(Schedule)
        self.CircularSliderB.setObjectName(u"CircularSliderB")
        self.CircularSliderB.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.CircularSliderB)

        self.CircularSliderC = QCircularSlider(Schedule)
        self.CircularSliderC.setObjectName(u"CircularSliderC")
        self.CircularSliderC.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.CircularSliderC)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.AbstractProgressCircularB = QAbstractProgressCircular(Schedule)
        self.AbstractProgressCircularB.setObjectName(u"AbstractProgressCircularB")
        self.AbstractProgressCircularB.setValue(24)

        self.gridLayout.addWidget(self.AbstractProgressCircularB, 7, 0, 1, 1)


        self.retranslateUi(Schedule)

        QMetaObject.connectSlotsByName(Schedule)
    # setupUi

    def retranslateUi(self, Schedule):
        Schedule.setWindowTitle(QCoreApplication.translate("Schedule", u"Frame", None))
        self.L_Header1.setText(QCoreApplication.translate("Schedule", u"Schedule", None))
        self.APC_PushButton.setText(QCoreApplication.translate("Schedule", u"Progress Start", None))
    # retranslateUi

