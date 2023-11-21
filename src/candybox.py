import sys
import core

from PySide2 import QtWidgets, QtGui
from pathlib import Path

from candyboxView import CandyBoxMainWindow
from candyboxModel import CandyBoxModels
from candyboxDelegator import CandyBoxDelegator


if __name__ == "__main__":
    qssloader: core.QssLoader = core.QssLoader()
    qssloader.filePath = Path(core.PATH_QSS) / "main.qss"
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QPixmap(":/image/app/appIcon.png"))
    delegator: CandyBoxDelegator = CandyBoxDelegator(
        view=CandyBoxMainWindow(), model=CandyBoxModels()
    )
    delegator.view.setStyleSheet(qssloader.styleSheet)
    delegator.connect()
    sys.exit(app.exec_())
