import gramatica_createT as g
from expresiones import *
from instrucciones import *
import tc as TC

from graphviz import Digraph

def procesar_createTable(instr,tc) :
    # print(instr.id)
    if instr.instrucciones != []:
        i = 0
        while i < len(instr.instrucciones):
            print(instr.instrucciones[i])
            i+=1
        for ins in instr.instrucciones:
            if isinstance(ins, Definicion_Columnas): 
                procesar_Definicion(ins,tc,instr.id)
            elif isinstance(ins, LLave_Primaria): 
                procesar_primaria(ins,tc,instr.id)
            elif isinstance(ins, Definicon_Foranea): 
                procesar_Foranea(ins,tc,instr.id)
            elif isinstance(ins, Lista_Parametros): 
                procesar_listaId(ins,tc,instr.id)
            
        
                  

def procesar_createTable_Herencia(instr,tc) :
    #print('Crear Tabla con herencia')
    if 1>2:
        print("")

def procesar_Definicion(instr,tc,tabla) :
    tipo = TC.Tipo(tabla,instr.id,instr.tipo_datos.etiqueta,instr.etiqueta,instr.id_referencia,None)
    tc.agregar(tipo)
    
def procesar_listaId(instr,tc,tabla):
    if instr.identificadores != []:
        for ids in instr.identificadores:
            print(ids.id)
            tipo = TC.Tipo(tabla,ids.id,None,OPCIONESCREATE_TABLE.UNIQUE,None,None)
            tc.actualizarRestriccion(tipo,tabla,ids.id,OPCIONESCREATE_TABLE.UNIQUE)

def procesar_primaria(instr,tc,tabla):
    tipo = TC.Tipo(tabla,instr.id,None,OPCIONESCREATE_TABLE.PRIMARIA,None,None)
    tc.actualizarRestriccion(tipo,tabla,instr.id,OPCIONESCREATE_TABLE.PRIMARIA)

def procesar_Foranea(instr,tc,tabla):
    # print(instr.nombre_tabla,instr.referencia_tabla,instr.campo_referencia)
    tipo = TC.Tipo(tabla,instr.nombre_tabla,None,OPCIONESCREATE_TABLE.PRIMARIA,instr.campo_referencia,instr.referencia_tabla)
    tc.actualizarLlaveForanea(tipo,tabla,instr.nombre_tabla,OPCIONESCREATE_TABLE.FORANEA,instr.referencia_tabla,instr.campo_referencia)
    

def procesar_constraint(instr,tc):
    #print('constraint')
    #print( instr.id ,  instr.tipo ,  instr.referencia  , instr.columna, instr.opciones_constraint )
    if 1>2:
        print("") 




def procesar_check(instr,tc):
    #print('Check')
    if 1>2:
        print("")

def procesar_Expresion_Relacional(instr,tc):
    #print('Expresion Relacional')
    if 1>2:
        print("")

def procesar_Expresion_Binaria(instr,tc):
    #print('Expresion Binaria')
    if 1>2:
        print("")

def procesar_Expresion_logica(instr,tc):
    #print('Expresion Logica')
    if 1>2:
        print("")

def resolver_expresion_aritmetica(instr,tc):
    #print('Expresion aritmetica')
    if 1>2:
        print("")
    
def procesar_Expresion_Numerica(instr,tc):
    #print('Entero')
    if 1>2:
        print("")

def procesar_instrucciones(instr,tc) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if isinstance(instr, Create_Table) : procesar_createTable(instr,tc)
        elif isinstance(instr, ExpresionRelacional) : procesar_Expresion_Relacional(instr,tc)
        elif isinstance(instr, ExpresionBinaria) : procesar_Expresion_Binaria(instr,tc)
        elif isinstance(instr, ExpresionLogica) : procesar_Expresion_logica(instr,tc)
        elif isinstance(instr, definicion_constraint) : procesar_constraint(instr,tc)
        else : print('Error: instrucción no válida')

f = open("./entrada.txt", "r")
input = f.read()

instrucciones = g.parse(input)
tc_global = TC.TablaDeTipos()
procesar_instrucciones(instrucciones,tc_global)

'''dot3 = Digraph('TS', node_attr={'shape': 'plaintext','color': 'lightblue2'})
cadena = "<\n"
cadena = cadena + "<table border='1' cellborder='1'>\n"
cadena = cadena + "<tr><td colspan='3'>Tabla de Simbolos</td></tr>"
cadena = cadena + "<tr><td port='port_one'>Id</td><td port='port_two'>Tipo</td><td port='port_three'>Valor</td></tr>"
for key in tc_global.tipos:
    cadena2 = "<tr><td port='port_one'>" + str(tc_global.tipos[key].id) + "</td><td port='port_two'>" + str(tc_global.tipos[key].tipo) + "</td><td port='port_three'>" + str(tc_global.tipos[key].restriccion) + "</td></tr>\n"
    cadena = cadena + cadena2
cadena = cadena + "</table>"
cadena = cadena + '>'
dot3.node('tab', label=cadena)
dot3.view('TS', cleanup=True)'''

