import os
import core
from PySide2.QtWidgets import QWidget, QListView, QAbstractItemView
from PySide2.QtCore import Qt
from PySide2.QtUiTools import loadUiType, QUiLoader



class messageWidget(QWidget):

    def __init__(self, parent=None, *args, **kwargs) -> None:

        super(messageWidget, self).__init__(parent, *args, **kwargs)
        uiLoader = QUiLoader()
        __uiFilePath = os.path.join(core.PATH_VIEWS, "message", "message.ui")
        ui = uiLoader.load(__uiFilePath)
        self.ui = ui
        self.ui.setParent(parent)
        self.setObjectName("Message")
        

        self.listView.setAutoFillBackground(True)
        self.listView.setFlow(QListView.LeftToRight)
        self.listView.setViewMode(QListView.IconMode)
        self.listView.setResizeMode(QListView.Adjust)
        self.listView.setLayoutMode(QListView.SinglePass)
        self.listView.setWrapping(True)
        self.listView.setMovement(QListView.Static)
        self.listView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listView.setSpacing(2)

    @property
    def listView(self) -> QListView:
        return self.ui.listView