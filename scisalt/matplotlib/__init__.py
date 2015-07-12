__all__ = [
    'NonUniformImage',
    'NonUniformImage_axes',
    'addlabel',
    'figure',
    'hist',
    'hist2d',
    'imshow_batch',
    'imshow_slider',
    'pcolor_axes',
    'plot_featured',
    'rgb2gray',
    'setup_figure',
    'showfig',
    ]
import os as _os
on_rtd = _os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    from .cmaps import parula

from .NonUniformImage import NonUniformImage
from .NonUniformImage_axes import NonUniformImage_axes
from .addlabel import addlabel
from .figure import figure
from .hist import hist
from .hist2d import hist2d
from .imshow_batch import imshow_batch
from .imshow_slider import imshow_slider
from .pcolor_axes import pcolor_axes
from .plot_featured import plot_featured
from .rgb2gray import rgb2gray
from .setup_figure import setup_figure
from .showfig import showfig
