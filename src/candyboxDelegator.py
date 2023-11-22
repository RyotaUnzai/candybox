from PySide2 import QtWidgets, QtCore
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

    def __init__(self: Self, view: CandyBoxMainWindow, model: CandyBoxModels, *args, **kwargs) -> Self:
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
        self.model.iconListModel = IconListModel(items=iconDataList)
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

        for num, pushButton in self.view.navigation.pushButtons:
            pushButtonName: str = pushButton.objectName()
            widgetType: str = pushButtonName[10:]
            eval(
                f"""
self.view.navigation.{pushButtonName}.clicked.connect(
    lambda widType="{widgetType}", boxLayout=self.view.boxLayout: self.model.bodyItemModel.showHideWidget(
        widgetType="{widgetType}", layout=boxLayout
    )
)""",
                {"self": self}
            )

    def __navigationConnection(self: Self) -> None:
        self.fontRemixicon.setPixelSize(20)
        self.view.navigation.setFont(self.fontRemixicon)
        textData = {
            0: self.fontRemixicon.ri_account_box_fill,
            1: self.fontRemixicon.ri_home_2_fill,
            2: self.fontRemixicon.ri_message_2_fill,
            3: self.fontRemixicon.ri_calendar_2_fill,
            4: self.fontRemixicon.ri_settings_2_fill
        }
        self.view.navigation.setText(textData)
        self.view.navigation.setIconText(
            self.fontRemixicon, iconText=self.fontRemixicon.ri_apps_fill, iconSize=36
        )
