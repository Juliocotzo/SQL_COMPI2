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
        

    def procesar_database1(self):
        global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
        instrucciones = g.parse('CREATE DATABASE prueba1;')
        erroressss = ErrorHTML()

        if  erroressss.getList()== []:
            instrucciones_Global = instrucciones
            ts_global = TS.TablaDeSimbolos()
            tc_global = TC.TablaDeTipos()
            tc_global1 = tc_global
            ts_global1 = ts_global
            salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
            return salida
        else:
            print('Parser Error')

    def procesar_database2(self):
        global instrucciones_Global,tc_global1,ts_global1,listaErrores,erroressss
        instrucciones = g.parse('CREATE DATABASE prueba2;')
        erroressss = ErrorHTML()

        if  erroressss.getList()== []:
            instrucciones_Global = instrucciones
            ts_global = TS.TablaDeSimbolos()
            tc_global = TC.TablaDeTipos()
            tc_global1 = tc_global
            ts_global1 = ts_global
            salida = procesar_instrucciones(instrucciones, ts_global,tc_global)
            return salida

        else:
            print('Parser Error')


    def Reportes(self):
        global instrucciones_Global,tc_global1,ts_global1,listaErrores
        astGraph = AST()
        astGraph.generarAST(instrucciones_Global)
        typeC = TipeChecker()
        typeC.crearReporte(tc_global1)
        RTablaS = RTablaDeSimbolos()
        RTablaS.crearReporte(ts_global1)
        return ''


'''inter = Intermedio()
inter.procesar_database1()
inter.procesar_database2()
inter.Reportes()'''