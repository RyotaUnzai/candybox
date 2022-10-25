# -*- coding: utf-8 -*-
from re import L
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import candyboxView
import candyboxModel
import core


class candyBoxDelegator(core.delegator):
    __view = None
    __model = None
    __nav = None
    __body = None

    def __init__(self, view=None, model=None, *args, **kwargs):
        super(candyBoxDelegator, self).__init__(view, model, *args, **kwargs)

        self.FontRemix = core.fontRemixicon.Remixcon()
        self.FontRaleway = core.fontRaleway.Raleway()

    @property
    def nav(self) -> candyboxView.views.navigationWidget:
        return self.__nav

    @nav.setter
    def nav(self, value):
        self.__nav = value

    @property
    def body(self) -> candyboxView.views.bodyWidget:
        return self.__body

    @body.setter
    def body(self, value):
        self.__body = value

    @property
    def view(self) -> candyboxView.candyBoxMainWindow:
        return self.__view

    @view.setter
    def view(self, value):
        self.__view = value

    @property
    def model(self) -> candyboxModel:
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    def connect(self):
        self.view.show()
        self.createClassVariables()
        self.__bodyWidgetConnection()
        self.__navigationConnection()
        self.__settingWidgetConnection()

    def createClassVariables(self):
        self.nav = self.view.cw.navigation.ui
        self.bodyWidget = self.view.cw.bodyWidget
        self.bodyWidgetLayout = self.view.cw.bodyWidget.layout()
        self.settingWidget = self.view.cw.settingWidget

    def __settingWidgetConnection(self):
        data = [
            {'parent': 'python', 'key': 'flake8Args'},
            {'parent': 'python', 'key': 'provider'},
            {'parent': 'python', 'key': 'autopep8Args'},
            {'parent': 'python', 'key': 'renderControlCharacters'},
            {'parent': 'python', 'key': 'formatOnSave'},
            {'parent': 'colorInfo', 'key': 'homeUI'},
            {'parent': 'colorInfo', 'key': 'fields'},
            {'parent': 'colorInfo', 'key': 'formatOnSave'},
            {'parent': 'colorInfo', 'key': 'renderControlCharacters'},
            {'parent': 'colorInfo', 'key': 'associations'},
            {'parent': 'svn', 'key': 'svn'},
            {'parent': 'svn', 'key': 'fields'},
            {'parent': 'svn', 'key': 'formatOnSave'},
            {'parent': 'svn', 'key': 'renderControlCharacters'},
            {'parent': 'svn', 'key': 'associations'},
            {'parent': 'svn', 'key': 'd'}
        ]

        self.settingModel = self.model.settingTreeModel.SettingTreeModel(data)
        self.settingWidget.TreeView_Setting.setModel(self.settingModel)
        self.settingWidget.TableView_Setting.setModel(self.settingModel)
        self.settingWidget.TreeView_Setting.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.settingWidget.TreeView_Setting.setSelectionModel(self.settingWidget.TableView_Setting.selectionModel())

    def __bodyWidgetConnection(self):

        self.bodyItemModel = self.model.candyBoxBodyItemModel()
        self.bodyItemModel.setBodyWidgetItems(self.bodyWidgetLayout)

        self.nav.PB_Home.clicked.connect(
            lambda: self.bodyItemModel.showHideWidget(widgetType="Home", layout=self.bodyWidgetLayout)
        )
        self.nav.PB_Message.clicked.connect(
            lambda: self.bodyItemModel.showHideWidget(widgetType="Message", layout=self.bodyWidgetLayout)
        )
        self.nav.PB_Schedule.clicked.connect(
            lambda: self.bodyItemModel.showHideWidget(widgetType="Schedule", layout=self.bodyWidgetLayout)
        )
        self.nav.PB_Setting.clicked.connect(
            lambda: self.bodyItemModel.showHideWidget(widgetType="Setting", layout=self.bodyWidgetLayout)
        )
        self.nav.PB_Account.clicked.connect(
            lambda: self.bodyItemModel.showHideWidget(widgetType="Account", layout=self.bodyWidgetLayout)
        )

    def __navigationConnection(self):

        # self.nav.setMaximumWidth(100)
        # self.nav.PB_Home.clicked.connect(self.view.close)

        self.FontRemix.Font_Remixicon.setPixelSize(20)
        self.nav.PB_Home.setFont(self.FontRemix.Font_Remixicon)
        self.nav.PB_Message.setFont(self.FontRemix.Font_Remixicon)
        self.nav.PB_Schedule.setFont(self.FontRemix.Font_Remixicon)
        self.nav.PB_Setting.setFont(self.FontRemix.Font_Remixicon)
        self.nav.PB_Account.setFont(self.FontRemix.Font_Remixicon)

        self.nav.PB_Home.setText(self.FontRemix.ri_home_2_fill)
        self.nav.PB_Message.setText(self.FontRemix.ri_message_2_fill)
        self.nav.PB_Schedule.setText(self.FontRemix.ri_calendar_2_fill)
        self.nav.PB_Setting.setText(self.FontRemix.ri_settings_2_fill)
        self.nav.PB_Account.setText(self.FontRemix.ri_account_box_fill)

        self.FontRemix.Font_Remixicon.setPixelSize(36)
        self.nav.L_Appicon.setFont(self.FontRemix.Font_Remixicon)
        self.nav.L_Appicon.setText(self.FontRemix.ri_apps_fill)
