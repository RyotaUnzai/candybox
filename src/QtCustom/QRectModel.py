from PySide2 import QtCore, QtGui, QtWidgets
from typing import Union, TypeVar, Dict, Tuple
from pathlib import WindowsPath
from pydantic import BaseModel, root_validator


class QRectModel(BaseModel):
    rect: Union[QtCore.QRect, QtCore.QRectF]
    x: Union[int, float]
    y: Union[int, float]
    width: Union[int, float]
    height: Union[int, float]

    class Config:
        arbitrary_types_allowed = True

    @root_validator(pre=True)
    def create_new_attribute(cls, values) -> Union[QtCore.QRect, QtCore.QRectF]:
        rect = values.get("rect")
        values["x"] = rect.x()
        values["y"] = rect.y()
        values["width"] = rect.width()
        values["height"] = rect.height()
        return values
