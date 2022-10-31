import os

from .application import *
from .fontRemixicon import *
from .fontRaleway import *
from .qssloader import *
from .imageResource import *

PATH_ABS = os.path.abspath(os.getcwd())
PATH_SRC = os.path.join(PATH_ABS, "src")
PATH_VIEWS = os.path.join(PATH_SRC, "views")
PATH_QSS = os.path.join(PATH_SRC, "qss")
PATH_RESOURCE = os.path.join(PATH_ABS, "resource")
PATH_DATA = os.path.join(PATH_ABS, "data")

# Qt UserOrle
IncludeAssetsRole = Qt.UserRole
LastAuthorRole = Qt.UserRole + 1
AssetVersionRole = Qt.UserRole + 2
MaterialParametersDataRole = Qt.UserRole + 3
LabelsRole = Qt.UserRole + 4
BaseUriRole = Qt.UserRole + 5
FileUpdateTimeRole = Qt.UserRole + 6
MetadataUpdateTimeRole = Qt.UserRole + 7
AuthorsRole = Qt.UserRole + 8
ReferenceAssetsRole = Qt.UserRole + 9
ThumbnailRole = Qt.UserRole + 10
ImportTimeRole = Qt.UserRole + 11
MD5Role = Qt.UserRole + 12

ThumbnailImgRole = Qt.UserRole + 100
ThumbnailImgPathRole = Qt.UserRole + 101
FilePathRole = Qt.UserRole + 102
