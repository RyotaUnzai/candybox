from PySide2 import QtWidgets, QtGui

import candyboxView
import candyboxModel
import core
import delegator


class candyBoxDelegator(core.delegator):
    view: candyboxView.candyBoxMainWindow
    model: candyboxModel
    fontRemix: core.fontRemixicon.Remixcon
    fontRaleway: core.fontRaleway.Raleway
    nav: candyboxView.views.navigationWidget
    body: candyboxView.views.bodyWidget

    def __init__(self, view=None, model=None, *args, **kwargs):
        super(candyBoxDelegator, self).__init__(view, model, *args, **kwargs)
        self.fontRemix = core.fontRemixicon.Remixcon()
        self.fontRaleway = core.fontRaleway.Raleway()

    def connect(self) -> None:
        self.view.show()
        self.createClassVariables()
        self.__bodyWidgetConnection()
        self.__navigationConnection()
        self.__settingWidgetConnection()
        self.__messageWidgetConnection()

    def createClassVariables(self) -> None:
        self.nav = self.view.cw.navigation.ui
        self.bodyWidget = self.view.cw.bodyWidget
        self.bodyWidgetLayout = self.view.cw.bodyWidget.layout()
        self.settingWidget = self.view.cw.settingWidget
        self.messageWidget = self.view.cw.messageWidget

    def __messageWidgetConnection(self) -> None:
        iconList = self.model.getExtList(core.PATH_DATA)
        iconDataList = []
        for url in iconList:
            iconData = self.model.loadJson(url)
            iconData["filePath"] = url
            iconDataList.append(iconData)
        self.iconListModel = self.model.iconListModel(data=iconDataList)
        self.messageWidget.listView.setModel(self.iconListModel)
        self.messageWidget.listView.setItemDelegate(delegator.iconListDelegate(self.messageWidget.listView))

    def __settingWidgetConnection(self) -> None:
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
        self.settingWidget.TreeView_Setting.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.settingWidget.TreeView_Setting.setSelectionModel(self.settingWidget.TableView_Setting.selectionModel())

    def __bodyWidgetConnection(self) -> None:

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

    def __navigationConnection(self) -> None:

        # self.nav.setMaximumWidth(100)
        # self.nav.PB_Home.clicked.connect(self.view.close)

        self.fontRemix.Font_Remixicon.setPixelSize(20)
        self.nav.PB_Home.setFont(self.fontRemix.Font_Remixicon)
        self.nav.PB_Message.setFont(self.fontRemix.Font_Remixicon)
        self.nav.PB_Schedule.setFont(self.fontRemix.Font_Remixicon)
        self.nav.PB_Setting.setFont(self.fontRemix.Font_Remixicon)
        self.nav.PB_Account.setFont(self.fontRemix.Font_Remixicon)

        self.nav.PB_Home.setText(self.fontRemix.ri_home_2_fill)
        self.nav.PB_Message.setText(self.fontRemix.ri_message_2_fill)
        self.nav.PB_Schedule.setText(self.fontRemix.ri_calendar_2_fill)
        self.nav.PB_Setting.setText(self.fontRemix.ri_settings_2_fill)
        self.nav.PB_Account.setText(self.fontRemix.ri_account_box_fill)

        self.fontRemix.Font_Remixicon.setPixelSize(36)
        self.nav.L_Appicon.setFont(self.fontRemix.Font_Remixicon)
        self.nav.L_Appicon.setText(self.fontRemix.ri_apps_fill)
