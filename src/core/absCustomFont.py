from PySide2.QtGui import QFont, QFontDatabase
from typing import TypeVar

from .fontResource import *


class AbsCustomFont(QFont):
    """
    A base class for managing custom fonts.

    This class inherits from QFont and provides functionality to add custom fonts to an application. 
    It loads a font from a specified font file and sets up the font for use.

    Attributes:
        Self: A type variable representing an instance of AbsCustomFont or its subclasses.

    Args:
        fontPath : The path to the font file.
        pointSize : The point size of the font. Default is 12.

    Raises:
        FileNotFoundError: Raised if the specified font file does not exist.

    Examples:
        >>> custom_font = AbsCustomFont("/path/to/font.<extention>")
        >>> print(custom_font.family())
    """
    Self = TypeVar("Self", bound="AbsCustomFont")

    def __init__(self: Self, fontPath:str, pointSize: int=12) -> Self:
        super(AbsCustomFont, self).__init__()
        fontId = QFontDatabase.addApplicationFont(fontPath)
        fontFamilies = QFontDatabase.applicationFontFamilies(fontId)
        if fontFamilies:
            self.setFamily(fontFamilies[0])
            self.setPointSize(pointSize)
        else:
            raise FileNotFoundError(f"Font file not found: {fontPath}")