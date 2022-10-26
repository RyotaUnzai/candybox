# Python標準

# PySide2
from PySide2.QtGui import *

from .fontResource import *


class Raleway(object):
    def __init__(self):
        FontDatabase = QFontDatabase()
        # ---------------------------------- remixicon font
        id_01 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-Black.ttf")
        Font_Raleway_Black = FontDatabase.applicationFontFamilies(id_01)[0]
        self.Font_Raleway_Black = QFont(Font_Raleway_Black, pointSize=12)

        id_02 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-BlackItalic.ttf")
        Font_Raleway_BlackItalic = FontDatabase.applicationFontFamilies(id_02)[0]
        self.Font_Raleway_BlackItalic = QFont(Font_Raleway_BlackItalic, pointSize=12)

        id_03 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-Bold.ttf")
        Font_Raleway_Bold = FontDatabase.applicationFontFamilies(id_03)[0]
        self.Font_Raleway_Bold = QFont(Font_Raleway_Bold, pointSize=12)

        id_04 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-BoldItalic.ttf")
        Font_Raleway_BoldItalic = FontDatabase.applicationFontFamilies(id_04)[0]
        self.Font_Raleway_BoldItalic = QFont(Font_Raleway_BoldItalic, pointSize=12)

        id_05 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-ExtraBold.ttf")
        Font_Raleway_ExtraBold = FontDatabase.applicationFontFamilies(id_05)[0]
        self.Font_Raleway_ExtraBold = QFont(Font_Raleway_ExtraBold, pointSize=12)

        id_06 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-ExtraBoldItalic.ttf")
        Font_Raleway_ExtraBoldItalic = FontDatabase.applicationFontFamilies(id_06)[0]
        self.Font_Raleway_ExtraBoldItalic = QFont(Font_Raleway_ExtraBoldItalic, pointSize=12)

        id_07 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-ExtraLight.ttf")
        Font_Raleway_ExtraLight = FontDatabase.applicationFontFamilies(id_07)[0]
        self.Font_Raleway_ExtraLight = QFont(Font_Raleway_ExtraLight, pointSize=12)

        id_08 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-ExtraLightItalic.ttf")
        Font_Raleway_ExtraLightItalic = FontDatabase.applicationFontFamilies(id_08)[0]
        self.Font_Raleway_ExtraLightItalic = QFont(Font_Raleway_ExtraLightItalic, pointSize=12)

        id_09 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-Italic.ttf")
        Font_Raleway_Italic = FontDatabase.applicationFontFamilies(id_09)[0]
        self.Font_Raleway_Italic = QFont(Font_Raleway_Italic, pointSize=12)

        id_10 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-Light.ttf")
        Font_Raleway_Light = FontDatabase.applicationFontFamilies(id_10)[0]
        self.Font_Raleway_Light = QFont(Font_Raleway_Light, pointSize=12)

        id_11 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-LightItalic.ttf")
        Font_Raleway_LightItalic = FontDatabase.applicationFontFamilies(id_11)[0]
        self.Font_Raleway_LightItalic = QFont(Font_Raleway_LightItalic, pointSize=12)

        id_12 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-Medium.ttf")
        Font_Raleway_Medium = FontDatabase.applicationFontFamilies(id_12)[0]
        self.Font_Raleway_Medium = QFont(Font_Raleway_Medium, pointSize=12)

        id_13 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-MediumItalic.ttf")
        Font_Raleway_MediumItalic = FontDatabase.applicationFontFamilies(id_13)[0]
        self.Font_Raleway_MediumItalic = QFont(Font_Raleway_MediumItalic, pointSize=12)

        id_14 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-Regular.ttf")
        Font_Raleway_Regular = FontDatabase.applicationFontFamilies(id_14)[0]
        self.Font_Raleway_Regular = QFont(Font_Raleway_Regular, pointSize=12)

        id_15 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-SemiBold.ttf")
        Font_Raleway_SemiBold = FontDatabase.applicationFontFamilies(id_15)[0]
        self.Font_Raleway_SemiBold = QFont(Font_Raleway_SemiBold, pointSize=12)

        id_16 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-SemiBoldItalic.ttf")
        Font_Raleway_SemiBoldItalic = FontDatabase.applicationFontFamilies(id_16)[0]
        self.Font_Raleway_SemiBoldItalic = QFont(Font_Raleway_SemiBoldItalic, pointSize=12)

        id_17 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-Thin.ttf")
        Font_Raleway_Thin = FontDatabase.applicationFontFamilies(id_17)[0]
        self.Font_Raleway_Thin = QFont(Font_Raleway_Thin, pointSize=12)

        id_18 = FontDatabase.addApplicationFont(":/fonts/Raleway/static/TTF/Raleway-ThinItalic.ttf")
        Font_Raleway_ThinItalic = FontDatabase.applicationFontFamilies(id_18)[0]
        self.Font_Raleway_ThinItalic = QFont(Font_Raleway_ThinItalic, pointSize=12)

        id_19 = FontDatabase.addApplicationFont(":/fonts/Raleway/variable/TTF/Raleway-Italic-VF.ttf")
        Font_Raleway_Italic_VF = FontDatabase.applicationFontFamilies(id_19)[0]
        self.Font_Raleway_Italic_VF = QFont(Font_Raleway_Italic_VF, pointSize=12)

        id_20 = FontDatabase.addApplicationFont(":/fonts/Raleway/variable/TTF/Raleway-VF.ttf")
        Font_Raleway_VF = FontDatabase.applicationFontFamilies(id_20)[0]
        self.Font_Raleway_VF = QFont(Font_Raleway_VF, pointSize=12)
