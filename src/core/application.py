
from PySide2 import QtWidgets
from typing import Any


class Delegator:
    view: QtWidgets.QMainWindow
    model: Any

    def __init__(self, view: QtWidgets.QMainWindow, model: Any) -> None:
        self.view = view
        self.model = model

    def connect(self) -> None:
        ...
