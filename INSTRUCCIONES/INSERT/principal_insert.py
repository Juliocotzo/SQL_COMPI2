import gramatica_insert as g
from expresion_insert import *
from instrucciones_insert import *
from report_ast import *

def procesar_insert(instr):
    print('esta en el insert')

    if instr.etiqueta == TIPO_INSERT.CON_PARAMETROS:
        if instr.lista_parametros != []:
            for parametros in instr.lista_parametros:
                print(instr.id, instr.etiqueta, parametros.id)

        if instr.lista_datos != []:
            for parametros in instr.lista_datos:
                print(parametros.val)
            
    else:
        if instr.lista_datos != []:
            for parametros in instr.lista_datos:
                print(parametros.val)




def procesar_instrucciones(instrucciones) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if isinstance(instr, Definicion_Insert) : procesar_insert(instr)
        else : print('Error: instrucción no válida')

f = open("./entrada_insert.txt", "r")
input = f.read()

instrucciones = g.parse(input)
procesar_instrucciones(instrucciones)
ast = AST()
ast.generarAST(instrucciones)
