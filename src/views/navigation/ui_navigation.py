# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'navigation.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Navigation(object):
    def setupUi(self, Navigation):
        if not Navigation.objectName():
            Navigation.setObjectName(u"Navigation")
        Navigation.resize(460, 521)
        Navigation.setFrameShape(QFrame.StyledPanel)
        Navigation.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(Navigation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.VBL_Bottom = QVBoxLayout()
        self.VBL_Bottom.setObjectName(u"VBL_Bottom")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.VBL_Bottom.addItem(self.verticalSpacer)

        self.PB_Account = QPushButton(Navigation)
        self.PB_Account.setObjectName(u"PB_Account")
        self.PB_Account.setMinimumSize(QSize(60, 60))
        self.PB_Account.setMaximumSize(QSize(60, 60))
        self.PB_Account.setCheckable(True)

        self.VBL_Bottom.addWidget(self.PB_Account)


        self.gridLayout.addLayout(self.VBL_Bottom, 1, 0, 1, 1)

        self.VBL_Top = QVBoxLayout()
        self.VBL_Top.setObjectName(u"VBL_Top")
        self.L_Appicon = QLabel(Navigation)
        self.L_Appicon.setObjectName(u"L_Appicon")
        self.L_Appicon.setMinimumSize(QSize(60, 60))
        self.L_Appicon.setMaximumSize(QSize(60, 60))
        self.L_Appicon.setLayoutDirection(Qt.LeftToRight)
        self.L_Appicon.setAlignment(Qt.AlignCenter)

        self.VBL_Top.addWidget(self.L_Appicon)

        self.PB_Home = QPushButton(Navigation)
        self.PB_Home.setObjectName(u"PB_Home")
        self.PB_Home.setMinimumSize(QSize(60, 60))
        self.PB_Home.setMaximumSize(QSize(60, 60))
        self.PB_Home.setCheckable(True)
        self.PB_Home.setChecked(True)

        self.VBL_Top.addWidget(self.PB_Home)

        self.PB_Message = QPushButton(Navigation)
        self.PB_Message.setObjectName(u"PB_Message")
        self.PB_Message.setMinimumSize(QSize(60, 60))
        self.PB_Message.setMaximumSize(QSize(60, 60))
        self.PB_Message.setCheckable(True)

        self.VBL_Top.addWidget(self.PB_Message)

        self.PB_Schedule = QPushButton(Navigation)
        self.PB_Schedule.setObjectName(u"PB_Schedule")
        self.PB_Schedule.setMinimumSize(QSize(60, 60))
        self.PB_Schedule.setMaximumSize(QSize(60, 60))
        self.PB_Schedule.setCheckable(True)

        self.VBL_Top.addWidget(self.PB_Schedule)

        self.PB_Setting = QPushButton(Navigation)
        self.PB_Setting.setObjectName(u"PB_Setting")
        self.PB_Setting.setMinimumSize(QSize(60, 60))
        self.PB_Setting.setMaximumSize(QSize(60, 60))
        self.PB_Setting.setCheckable(True)

        self.VBL_Top.addWidget(self.PB_Setting)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.VBL_Top.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.VBL_Top, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.retranslateUi(Navigation)

        QMetaObject.connectSlotsByName(Navigation)
    # setupUi

    def retranslateUi(self, Navigation):
        Navigation.setWindowTitle(QCoreApplication.translate("Navigation", u"Frame", None))
        self.PB_Account.setText(QCoreApplication.translate("Navigation", u"Account", None))
        self.L_Appicon.setText(QCoreApplication.translate("Navigation", u"AppIcon", None))
        self.PB_Home.setText(QCoreApplication.translate("Navigation", u"Home", None))
        self.PB_Message.setText(QCoreApplication.translate("Navigation", u"Message", None))
        self.PB_Schedule.setText(QCoreApplication.translate("Navigation", u"Schedule", None))
        self.PB_Setting.setText(QCoreApplication.translate("Navigation", u"Setting", None))
    # retranslateUi

