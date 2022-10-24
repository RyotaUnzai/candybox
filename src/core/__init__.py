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
