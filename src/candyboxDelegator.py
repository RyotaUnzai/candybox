# -*- coding: utf-8 -*-
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
        self.nav = self.__view.cw.navigation
        self.nav = self.__view.cw.navigation.ui
        self.body = self.__view.cw.body

    @property
    def model(self) -> candyboxModel:
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    def connect(self):
        self.view.show()
        self.__navigationConnection()

    def __navigationConnection(self):
        # self.nav.setMaximumWidth(100)
        self.nav.PB_Home.clicked.connect(self.view.close)

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

        self.nav.PB_Message.clicked.connect(
            lambda: self.model.showHideWidget(view=self.view, widgetType="homeWidget", bodyWidget=self.body)
        )
