import sys
import core

from PySide2 import QtWidgets, QtGui
from pathlib import Path

import candyboxView
import candyboxModel
import candyboxDelegator

# import models


if __name__ == "__main__":
    qssloader = core.QssLoader()
    qssloader.filePath = Path(core.PATH_QSS) / "main.qss"

    # models.saveFile(path=r"D:\python\candybox\src\qss\test.qss", data=qssloader.styleSheet)
    app = QtWidgets.QApplication(sys.argv)
    # app
    app.setWindowIcon(QtGui.QPixmap(":/image/app/appIcon.png"))

    delegator = candyboxDelegator.candyBoxDelegator(
        view=candyboxView.CandyBoxMainWindow(),
        model=candyboxModel
    )
    # delegator.view = candyboxView.candyBoxMainWindow()
    delegator.view.setStyleSheet(qssloader.styleSheet)
    # delegator.model = candyboxModel
    delegator.connect()

    sys.exit(app.exec_())
