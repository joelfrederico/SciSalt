import logging, inspect

class Keywords(object):
	def __init__(self,**kwargs):
		for name,value in kwargs.items():
			setattr(self,name,value)

class IndentFormatter(logging.Formatter):
	def __init__( self,fmt=None,datefmt=None,indent_offset=6):
		if fmt is None:
			fmt = '%(indent)s------------------\n%(indent)s%(levelname)s - %(name)s:%(funcName)s:%(lineno)d\n%(indent)s%(message)s'

		super(IndentFormatter,self).__init__(fmt=fmt,datefmt=datefmt)
		#  print type(len(inspect.stack()))
		#  print type(indent_offset)
		self.baseline = len(inspect.stack())+indent_offset

	def format( self, rec ):
		stack = inspect.stack()
		stackdepth = len(stack)
		stackdiff = stackdepth-self.baseline
		rec.indent = '\t'*stackdiff
		#  rec.function = stack[8][3]
		out = logging.Formatter.format(self, rec)
		del rec.indent
		#  del rec.function
		return out
