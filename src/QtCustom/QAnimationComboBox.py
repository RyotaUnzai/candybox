
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class QAnimationComboBox(QComboBox):
    __PopupOffcet = (0, 0)
    __fade = False
    __stretch = False
    __slide = False

    def __init__(self, parent=None, *args, **kwargs):
        super(QAnimationComboBox, self).__init__(parent, *args, **kwargs)
        self.popup = self.view().window()

    @property
    def PopupOffcet(self):
        return self.__PopupOffcet

    @PopupOffcet.setter
    def PopupOffcet(self, value):
        self.__PopupOffcet = value

    @property
    def fade(self):
        return self.__fade

    @fade.setter
    def fade(self, value):
        self.__fade = value

    @property
    def stretch(self):
        return self.__stretch

    @stretch.setter
    def stretch(self, value):
        self.__stretch = value

    @property
    def slide(self):
        return self.__slide

    @slide.setter
    def slide(self, value):
        self.__slide = value

    def showPopup(self):
        super(CustomeComboBox, self).showPopup()
        self.rect = self.popup.geometry()
        self.popup.move(
            self.rect.x() + self.__PopupOffcet[0],
            self.rect.y() + self.__PopupOffcet[1]
        )

        if self.__fade:
            self.fadeWindowAnimation(start=0, end=1, duration=300, object=self.popup)
        if self.__slide:
            self.slideWindowAnimation(start=10, end=0, duration=300, object=self.popup)
        if self.__stretch:
            self.stretchWindowAnimation(start=0, end=self.rect.height(), duration=300, object=self.popup)

    def hidePopup(self):
        finished = False
        if self.__fade:
            self.fadeWindowAnimation(start=1, end=0, duration=500, object=self.popup)
            if not finished:
                self.opasicyAnimationtion.finished.connect(self.finishedPopup)
                finished = True
        if self.__slide:
            self.slideWindowAnimation(start=0, end=10, duration=300, object=self.popup)
            if not finished:
                self.slideAnimation.finished.connect(self.finishedPopup)
                finished = True
        if self.__stretch:
            self.stretchWindowAnimation(start=self.rect.height(), end=1, duration=400, object=self.popup)
            if not finished:
                self.stretchAnimation.finished.connect(self.finishedPopup)
                finished = True
        if not finished:
            super(CustomeComboBox, self).hidePopup()

    def finishedPopup(self):
        super(CustomeComboBox, self).hidePopup()

    def stretchWindowAnimation(
        self, start=10, end=0, duration=300, object=None,
        animationStyle=None, finishAction=None, windowAnim=True,
        startCurveType=QEasingCurve.OutCubic,
        endCurveType=QEasingCurve.InCubic,
    ):
        geo = object.geometry()
        self.stretchAnimation = QPropertyAnimation(object, b"size", object)
        self.stretchAnimation.setDuration(duration)
        style = QEasingCurve()
        if start >= end:
            style.setType(endCurveType)
        else:
            style.setType(startCurveType)
        if animationStyle is not None:
            style.setType(animationStyle)
        self.stretchAnimation.setEasingCurve(style)
        self.stretchAnimation.setStartValue(QSize(geo.width(), start))
        self.stretchAnimation.setEndValue(QSize(geo.width(), end))
        self.stretchAnimation.start()

    def slideWindowAnimation(
        self, start=-100, end=0, duration=300, object=None,
        animationStyle=None, finishAction=None, windowAnim=True,
        startCurveType=QEasingCurve.OutCubic,
        endCurveType=QEasingCurve.InCubic,
    ):
        pos = object.pos()
        self.slideAnimation = QPropertyAnimation(object, b"pos", object)
        self.slideAnimation.setDuration(duration)
        style = QEasingCurve()
        if start >= end:
            style.setType(endCurveType)
        else:
            style.setType(startCurveType)
        if animationStyle is not None:
            style.setType(animationStyle)
        self.slideAnimation.setEasingCurve(style)
        self.slideAnimation.setStartValue(QPoint(pos.x(), pos.y() + start))
        self.slideAnimation.setEndValue(QPoint(pos.x(), pos.y() + end))
        self.slideAnimation.start()

    def fadeWindowAnimation(
        self, start=0, end=1, duration=300, object=None,
        finishAction=None, windowAnim=True,
        startCurveType=QEasingCurve.OutCubic,
        endCurveType=QEasingCurve.InCubic,
    ):
        style = QEasingCurve()
        if start >= end:
            style.setType(endCurveType)
        else:
            style.setType(startCurveType)

        self.opasicyAnimationtion = QPropertyAnimation(object, b"windowOpacity", object)
        self.opasicyAnimationtion.setEasingCurve(style)
        self.opasicyAnimationtion.setDuration(duration)
        self.opasicyAnimationtion.setStartValue(start)
        self.opasicyAnimationtion.setEndValue(end)
        self.opasicyAnimationtion.start()
