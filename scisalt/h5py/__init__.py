# Author: Joel Frederico
"""
The :mod:`scisalt.h5py` module provides ways of making it easier to parse :mod:`h5py` modules' into data, and manipulate that data.
"""
__all__ = ['convertH5ref', 'create_group', 'derefdataset', 'H5Drill']
from .derefdataset import derefdataset
from .h5drill import H5Drill
