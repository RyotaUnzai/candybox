import sys
import core

from PySide2.QtWidgets import QApplication
from PySide2.QtGui import *

import candyboxView
import candyboxModel
import candyboxDelegator


if __name__ == "__main__":
    qssloader = core.qssLoader(rootPath=core.PATH_QSS)

    app = QApplication(sys.argv)
    app.setStyleSheet(qssloader.styleSheet)
    app.setWindowIcon(QPixmap(":/image/app/appIcon.png"))

    delegator = candyboxDelegator.candyBoxDelegator()
    delegator.view = candyboxView.candyBoxMainWindow()
    delegator.model = candyboxModel
    delegator.connect()

    sys.exit(app.exec_())
