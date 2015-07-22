__all__ = [
    'Imshow_Slider',
    'NonUniformImage',
    'NonUniformImage_axes',
    'RectangleSelector',
    'addlabel',
    'axesfontsize',
    'colorbar',
    'figure',
    'hist',
    'hist2d',
    'imshow_batch',
    'imshow',
    'latexfig',
    'less_labels',
    'pcolor_axes',
    'plot_featured',
    'rgb2gray',
    'savefig',
    'scaled_figsize'
    'setup_axes',
    'setup_figure',
    'showfig',
    ]
import os as _os
on_rtd = _os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    from .cmaps import parula
    from .cmaps import viridis
    __all__.append('parula')
    __all__.append('viridis')
    __all__.sort()

from .Imshow_Slider import Imshow_Slider
from .NonUniformImage import NonUniformImage
from .NonUniformImage_axes import NonUniformImage_axes
from .RectangleSelector import RectangleSelector
from .addlabel import addlabel
from .axesfontsize import axesfontsize
from .colorbar import colorbar
from .figure import figure
from .hist import hist
from .hist2d import hist2d
from .imshow_batch import imshow_batch
from .imshow import imshow
from .imshow import scaled_figsize
from .latexfig import latexfig
from .less_labels import less_labels
from .pcolor_axes import pcolor_axes
from .plot_featured import plot_featured
from .rgb2gray import rgb2gray
from .savefig import savefig
from .setup_axes import setup_axes
from .setup_figure import setup_figure
from .showfig import showfig
