
from gramatica import parse
from principal import * 
import ts as TS
from expresiones import *
from instrucciones import *
from report_ast import *
from report_tc import *
from report_ts import *
from report_errores import *


class Intermedio():
	instrucciones_Global = []
	tc_global1 = []
	ts_global1 = []

	def __init__(self):
		''' Funcion Intermedia '''


	def Reportes(self):
		global instrucciones_Global,tc_global1,ts_global1,listaErrores
		#astGraph = AST()
		#astGraph.generarAST(instrucciones_Global)
		typeC = TipeChecker()
		typeC.crearReporte(tc_global1)
		RTablaS = RTablaDeSimbolos()
		RTablaS.crearReporte(ts_global1)
		return ''
