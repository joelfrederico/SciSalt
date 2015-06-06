from . import classes                                    # NOQA
from . import facettools                                 # NOQA
from . import graphics                                   # NOQA
from . import hardcode                                   # NOQA
from . import PWFA                                       # NOQA

from .BDES2K import *                                    # NOQA
from .LinLsqFit import LinLsqFit                         # NOQA
from .NonUniformImage import *                           # NOQA
from .NonUniformImage_axes import NonUniformImage_axes   # NOQA
from .addlabel import addlabel                           # NOQA
from .chisquare import chisquare                         # NOQA
from .create_group import create_group                   # NOQA
from .curve_fit_unscaled import curve_fit_unscaled       # NOQA
from .derefdataset import *                              # NOQA
from .fft import fft
from .figure import figure                               # NOQA
from .fill_missing_timestamps import *                   # NOQA
from .findpinch import findpinch                         # NOQA
from .fitimageslice import fitimageslice                 # NOQA
from .frexp10 import *                                   # NOQA
from .gaussfit import _gauss                             # NOQA
from .gaussfit import _gaussvar                          # NOQA
from .gaussfit import gaussfit                           # NOQA
from .h5drill import *                                   # NOQA
from .hist import hist                                   # NOQA
from .hist2d import hist2d                               # NOQA
from .linspaceborders import linspaceborders             # NOQA
from .linspacestep import linspacestep                   # NOQA
from .mylogger import *                                  # NOQA
from .pcolor_axes import pcolor_axes                     # NOQA
from .picklejar import picklejar                         # NOQA
from .plot_featured import plot_featured                 # NOQA
from .showfig import showfig                             # NOQA


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
