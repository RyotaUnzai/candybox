import os

from pathlib import Path
from PySide2 import QtCore

from .application import *
from .fontRemixicon import *
from .fontRaleway import *
from .qssloader import *
from .imageResource import *

PATH_ABS = Path(os.getcwd())
PATH_SRC = PATH_ABS / "src"
PATH_VIEWS = PATH_SRC / "views"
PATH_QSS = PATH_SRC / "qss"
PATH_RESOURCE = PATH_ABS / "resource"
PATH_DATA = PATH_ABS / "data"

# Qt UserOrle
IncludeAssetsRole = QtCore.Qt.UserRole
LastAuthorRole = QtCore.Qt.UserRole + 1
AssetVersionRole = QtCore.Qt.UserRole + 2
MaterialParametersDataRole = QtCore.Qt.UserRole + 3
LabelsRole = QtCore.Qt.UserRole + 4
BaseUriRole = QtCore.Qt.UserRole + 5
FileUpdateTimeRole = QtCore.Qt.UserRole + 6
MetadataUpdateTimeRole = QtCore.Qt.UserRole + 7
AuthorsRole = QtCore.Qt.UserRole + 8
ReferenceAssetsRole = QtCore.Qt.UserRole + 9
ThumbnailRole = QtCore.Qt.UserRole + 10
ImportTimeRole = QtCore.Qt.UserRole + 11
MD5Role = QtCore.Qt.UserRole + 12

ThumbnailImgRole = QtCore.Qt.UserRole + 100
ThumbnailImgPathRole = QtCore.Qt.UserRole + 101
FilePathRole = QtCore.Qt.UserRole + 102
