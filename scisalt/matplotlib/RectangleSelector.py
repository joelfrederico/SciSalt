import os as _os
_on_rtd = _os.environ.get('READTHEDOCS', None) == 'True'
if not _on_rtd:
    import matplotlib.widgets as _mw
    import matplotlib.pyplot as _plt
    import matplotlib.patches as _mp

__all__ = ['RectangleSelector']


class RectangleSelector(object):
    """
    Add rectangle selection to an already-existing axis *as*. *\*args* and *\*\*kwargs* pass through to :class:`matplotlib.widgets.RectangleSelector`.

    Use key *A* or *a* to toggle whether the rectangle is active or not.
    """
    def __init__(self, ax, *args, selfunc=None, **kwargs):
        # ======================================
        # Store things to class
        # ======================================
        self._selfunc = selfunc
        self._ax = ax

        # ======================================
        # Add rectangle selector
        # ======================================
        self._RectangleSelector = _mw.RectangleSelector(ax, self._onselect, *args, **kwargs)
        _plt.connect('key_press_event', self._toggle)

    def _onselect(self, eclick, erelease):
        # ======================================
        # Occurs on release
        # ======================================
        self._eclick = eclick
        self._erelease = erelease
        # print('eclick (x, y):\t\t({}, {})'.format(eclick.xdata, eclick.ydata))
        # print('erelease (x, y):\t({}, {})'.format(erelease.xdata, erelease.ydata))
        try:
            self._rect.remove()
        except:
            pass
        self._rect = self._ax.add_patch(
            _mp.Rectangle(
                xy     = (self.x0, self.y0),
                width  = self.width,
                height = self.height,
                ec     = 'r',
                fc     = 'none'
                )
            )
        _plt.draw()

        if self.selfunc is not None:
            self.selfunc(self)

    @property
    def RectangleSelector(self):
        """
        The instance of :class:`matplotlib.widgets.RectangleSelector`.
        """
        return self._RectangleSelector

    @property
    def ax(self):
        """
        The axis used.
        """
        return self._ax

    @property
    def selfunc(self):
        """
        The function called on each mouse release.
        """
        return self._selfunc

    @property
    def eclick(self):
        """
        The starting mouse click from :class:`scisalt.matplotlib.RectangleSelector.RectangleSelector`.
        """
        return self._eclick

    @property
    def erelease(self):
        """
        The ending mouse click from :class:`scisalt.matplotlib.RectangleSelector.RectangleSelector`.
        """
        return self._erelease

    def _toggle(self, event):
        if event.key in ['A', 'a']:
            self.RectangleSelector.set_active(not self.RectangleSelector.active)

    @property
    def x0(self):
        """
        Minimum x coordinate of rectangle.
        """
        return min([self.erelease.xdata, self.eclick.xdata])

    @property
    def x1(self):
        """
        Maximum x coordinate of rectangle.
        """
        return max([self.erelease.xdata, self.eclick.xdata])

    @property
    def y0(self):
        """
        Minimum y coordinate of rectangle.
        """
        return min([self.erelease.ydata, self.eclick.ydata])

    @property
    def y1(self):
        """
        Maximum y coordinate of rectangle.
        """
        return max([self.erelease.ydata, self.eclick.ydata])

    @property
    def width(self):
        """
        Width of rectangle.
        """
        return self.x1-self.x0

    @property
    def height(self):
        """
        Height of rectangle.
        """
        return self.y1-self.y0
