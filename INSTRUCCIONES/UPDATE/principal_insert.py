import gramatica_insert as g
from expresion_insert import *
from instrucciones_insert import *
from claseast import *

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
        if isinstance(instr,Create_update) : procesar_update(instr)
        else : print('Error: instrucción no válida')

#COSAS DE JONATAN
def procesar_update(instr):
    print(instr.identificador.id)
    if instr.lista_update != []:
        for datos in instr.lista_update:
            print(datos.ids.id)
            print(datos.expresion.val)
   

def procesar_parametro_update(instr):
    print('parametros update')

f = open("./entrada_insert.txt", "r")
input = f.read()

instrucciones = g.parse(input)
procesar_instrucciones(instrucciones)
astclase = AST()
astclase.generarAST(instrucciones)