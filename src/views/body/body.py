
from PySide2.QtWidgets import *

try:
    from ..account import *
    from ..home import *
    from ..message import *
    from ..schedule import *
    from ..setting import *
except BaseException:
    import sys
    sys.path.append("./")
    sys.path.append("../account")
    sys.path.append("../home")
    sys.path.append("../message")
    sys.path.append("../schedule")
    sys.path.append("../setting")
    from PySide2.QtGui import *
    from src.views.account import *
    from src.views.home import *
    from src.views.message import *
    from src.views.schedule import *
    from src.views.setting import *


class bodyWidget(QFrame):
    def __init__(self, parent=None, *args, **kwargs) -> None:
        super(bodyWidget, self).__init__(parent, *args, **kwargs)

        # self.setObjectName("body")
        #self.Hbox = QGridLayout(self)

        #self.home = homeWidget(self)
        #self.message = messageWidget(self)
        #self.schedule = scheduleWidget(self)
        # self.setting = settingWidget(self)
        # self.account = accountWidget(self)

        #self.homeUI = self.home.ui
        #self.messageUI = self.message.ui
        #self.scheduleUI = self.schedule
        # self.settingUI = self.setting.ui
        # self.accountUI = self.account.ui

        # self.layout.addWidget(self.homeUI)
        # self.layout.addWidget(self.messageUI)
        # self.layout.addWidget(self.scheduleUI)
        # self.layout.addWidget(self.settingUI)
        # self.layout.addWidget(self.accountUI)

        # self.setLayout(self.Hbox)


def main():
    import sys
    app = QApplication(sys.argv)
    ex = bodyWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
