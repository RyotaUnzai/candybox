from PySide2.QtGui import QFontDatabase, QFont

from .fontResource import *

class Raleway:
    def __init__(self) -> None:
        self.Font_Raleway_Black: QFont = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Black.ttf")
        self.Font_Raleway_BlackItalic: QFont = self._load_font(":/fonts/Raleway/static/TTF/Raleway-BlackItalic.ttf")
        self.Font_Raleway_Bold: QFont = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Bold.ttf")
        self.Font_Raleway_BoldItalic: QFont = self._load_font(":/fonts/Raleway/static/TTF/Raleway-BoldItalic.ttf")
        # ... 他のフォントも同様に

    def _load_font(self, path: str) -> QFont:
        font_id = QFontDatabase.addApplicationFont(path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        return QFont(font_family, pointSize=12)