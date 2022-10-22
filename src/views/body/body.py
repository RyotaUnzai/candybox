
from PySide2.QtWidgets import QWidget, QPushButton, QHBoxLayout

from ..account import *
from ..home import *
from ..message import *
from ..schedule import *
from ..setting import *


class bodyWidget(QWidget):
    layout = QHBoxLayout()

    def __init__(self, parent=None, *args, **kwargs) -> None:
        super(bodyWidget, self).__init__(parent, *args, **kwargs)

        #self.test = QPushButton("QOQKQKQKQKKQKQ", self)
        # self.setObjectName("body")
        self.home = homeWidget(self)

        # self.layout.addWidget(home)
        self.setLayout(self.layout)
