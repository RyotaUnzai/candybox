from PySide2 import QtWidgets

import candyboxModel
import candyboxView
import core
import delegator


class candyBoxDelegator(core.Delegator):
    view: candyboxView.candyBoxMainWindow
    model: candyboxModel
    fontRemicon: core.fontRemixicon.Remixicon
    fontRalewayExtraBoldItalic: core.fontRaleway.RalewayExtraBoldItalic
    nav: candyboxView.views.navigationWidget
    body: QtWidgets.QWidget

    def __init__(self, view=None, model=None, *args, **kwargs):
        super(candyBoxDelegator, self).__init__(view, model, *args, **kwargs)
        #self.fontRemix = core.fontRemixicon.Remixicon()
        self.fontRemicon = core.fontRemixicon.Remixicon()
        self.fontRalewayExtraBoldItalic = core.fontRaleway.RalewayExtraBoldItalic()

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
        self.settingWidget = self.view.cw.setting
        self.messageWidget = self.view.cw.message

    def __messageWidgetConnection(self) -> None:
        iconList = core.getExtList(core.PATH_DATA)
        iconDataList = []
        for url in iconList:
            iconData = core.loadJson(url)
            iconData["filePath"] = url
            iconModel = candyboxModel.IconModel(**iconData)
            iconDataList.append(iconModel)
        self.iconListModel = self.model.IconListModel(data=iconDataList)
        self.messageWidget.listView.setModel(self.iconListModel)
        self.messageWidget.listView.setItemDelegate(delegator.iconListDelegate(self.messageWidget.listView))

    def __settingWidgetConnection(self) -> None:
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

        self.settingModel = self.model.settingTreeModel.SettingTreeModel(data)
        self.settingWidget.treeView.setModel(self.settingModel)
        self.settingWidget.tableView.setModel(self.settingModel)
        self.settingWidget.treeView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.settingWidget.treeView.setSelectionModel(self.settingWidget.tableView.selectionModel())

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

        #self.fontRemix.Font_Remixicon.setPixelSize(20)
        self.fontRemicon.setPixelSize(20)
        self.nav.PB_Home.setFont(self.fontRemicon)
        self.nav.PB_Message.setFont(self.fontRemicon)
        self.nav.PB_Schedule.setFont(self.fontRemicon)
        self.nav.PB_Setting.setFont(self.fontRemicon)
        self.nav.PB_Account.setFont(self.fontRemicon)

        self.nav.PB_Home.setText(self.fontRemicon.ri_home_2_fill)
        self.nav.PB_Message.setText(self.fontRemicon.ri_message_2_fill)
        self.nav.PB_Schedule.setText(self.fontRemicon.ri_calendar_2_fill)
        self.nav.PB_Setting.setText(self.fontRemicon.ri_settings_2_fill)
        self.nav.PB_Account.setText(self.fontRemicon.ri_account_box_fill)

        self.fontRemicon.setPixelSize(36)
        self.nav.L_Appicon.setFont(self.fontRemicon)
        self.nav.L_Appicon.setText(self.fontRemicon.ri_apps_fill)
