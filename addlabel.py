import matplotlib.pyplot as plt
from warnings import warn

def addlabel(toplabel=None,xlabel=None,ylabel=None,axes=None,clabel=None,cb=None,windowlabel=None,fig=None):
    """Adds labels to a plot."""
    if windowlabel!=None and fig!=None:
        fig.canvas.set_window_title(windowlabel)

    if fig is not None and axes is None:
        axes = fig.get_axes()
        if axes==[]:
            warn('No axes found!',RuntimeWarning)

    if axes is not None:
        if toplabel is not None:
            axes.set_title(toplabel)
        if xlabel is not None:
            axes.set_xlabel(xlabel)
        if ylabel is not None:
            axes.set_ylabel(ylabel)
        if (clabel is not None) and (cb is not None):
            cb.set_label(clabel)

    else:
        warn('No labels added!',RuntimeWarning)

