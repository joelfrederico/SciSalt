import os as _os
_on_rtd = _os.environ.get('READTHEDOCS', None) == 'True'
if not _on_rtd:
    import matplotlib.widgets as _mw
    import matplotlib.pyplot as _plt

__all__ = ['RectangleSelector']


class RectangleSelector(object):
    """
    Add rectangle selection to an already-existing axis *as*. *\*args* and *\*\*kwargs* pass through to :class:`matplotlib.widgets.RectangleSelector`.

    Use key *A* or *a* to toggle whether the rectangle is active or not.
    """
    def __init__(self, ax, *args, **kwargs):
        self._rs = _mw.RectangleSelector(ax, self._onselect, *args, **kwargs)
        _plt.connect('key_press_event', self._toggle)

    def _onselect(self, eclick, erelease):
        self.eclick = eclick
        self.erelease = erelease

    def _toggle(self, event):
        if event.key in ['A', 'a']:
            self._rs.set_active(not self._rs.active)
