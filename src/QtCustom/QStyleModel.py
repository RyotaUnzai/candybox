from PySide2 import QtGui, QtWidgets
from pydantic import BaseModel


class QStyleOptionButtonModel(BaseModel):
    button: QtWidgets.QStyleOptionButton
    pixmap: QtGui.QPixmap

    class Config:
        arbitrary_types_allowed = True
