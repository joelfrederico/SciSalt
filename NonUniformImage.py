import matplotlib.image as mplim
def NonUniformImage(x,y,z,ax):
    im = mplim.NonUniformImage(ax)
    im.set_data(x,y,z)
    ax.images.append(im)

    xmin = min(x)
    xmax = max(x)

    ymin = min(y)
    ymax = max(y)

    ax.set_xlim(xmin,xmax)
    ax.set_ylim(ymin,ymax)

    return im
