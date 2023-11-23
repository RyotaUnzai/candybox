from PySide2 import QtCore, QtGui, QtWidgets
from typing import Union, TypeVar, Dict, Tuple
from pathlib import WindowsPath
from pydantic import BaseModel, root_validator


class QPointModel(BaseModel):
    point: Union[QtCore.QPoint, QtCore.QPointF]
    x: Union[int, float]
    y: Union[int, float]

    class Config:
        arbitrary_types_allowed = True

    @root_validator(pre=True)
    def create_new_attribute(cls, values) -> Union[QtCore.QPoint, QtCore.QPointF]:
        point: Union[QtCore.QPoint, QtCore.QPointF] = values.get("point")
        values["x"] = point.x()
        values["y"] = point.y()
        return values
