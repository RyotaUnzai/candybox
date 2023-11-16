from PySide2.QtGui import QFont, QFontDatabase

from .fontResource import *


class Raleway:
    Font_Raleway_Black: QFont
    Font_Raleway_BlackItalic: QFont
    Font_Raleway_Bold: QFont
    Font_Raleway_BoldItalic: QFont
    Font_Raleway_ExtraBold: QFont 
    Font_Raleway_ExtraBoldItalic: QFont
    Font_Raleway_ExtraLight: QFont
    Font_Raleway_ExtraLightItalic: QFont
    Font_Raleway_Italic: QFont
    Font_Raleway_Light: QFont
    Font_Raleway_LightItalic: QFont
    Font_Raleway_Medium: QFont
    Font_Raleway_MediumItalic: QFont
    Font_Raleway_Regular: QFont
    Font_Raleway_SemiBold: QFont
    Font_Raleway_SemiBoldItalic: QFont 
    Font_Raleway_Thin: QFont
    Font_Raleway_ThinItalic: QFont
    Font_Raleway_Italic_VF: QFont
    Font_Raleway_VF: QFont

    def __init__(self) -> None:
        self.Font_Raleway_Black = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Black.ttf")
        self.Font_Raleway_BlackItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-BlackItalic.ttf")
        self.Font_Raleway_Bold = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Bold.ttf")
        self.Font_Raleway_BoldItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-BoldItalic.ttf")
        self.Font_Raleway_ExtraBold = self._load_font(":/fonts/Raleway/static/TTF/Raleway-ExtraBold.ttf")
        self.Font_Raleway_ExtraBoldItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-ExtraBoldItalic.ttf")
        self.Font_Raleway_ExtraLight = self._load_font(":/fonts/Raleway/static/TTF/Raleway-ExtraLight.ttf")
        self.Font_Raleway_ExtraLightItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-ExtraLightItalic.ttf")
        self.Font_Raleway_Italic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Italic.ttf")
        self.Font_Raleway_Light = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Light.ttf")
        self.Font_Raleway_LightItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-LightItalic.ttf")
        self.Font_Raleway_Medium = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Medium.ttf")
        self.Font_Raleway_MediumItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-MediumItalic.ttf")
        self.Font_Raleway_Regular = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Regular.ttf")
        self.Font_Raleway_SemiBold = self._load_font(":/fonts/Raleway/static/TTF/Raleway-SemiBold.ttf")
        self.Font_Raleway_SemiBoldItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-SemiBoldItalic.ttf")
        self.Font_Raleway_Thin = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Thin.ttf")
        self.Font_Raleway_ThinItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-ThinItalic.ttf")
        self.Font_Raleway_Italic_VF = self._load_font(":/fonts/Raleway/variable/TTF/Raleway-Italic-VF.ttf")
        self.Font_Raleway_VF = self._load_font(":/fonts/Raleway/variable/TTF/Raleway-VF.ttf")

    def _load_font(self, path: str) -> QFont:
        font_id = QFontDatabase.addApplicationFont(path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        return QFont(font_family, pointSize=12)
