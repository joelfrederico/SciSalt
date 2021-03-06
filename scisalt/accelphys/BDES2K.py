import os as _os
on_rtd = _os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    import numpy as _np

import logging
loggerlevel = 9
logger      = logging.getLogger(__name__)

__all__ = ['BDES2K', 'K2BDES']


def BDES2K(bdes, quad_length, energy):
    """
    Converts a quadrupole :math:`B_des` into a geometric focusing strength :math:`K`.

    Parameters
    ----------

    bdes : float
        The magnet value of :math:`B_des`.
    quad_length : float
        The length of the quadrupole in meters.
    energy : float
        The design energy of the beam in GeV.

    Returns
    -------
    K : float
        The geometric focusing strength :math:`K`.
    """
    # Make sure everything is float
    bdes        = _np.float_(bdes)
    quad_length = _np.float_(quad_length)
    energy      = _np.float_(energy)

    Brho = energy/_np.float_(0.029979)
    K = bdes/(Brho*quad_length)
    logger.log(level=loggerlevel, msg='Converted BDES: {bdes}, quad length: {quad_length}, energy: {energy} to K: {K}'.format(
        bdes        = bdes        ,
        quad_length = quad_length ,
        energy      = energy      ,
        K           = K
        )
        )

    return K


def K2BDES(K, quad_length, energy):
    """
    Returns the BDES for a quadrupole with geometric strength *K* and length *quad_length* for a beam with a given *energy*.
    Converts a geometric focusing strength :math:`K` into a quadrupole :math:`B_des`.

    Parameters
    ----------
    K : float
        The geometric focusing strength :math:`K`.
    quad_length : float
        The length of the quadrupole in meters.
    energy : float
        The design energy of the beam in GeV.

    Returns
    -------
    bdes : float
        The magnet value of :math:`B_des`.
    """
    # Make sure everything is float
    K           = _np.float_(K)
    quad_length = _np.float_(quad_length)
    energy      = _np.float_(energy)

    Brho = energy/_np.float_(0.029979)
    BDES = K*Brho*quad_length
    logger.log(level=loggerlevel, msg='Converted K: {K}, quad length: {quad_length}, energy: {energy} to BDES: {bdes}'.format(
        bdes        = BDES        ,
        quad_length = quad_length ,
        energy      = energy      ,
        K           = K
        )
        )
    return BDES
