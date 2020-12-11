import gramatica as g
import ts as TS
from expresiones import *
from instrucciones import *
from graphviz import Digraph

def procesar_createTable(instr,ts) :
    # print('Crear Tabla Normal')
    simbolo = TS.Simbolo(instr.nombre_tabla, TS.TIPO_DATO.CREATE_TABLE, 0)
    ts.agregar(simbolo)
    if instr.intrucc != []:
        procesar_instrucciones(instr.intrucc,ts)

def procesar_createTable_Herencia(instr,ts) :
    # print('Crear Tabla con herencia')
    simbolo = TS.Simbolo(instr.nombre_tabla, TS.TIPO_DATO.CREATE_TABLE, 0)
    ts.agregar(simbolo)
    if instr.intrucc != []:
        procesar_instrucciones(instr.intrucc,ts)

def procesar_Definicion(instr,ts) :
    # print('Definicion')
    simbolo = TS.Simbolo(instr.id.id, TS.TIPO_DATO.CREATE_TABLE, 0)
    ts.agregar(simbolo)

def procesar_instrucciones(instrucciones,ts) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if isinstance(instr, CrearTable) : procesar_createTable(instr,ts)
        elif isinstance(instr, CrearTable_Herencia) : procesar_createTable_Herencia(instr,ts)
        elif isinstance(instr, Definicion) : procesar_Definicion(instr,ts)
        
        else : print('Error: instrucción no válida')

#f = open("./entrada.txt", "r")
#input = f.read()

#print("")



def ts_graph():
    ts_global = TS.TablaDeSimbolos()
    dot3 = Digraph('TS', node_attr={'shape': 'plaintext','color': 'lightblue2'})
    cadena = "<\n"
    cadena = cadena + "<table border='1' cellborder='1'>\n"
    cadena = cadena + "<tr><td colspan='3'>Tabla de Simbolos</td></tr>"
    cadena = cadena + "<tr><td port='port_one'>Id</td><td port='port_two'>Tipo</td><td port='port_three'>Valor</td></tr>"
    for key in ts_global.simbolos:
        cadena2 = "<tr><td port='port_one'>" + str(ts_global.simbolos[key].id) + "</td><td port='port_two'>" + str(ts_global.simbolos[key].tipo) + "</td><td port='port_three'>" + str(ts_global.simbolos[key].valor) + "</td></tr>\n"
        cadena = cadena + cadena2
    cadena = cadena + "</table>"
    cadena = cadena + '>'
    dot3.node('tab', label=cadena)
    dot3.view('TS', cleanup=True)