'''
print("PRUEBA")
print(tc_global.tipos[0].tabla,tc_global.tipos[0].id,tc_global.tipos[0].tipo,tc_global.tipos[0].restriccion)
tipo = TC.Tipo(tc_global.tipos[0].tabla,tc_global.tipos[0].id,None,None,None,None)
tc_global.actualizarRestriccion(tipo,tc_global.tipos[0].tabla,tc_global.tipos[0].id,OPCIONESCREATE_TABLE.PRIMARIA_SOLA)
print(tc_global.tipos[0].tabla,tc_global.tipos[0].id,tc_global.tipos[0].tipo,tc_global.tipos[0].restriccion)

'''


'''dot3 = Digraph('TS', node_attr={'shape': 'plaintext','color': 'lightblue2'})
cadena = "<\n"
cadena = cadena + "<table border='1' cellborder='1'>\n"
cadena = cadena + "<tr><td colspan='7'>TYPE CHECKER</td></tr>"
cadena = cadena + "<tr><td port='port_cero'>No.</td><td port='port_one'>Tabla</td><td port='port_two'>ID</td><td port='port_three'>TIPO</td><td port='port_four'>RESTRICCION</td><td port='port_five'>REFERENCIA</td><td port='port_six'>TABLA REF</td></tr>"

    

i = 0
while i < len(tc_global.tipos):
    cadena2 = "<tr><td port='port_cero'>" + str(i) + "</td><td port='port_one'>" + str(tc_global.tipos[i].tabla) + "</td><td port='port_two'>" + str(tc_global.tipos[i].id) + "</td><td port='port_three'>" + str(tc_global.tipos[i].tipo) + "</td><td port='port_four'>" + str(tc_global.tipos[i].restriccion) + "</td><td port='port_five'>" + str(tc_global.tipos[i].referencia) + "</td><td port='port_six'>" + str(tc_global.tipos[i].tablaRef) + "</td></tr>\n"
    cadena = cadena + cadena2
    i += 1
cadena = cadena + "</table>"
cadena = cadena + '>'
dot3.node('tab', label=cadena)
dot3.view('reportes/TC', cleanup=True)'''

f = open("reportes/tc.html", "w")
f.write("<!DOCTYPE html>")
f.write("<html lang=\"en\" class=\"no-js\">")
f.write("")
f.write("<head>")
f.write("    <meta charset=\"UTF-8\" />")
f.write("    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">")
f.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
f.write("    <title>Type Checker </title>")
f.write("    <meta name=\"description\"")
f.write("        content=\"Sticky Table Headers Revisited: Creating functional and flexible sticky table headers\" />")
f.write("    <meta name=\"keywords\" content=\"Sticky Table Headers Revisited\" />")
f.write("    <meta name=\"author\" content=\"Codrops\" />")
f.write("    <link rel=\"shortcut icon\" href=\"../favicon.ico\">")
f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/normalize.css\" />")
f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/demo.css\" />")
f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/component.css\" />")
f.write("</head>")

f.write("<body>")
f.write("    <div class=\"container\">")
f.write("        <!-- Top Navigation -->")
f.write("        <header>")
f.write("            <h1>Type Checker</h1>")
f.write("        </header>")
f.write("        <div class=\"component\">")
f.write("            <table>")
f.write("                <thead>")
f.write("                    <tr>")
f.write("                        <th>No.</th>")
f.write("                        <th>TABLA</th>")
f.write("                        <th>ID</th>")
f.write("                        <th>TIPO</th>")
f.write("                        <th>RESTRICCION</th>")
f.write("                        <th>REFERENCIA</th>")
f.write("                        <th>TABLA REFERENCIA</th>")
f.write("                    </tr>")
f.write("                </thead>")
f.write("                <tbody>")
i = 0
while i < len(tc_global.tipos):
    f.write("                    <tr>")
    f.write("                        <td class=\"text-left\">"+ str(i) +"</td>")
    f.write("                        <td class=\"text-left\">"+ str(tc_global.tipos[i].tabla) +"</td>")
    f.write("                        <td class=\"text-left\">"+ str(tc_global.tipos[i].id) +"</td>")
    f.write("                        <td class=\"text-left\">"+ str(tc_global.tipos[i].tipo) +"</td>")
    f.write("                        <td class=\"text-left\">"+ str(tc_global.tipos[i].restriccion) +"</td>")
    f.write("                        <td class=\"text-left\">"+ str(tc_global.tipos[i].referencia) +"</td>")
    f.write("                        <td class=\"text-left\">"+ str(tc_global.tipos[i].tablaRef) +"</td>")
    f.write("                    </tr>")
    i += 1
f.write("                </tbody>")
f.write("            </table>")
f.write("        </div>")
f.write("    </div><!-- /container -->")
f.write("    <script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js\"></script>")
f.write("    <script src=\"http://cdnjs.cloudflare.com/ajax/libs/jquery-throttle-debounce/1.1/jquery.ba-throttle-debounce.min.js\"></script>")
f.write("    <script src=\"js/jquery.stickyheader.js\"></script>")
f.write("</body>")
f.write("")
f.write("</html>")
f.close()