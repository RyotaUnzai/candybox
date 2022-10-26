# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(650, 578)
        Setting.setFrameShape(QFrame.StyledPanel)
        Setting.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(Setting)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TreeView_Setting = QTreeView(Setting)
        self.TreeView_Setting.setObjectName(u"TreeView_Setting")

        self.gridLayout.addWidget(self.TreeView_Setting, 2, 0, 1, 1)

        self.L_Header1 = QLabel(Setting)
        self.L_Header1.setObjectName(u"L_Header1")

        self.gridLayout.addWidget(self.L_Header1, 0, 0, 1, 1)

        self.TableView_Setting = QTableView(Setting)
        self.TableView_Setting.setObjectName(u"TableView_Setting")

        self.gridLayout.addWidget(self.TableView_Setting, 2, 1, 1, 1)

        self.lineEdit = QLineEdit(Setting)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)


        self.retranslateUi(Setting)

        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"Frame", None))
        self.L_Header1.setText(QCoreApplication.translate("Setting", u"Setting", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Setting", u"search", None))
    # retranslateUi

