from . import classes
from . import graphics
from . import hardcode
from . import PWFA
# from . import qt

from .BDES2K import *
from .LinLsqFit import LinLsqFit
from .addlabel import addlabel
from .chisquare import chisquare
from .create_group import create_group
from .curve_fit_unscaled import curve_fit_unscaled
from .derefdataset import *
from .figure import figure
from .findpinch import findpinch
from .fitimageslice import fitimageslice
from .gaussfit import _gauss
from .gaussfit import _gaussvar
from .gaussfit import gaussfit
from .hist import hist
from .hist2d import hist2d
from .linspaceborders import linspaceborders
from .linspacestep import linspacestep
from .mylogger import *
from .picklejar import picklejar
from .plot_featured import plot_featured
from .showfig import showfig
from .NonUniformImage import *
from .frexp10 import *
from .pcolor_axes import pcolor_axes
from .NonUniformImage_axes import NonUniformImage_axes

from .h5drill import *


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class ArgumentError(Error):
    """Exception raised for errors in function arguments.

    Attributes:
        arg -- input argument in which the error occurred
        msg -- explanation of the error
    """

    def __init__(self, arg, msg):
        self.arg = arg
        self.msg = msg
