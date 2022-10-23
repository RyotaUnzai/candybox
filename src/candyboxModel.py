from PySide2.QtWidgets import *

from models import *
from candyboxView import *


class candyBoxBodyItemModel(object):
    widgetItems = {}

    def setBodyWidgetItems(self, layout):
        for num in range(layout.count()):
            item = layout.takeAt(num)
            try:
                widget = item.widget()
                print(widget)
                print(type(widget))
            except BaseException:
                pass


def debug():
    print("debug")


def showHideWidget(view: candyBoxMainWindow, widgetType: str, bodyWidget: QWidget) -> None:
    print("showHideWidget")
    if widgetType == "homeWidget":
        print(view.cw.body.layout.count())

        print("homeWidget", bodyWidget)

    elif widgetType == "messageWidget":
        print(view.cw.body.layout.count())

        print("messageWidget", bodyWidget)

    elif widgetType == "scheduleWidget":
        print(view.cw.body.layout.count())

        print("scheduleWidget", bodyWidget)

    elif widgetType == "settingWidget":
        print(view.cw.body.layout.count())

        print("settingWidget", bodyWidget)

    elif widgetType == "accountWidget":
        print(view.cw.body.layout.count())

        print("accountWidget", bodyWidget)
