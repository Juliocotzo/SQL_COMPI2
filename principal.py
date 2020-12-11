import gramatica as g
from expresiones import *
from instrucciones import *

def procesar_createTable(instr) :
    print('Crear Tabla Normal')
    if instr.intrucc != []:
        procesar_instrucciones(instr.intrucc)

def procesar_createTable_Herencia(instr) :
    print('Crear Tabla con herencia')
    if instr.intrucc != []:
        procesar_instrucciones(instr.intrucc)

def procesar_Definicion(instr) :
    print('Definicion')

def procesar_instrucciones(instrucciones) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if isinstance(instr, CrearTable) : procesar_createTable(instr)
        elif isinstance(instr, CrearTable_Herencia) : procesar_createTable_Herencia(instr)
        elif isinstance(instr, Definicion) : procesar_Definicion(instr)
        
        else : print('Error: instrucción no válida')

f = open("./entrada.txt", "r")
input = f.read()

instrucciones = g.parse(input)
procesar_instrucciones(instrucciones)