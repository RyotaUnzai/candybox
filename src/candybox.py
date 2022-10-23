import sys
import os
import core

from PySide2.QtWidgets import QApplication
from PySide2.QtGui import *

import candyboxView
import candyboxModel
import candyboxDelegator

import models


if __name__ == "__main__":
    qssloader = core.qssLoader()
    qssloader.filePath = os.path.join(core.PATH_QSS, "main.qss")

    # models.saveFile(path=r"D:\python\candybox\src\qss\test.qss", data=qssloader.styleSheet)
    app = QApplication(sys.argv)
    app.setStyleSheet(qssloader.styleSheet)
    app.setWindowIcon(QPixmap(":/image/app/appIcon.png"))

    delegator = candyboxDelegator.candyBoxDelegator()
    delegator.view = candyboxView.candyBoxMainWindow()
    delegator.model = candyboxModel
    delegator.connect()

    sys.exit(app.exec_())
