# PySide2
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class QFlowLayout(QLayout):
    __margin = (0, 0, 0, 0)
    __spacing = -1
    __space = (5, 5)

    def __init__(self, parent=None, margin=(0, 0, 0, 0), spacing=-1):
        super(QFlowLayout, self).__init__(parent)
        self.margin = margin
        self.spacing = spacing
        self.parent = parent

        if self.parent is not None:
            self.setContentsMargins(self.margi[0], self.margin[1], self.margin[2], self.margin[3])

        self.itemList = []

    @property
    def margin(self):
        return self.__margin

    @margin.setter
    def margin(self, value):
        if isinstance(value, int):
            self.__margin = (value, value, value, value)
        elif len(value) == 2:
            self.__margin = (value[0], value[1], value[0], value[1])
        elif len(value) == 3:
            self.__margin = (value[0], value[1], value[2], value[1])
        elif len(value) == 4:
            self.__margin = (value[0], value[1], value[2], value[3])

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        self.__parent = value

    @property
    def space(self):
        return self.__space

    @space.setter
    def space(self, value):
        self.__space = value
        self.spaceX = self.__space[0]
        self.spaceY = self.__space[1]

    @property
    def spacing(self):
        return self.__spacing

    @spacing.setter
    def spacing(self, value):
        self.__spacing = value

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(QFlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        size += QSize(2 * self.margin, 2 * self.margin)
        return size

    def doLayout(self, rect, heightForWidth):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            nextX = x + item.sizeHint().width() + self.spaceX
            if nextX - self.spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + self.spaceY
                nextX = x + item.sizeHint().width() + self.spaceX
                lineHeight = 0

            if not heightForWidth:
                item.setGeometry(
                    QRect(
                        QPoint(
                            x,
                            y
                        ),
                        item.sizeHint()
                    )
                )

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()
