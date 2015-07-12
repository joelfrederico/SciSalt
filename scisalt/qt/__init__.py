__all__ = [
    'get_app',
    'Mpl_Image',
    'Mpl_Image_Plus_Slider',
    'Mpl_Plot',
    'Slider_and_Text',
    'Button',
    'getDouble',
    'ButtonMsg',
    'getOpenFileName',
    'getExistingDirectory'
    ]
from .get_app import get_app                                                         # noqa
import os as _os
on_rtd = _os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    from .mplwidget import Mpl_Image, Mpl_Image_Plus_Slider, Mpl_Plot, Slider_and_Text   # noqa
from .ButtonMsg import *                                                             # noqa
from .Rectangle import Rectangle                                                     # noqa
