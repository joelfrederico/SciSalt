import os as _os
on_rtd = _os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    import numpy as _np
    import matplotlib.pyplot as _plt
    from ..matplotlib.plot import plot as _plot

from ..matplotlib.figure import figure
from ..numpy.linspacestep import linspacestep
from ..scipy.gaussfit import GaussResults
from ..matplotlib.imshow import imshow
import logging as _logging
logger = _logging.getLogger(__name__)
import pdb as _pdb


class findpinch(object):
    """
    Finds the location of a bunch in an image *img* given bounds *xbounds* and *ybounds* by slicing image in strips of pixels *step* high.

    """
    def __init__(self, img, xbounds=None, ybounds=None, step=1):
        # ======================================
        # Save things
        # ======================================
        self._img     = img
        self._xbounds = xbounds
        self._ybounds = ybounds
        self._step    = step
        self._ind     = None

        # ======================================
        # Translate to clearer variables
        # ======================================
        if xbounds is None:
            xstart = 0
            xstop = img.shape[0]
        else:
            xstart = xbounds[0]
            xstop  = xbounds[1]

        if ybounds is None:
            ystart = 0
            ystop = img.shape[1]
        else:
            ystart = ybounds[0]
            ystop  = ybounds[1]

        self._ystart = ystart
        self._ystop  = ystop
        self._xstart = xstart
        self._xstop  = xstop

        xrange = slice(xstart, xstop)
        yrange = slice(ystart, ystop)

        img = img[xrange, yrange]
        
        # ======================================
        # Check number of points and
        # initialize arrays
        # ======================================
        num_pts   = (ystop - ystart) / step
        self._variance  = _np.zeros(num_pts)
        self._gr = _np.empty(num_pts, object)
        
        # ======================================
        # Fit individual slices
        # ======================================
        for i, val in enumerate(linspacestep(0, ystop - ystart - step, step)):
            # Take a strip of the image
            strip = img[:, slice(val, val + step)]
            
            # Sum over the strip to get an average of sorts
            histdata = _np.sum(strip, 1)
            xbins = len(histdata)
            x = _np.linspace(1, xbins, xbins)
            
            # Fit with a Gaussian to find spot size
            try:
                self._gr[i] = GaussResults(
                    x,
                    histdata,
                    # sigma_y    = _np.ones(xbins),
                    variance   = False,
                    background = True
                    )

                self._variance[i] = self._gr[i].popt[2]
            except RuntimeError as e:
                print(e)

    @property
    def GaussResults(self):
        return self._gr

    @property
    def variance(self):
        return self._variance

    @property
    def xstart(self):
        return self._xstart

    @property
    def xstop(self):
        return self._xstop

    @property
    def ystart(self):
        return self._ystart

    @property
    def ystop(self):
        return self._ystop

    @property
    def step(self):
        return self._step

    @property
    def yvar(self):
        yvar = _np.shape(linspacestep(self._ystart, self._ystop, self.step))[0] - 1
        yvar = linspacestep(1, yvar)
        return yvar

    @property
    def ind(self):
        if self._ind is None:
            self._ind = self.variance > 0
        return self._ind

    @ind.setter
    def ind(self, val):
        self._ind = val

    @property
    def polyfit(self):
        out = _np.polyfit(self.yvar[self.ind], self.variance[self.ind], 2)
        return out

    @property
    def fitmin(self):
        return -self.polyfit[1] / (2 * self.polyfit[0])

    @property
    def pxmin(self):
        return self.fitmin * self.step + self.ystart

    @property
    def pvar(self):
        return self.ystart + self.yvar[self.ind] * self.step

    def plot(self):
        # ======================================
        # Fit 2nd-deg poly to results
        # ======================================
        _plot(self.pvar, self.variance[self.ind], '.-', self.pvar[self.ind], _np.polyval(self.polyfit, self.yvar[self.ind]), '-')
        _plt.show()
