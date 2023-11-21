from PySide2 import QtWidgets
from typing import TypeVar

import core
from core.fontRaleway import RalewayExtraBoldItalic
from core.fontRemixicon import Remixicon


from candyboxModel import (
    CandyBoxModels,
    IconModel,
    IconListModel
)
from candyboxView import CandyBoxMainWindow

import views
import delegator


class CandyBoxDelegator(core.Delegator):
    Self = TypeVar("Self", bound="CandyBoxDelegator")
    fontRemixicon: Remixicon
    fontRalewayExtraBoldItalic: RalewayExtraBoldItalic
    view: CandyBoxMainWindow
    model: CandyBoxModels
    nav: views.NavigationWidget
    body: QtWidgets.QWidget

    def __init__(self: Self,view: CandyBoxMainWindow, model: CandyBoxModels, *args, **kwargs) -> Self:
        super().__init__(view, model, *args, **kwargs)
        self.fontRemixicon = Remixicon()
        self.fontRalewayExtraBoldItalic = RalewayExtraBoldItalic()

    def connect(self: Self) -> None:
        self.view.show()
        self.__bodyWidgetConnection()
        self.__navigationConnection()
        self.__settingWidgetConnection()
        self.__messageWidgetConnection()

    def __messageWidgetConnection(self: Self) -> None:
        iconList = core.getExtList(core.PATH_DATA)
        iconDataList = []
        for url in iconList:
            iconData = core.loadJson(url)
            iconData["filePath"] = url
            iconModel = IconModel(**iconData)
            iconDataList.append(iconModel)
        self.model.iconListModel = IconListModel(data=iconDataList)
        self.view.message.listView.setModel(self.model.iconListModel)
        self.view.message.listView.setItemDelegate(delegator.iconListDelegate(self.view.message.listView))

    def __settingWidgetConnection(self: Self) -> None:
        data = [
            {'parent': 'python', 'key': 'flake8Args'},
            {'parent': 'python', 'key': 'provider'},
            {'parent': 'python', 'key': 'autopep8Args'},
            {'parent': 'python', 'key': 'renderControlCharacters'},
            {'parent': 'python', 'key': 'formatOnSave'},
            {'parent': 'colorInfo', 'key': 'home'},
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
        self.model.setSettingTreeModel(data)
        self.view.preference.treeView.setModel(self.model.settingTreeModel)
        self.view.preference.tableView.setModel(self.model.settingTreeModel)
        self.view.preference.treeView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.view.preference.treeView.setSelectionModel(self.view.preference.tableView.selectionModel())

    def __bodyWidgetConnection(self: Self) -> None:
        self.model.bodyItemModel.setBodyWidgetItems(self.view.body.layout())

        for pushButton in self.view.navigation.pushButtons:
            pushButtonName: str = pushButton.objectName()
            widgetType: str = pushButtonName[10:]
            exec(f"""self.view.navigation.{pushButtonName}.clicked.connect(
    lambda:  self.model.bodyItemModel.showHideWidget(widgetType="{widgetType}", layout=self.view.boxLayout)
)"""               )

    def __navigationConnection(self: Self) -> None:

        # self.view.navigation.setMaximumWidth(100)
        # self.view.navigation.PB_Home.clicked.connect(self.view.close)

        # self.fontRemix.Font_Remixicon.setPixelSize(20)
        self.fontRemixicon.setPixelSize(20)
        self.view.navigation.pushButtonAccount.setFont(self.fontRemixicon)
        self.view.navigation.pushButtonHome.setFont(self.fontRemixicon)
        self.view.navigation.pushButtonMessage.setFont(self.fontRemixicon)
        self.view.navigation.pushButtonSchedule.setFont(self.fontRemixicon)
        self.view.navigation.pushButtonPreference.setFont(self.fontRemixicon)

        self.view.navigation.pushButtonAccount.setText(self.fontRemixicon.ri_account_box_fill)
        self.view.navigation.pushButtonHome.setText(self.fontRemixicon.ri_home_2_fill)
        self.view.navigation.pushButtonMessage.setText(self.fontRemixicon.ri_message_2_fill)
        self.view.navigation.pushButtonSchedule.setText(self.fontRemixicon.ri_calendar_2_fill)
        self.view.navigation.pushButtonPreference.setText(self.fontRemixicon.ri_settings_2_fill)

        self.fontRemixicon.setPixelSize(36)
        self.view.navigation.labelAppIcon.setFont(self.fontRemixicon)
        self.view.navigation.labelAppIcon.setText(self.fontRemixicon.ri_apps_fill)
