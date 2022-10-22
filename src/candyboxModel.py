from PySide2.QtWidgets import *

from models import *
from candyboxView import *


def debug():
    print("debug")


def showHideWidget(view: candyBoxMainWindow, widgetType: str, bodyWidget: QWidget) -> None:
    print("showHideWidget")
    if widgetType == "homeWidget":
        print(view.cw.body.layout.count())

        print("homeWidget", bodyWidget)
