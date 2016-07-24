import numpy as _np


class EmitEllipse(object):
    def __init__(self, emit, alpha, beta):
        self._emit  = emit
        self._alpha = alpha
        self._beta  = beta

        gamma = (1+alpha**2)/beta

        if alpha == 0:
            theta = 0
        else:
            theta = _np.arctan(2*alpha/(gamma-beta))/2
        
        sth = _np.sin(theta)
        cth = _np.cos(theta)
        a = (gamma*cth**2 + 2*alpha*sth*cth + beta*sth**2)/emit
        c = (gamma*sth**2 - 2*alpha*sth*cth + beta*cth**2)/emit
        
        self._width  = 2/_np.sqrt(a)
        self._height = 2/_np.sqrt(c)

        self._theta_deg = theta*180/_np.pi

    @property
    def emit(self):
        return self._emit

    @property
    def alpha(self):
        return self._alpha

    @property
    def beta(self):
        return self._beta

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def theta_deg(self):
        return self._theta_deg
