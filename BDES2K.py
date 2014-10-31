import logging
loggerlevel=9
logger=logging.getLogger(__name__)

__all__ = ['BDES2K','K2BDES']

def BDES2K(bdes,quad_length,energy):
	Brho = energy/0.029979
	K = bdes/(Brho*quad_length)
	logger.log(level=loggerlevel,msg='Converted BDES: {bdes}, quad length: {quad_length}, energy: {energy} to K: {K}'.format(
		bdes        = bdes        ,
		quad_length = quad_length ,
		energy      = energy      ,
		K           = K
		)
		)

	return K

def K2BDES(K,quad_length,energy):
	Brho = energy/0.029979
        BDES = K*Brho*quad_length
	logger.log(level=loggerlevel,msg='Converted K: {K}, quad length: {quad_length}, energy: {energy} to BDES: {bdes}'.format(
		bdes        = BDES        ,
		quad_length = quad_length ,
		energy      = energy      ,
		K           = K
		)
		)
        return BDES
