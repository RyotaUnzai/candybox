from typing import TypeVar
import threading

from .absCustomFont import AbsCustomFont


class RalewayExtraBoldItalic(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-ExtraBoldItalic" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-ExtraBoldItalic" font. 
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_extrabolditalic_font = RalewayExtraBoldItalic(14)
        >>> print(font_raleway_extrabolditalic_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayExtraBoldItalic'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayExtraBoldItalic")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-ExtraBoldItalic.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewayExtraLight(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-ExtraLight" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-ExtraLight" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_extralight_font = RalewayExtraLight(14)
        >>> print(font_raleway_extralight_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayExtraLight'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayExtraLight")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-ExtraLight.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewayExtraLightItalic(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-ExtraLightItalic" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-ExtraLightItalic" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_extralightitalic_font = RalewayExtraLightItalic(14)
        >>> print(font_raleway_extralightitalic_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayExtraLightItalic'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayExtraLightItalic")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-ExtraLightItalic.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewayItalic(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-Italic" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-Italic" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_italic_font = RalewayItalic(14)
        >>> print(font_raleway_italic_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayItalic'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayItalic")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-Italic.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewayLight(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-Light" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-Light" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_light_font = RalewayLight(14)
        >>> print(font_raleway_light_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayLight'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayLight")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-Light.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewayLightItalic(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-LightItalic" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-LightItalic" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_lightitalic_font = RalewayLightItalic(14)
        >>> print(font_raleway_lightitalic_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayLightItalic'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayLightItalic")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-LightItalic.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewayMedium(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-Medium" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-Medium" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_medium_font = RalewayMedium(14)
        >>> print(font_raleway_medium_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayMedium'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayMedium")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-Medium.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewayMediumItalic(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-MediumItalic" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-MediumItalic" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_mediumitalic_font = RalewayMediumItalic(14)
        >>> print(font_raleway_mediumitalic_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayMediumItalic'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayMediumItalic")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-MediumItalic.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewayRegular(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-Regular" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-Regular" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_regular_font = RalewayRegular(14)
        >>> print(font_raleway_regular_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayRegular'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayRegular")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-Regular.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewaySemiBold(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-SemiBold" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-SemiBold" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_semibold_font = RalewaySemiBold(14)
        >>> print(font_raleway_semibold_font.family())

    Attributes:
        Self: A type variable bound to 'RalewaySemiBold'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewaySemiBold")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-SemiBold.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewaySemiBoldItalic(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-SemiBoldItalic" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-SemiBoldItalic" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_semibolditalic_font = RalewaySemiBoldItalic(14)
        >>> print(font_raleway_semibolditalic_font.family())

    Attributes:
        Self: A type variable bound to 'RalewaySemiBoldItalic'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewaySemiBoldItalic")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-SemiBoldItalic.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewayThin(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-Thin" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-Thin" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_thin_font = RalewayThin(14)
        >>> print(font_raleway_thin_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayThin'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayThin")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-Thin.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewayThinItalic(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-ThinItalic" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-ThinItalic" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_thinitalic_font = RalewayThinItalic(14)
        >>> print(font_raleway_thinitalic_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayThinItalic'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayThinItalic")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-ThinItalic.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewayItalicVF(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-Italic-VF" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-Italic-VF" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_italic_vf_font = RalewayItalicVF(14)
        >>> print(font_raleway_italic_vf_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayItalicVF'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayItalicVF")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-Italic-VF.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance


class RalewayVF(AbsCustomFont):
    """A thread-safe singleton class that encapsulates the "Raleway-VF" font.

    This class inherits from AbsCustomFont, providing a specialized instance for the "Raleway-VF" font.
    It ensures that only a single instance of this font class is created during the application's lifetime,
    following the Singleton design pattern. The class is also thread-safe, ensuring that concurrent
    threads do not create multiple instances.

    Source of Font:
        - https://fonts.google.com/specimen/Raleway

    Args:
        pointSize: The point size of the font. Defaults to 12.

    Examples:
        >>> font_raleway_vf_font = RalewayVF(14)
        >>> print(font_raleway_vf_font.family())

    Attributes:
        Self: A type variable bound to 'RalewayVF'.

    Notes:
        - The font file should be available at the specified path for the class to work correctly.
        - As a singleton, attempting to create another instance of this class will return the same object.
    """
    Self = TypeVar("Self", bound="RalewayVF")
    __lock = threading.Lock()

    def __init__(self: Self, pointSize=12) -> None:
        super().__init__(":/fonts/Raleway/static/TTF/Raleway-VF.ttf", pointSize)

    def __new__(cls: Self, *args, **kwargs) -> Self:
        # Singleton
        if not hasattr(cls, "_instance"):
            # Thread-safe
            with cls.__lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AbsCustomFont, cls).__new__(cls)
        return cls._instance
# class Raleway:
#     Font_Raleway_Black: QFont
#     Font_Raleway_BlackItalic: QFont
#     Font_Raleway_Bold: QFont
#     Font_Raleway_BoldItalic: QFont
#     Font_Raleway_ExtraBold: QFont 
#     Font_Raleway_ExtraBoldItalic: QFont
#     Font_Raleway_ExtraLight: QFont
#     Font_Raleway_ExtraLightItalic: QFont
#     Font_Raleway_Italic: QFont
#     Font_Raleway_Light: QFont
#     Font_Raleway_LightItalic: QFont
#     Font_Raleway_Medium: QFont
#     Font_Raleway_MediumItalic: QFont
#     Font_Raleway_Regular: QFont
#     Font_Raleway_SemiBold: QFont
#     Font_Raleway_SemiBoldItalic: QFont 
#     Font_Raleway_Thin: QFont
#     Font_Raleway_ThinItalic: QFont
#     Font_Raleway_Italic_VF: QFont
#     Font_Raleway_VF: QFont

#     def __init__(self) -> None:
#         self.Font_Raleway_Black = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Black.ttf")
#         self.Font_Raleway_BlackItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-BlackItalic.ttf")
#         self.Font_Raleway_Bold = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Bold.ttf")
#         self.Font_Raleway_BoldItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-BoldItalic.ttf")
#         self.Font_Raleway_ExtraBold = self._load_font(":/fonts/Raleway/static/TTF/Raleway-ExtraBold.ttf")
#         self.Font_Raleway_ExtraBoldItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-ExtraBoldItalic.ttf")
#         self.Font_Raleway_ExtraLight = self._load_font(":/fonts/Raleway/static/TTF/Raleway-ExtraLight.ttf")
#         self.Font_Raleway_ExtraLightItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-ExtraLightItalic.ttf")
#         self.Font_Raleway_Italic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Italic.ttf")
#         self.Font_Raleway_Light = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Light.ttf")
#         self.Font_Raleway_LightItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-LightItalic.ttf")
#         self.Font_Raleway_Medium = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Medium.ttf")
#         self.Font_Raleway_MediumItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-MediumItalic.ttf")
#         self.Font_Raleway_Regular = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Regular.ttf")
#         self.Font_Raleway_SemiBold = self._load_font(":/fonts/Raleway/static/TTF/Raleway-SemiBold.ttf")
#         self.Font_Raleway_SemiBoldItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-SemiBoldItalic.ttf")
#         self.Font_Raleway_Thin = self._load_font(":/fonts/Raleway/static/TTF/Raleway-Thin.ttf")
#         self.Font_Raleway_ThinItalic = self._load_font(":/fonts/Raleway/static/TTF/Raleway-ThinItalic.ttf")
#         self.Font_Raleway_Italic_VF = self._load_font(":/fonts/Raleway/variable/TTF/Raleway-Italic-VF.ttf")
#         self.Font_Raleway_VF = self._load_font(":/fonts/Raleway/variable/TTF/Raleway-VF.ttf")

#     def _load_font(self, path: str) -> QFont:
#         font_id = QFontDatabase.addApplicationFont(path)
#         font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
#         return QFont(font_family, pointSize=12)
