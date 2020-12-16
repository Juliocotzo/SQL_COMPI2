import gramatica as g
import ts as TS
import tc as TC
from expresiones import *
from instrucciones import *
from graphviz import Digraph
from report_ast import *
from report_tc import *
from report_ts import *
from report_errores import *

from storageManager import jsonMode as j

salida = ""
useCurrentDatabase = ""

def procesar_createTable(instr,ts,tc) :
    columns = []
    i = 0
    if instr.instrucciones != []:
        global salida
        for ins in instr.instrucciones:
            if isinstance(ins, Definicion_Columnas): 
                i+=1
                columns.append(i)
                procesar_Definicion(ins,ts,tc,instr.id)
            elif isinstance(ins, LLave_Primaria): 
                procesar_primaria(ins,ts,tc,instr.id)
            elif isinstance(ins, Definicon_Foranea): 
                procesar_Foranea(ins,ts,tc,instr.id)
            elif isinstance(ins, Lista_Parametros): 
                procesar_listaId(ins,ts,tc,instr.id)
            elif isinstance(ins, definicion_constraint): 
                procesar_constraint(ins,ts,tc,instr.id)
        
        result = j.createTable(str(useCurrentDatabase),str(instr.id),int(len(columns)))
        if result == 0:
            salida = "\nCREATE TABLE"
            temp1 = TS.Simbolo(str(instr.id),'Table',int(len(columns)),str(useCurrentDatabase))
            ts.agregar(temp1)
        elif result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result == 2 :
            salida = "\nERROR:  database \"" + useCurrentDatabase +"\" does not exist \nSQL state: 3D000"
        elif result == 3 :
            salida = "\nERROR:  relation \"" + str(instr.id) +"\" alredy exists\nSQL state: 42P07"
            
def procesar_Definicion(instr,ts,tc,tabla) :
    tipo = TC.Tipo(useCurrentDatabase,tabla,instr.id,instr.tipo_datos.etiqueta,instr.etiqueta,instr.id_referencia,None)
    tc.agregar(tipo)
    
def procesar_listaId(instr,ts,tc,tabla):
    if instr.identificadores != []:
        for ids in instr.identificadores:
            tipo = TC.Tipo(useCurrentDatabase,tabla,ids.id,None,OPCIONESCREATE_TABLE.UNIQUE,None,None)
            tc.actualizarRestriccion(tipo,useCurrentDatabase,tabla,ids.id,OPCIONESCREATE_TABLE.UNIQUE)

def procesar_primaria(instr,ts,tc,tabla):
    tipo = TC.Tipo(useCurrentDatabase,tabla,instr.id,None,OPCIONESCREATE_TABLE.PRIMARIA,None,None)
    tc.actualizarRestriccion(tipo,useCurrentDatabase,tabla,instr.id,OPCIONESCREATE_TABLE.PRIMARIA)

def procesar_Foranea(instr,ts,tc,tabla):
    # print(instr.nombre_tabla,instr.referencia_tabla,instr.campo_referencia)
    tipo = TC.Tipo(useCurrentDatabase,tabla,instr.nombre_tabla,None,OPCIONESCREATE_TABLE.PRIMARIA,instr.campo_referencia,instr.referencia_tabla)
    tc.actualizarLlaveForanea(tipo,useCurrentDatabase,tabla,instr.nombre_tabla,OPCIONESCREATE_TABLE.FORANEA,instr.referencia_tabla,instr.campo_referencia)
    
def procesar_constraint(instr,ts,tc,tabla):
    if instr.tipo == 'UNIQUE':
        if instr.opciones_constraint != []:
            
            temp = TS.Simbolo(instr.id,'CONSTRAINT',0,tabla)
            ts.agregar(temp)
            for ids in instr.opciones_constraint:
                tipo = TC.Tipo(useCurrentDatabase,tabla,ids.id,None,OPCIONESCREATE_TABLE.UNIQUE,None,None)
                tc.actualizarRestriccion(tipo,useCurrentDatabase,tabla,ids.id,OPCIONESCREATE_TABLE.UNIQUE)
    elif instr.tipo == 'FOREING':
        if instr.opciones_constraint != []:
            temp = TS.Simbolo(instr.id,'CONSTRAINT',0,tabla)
            ts.agregar(temp)
            for ids in instr.opciones_constraint:
                tipo = TC.Tipo(useCurrentDatabase,tabla,instr.columna,None,OPCIONESCREATE_TABLE.FORANEA,ids,instr.referencia)
                tc.actualizarLlaveForanea(tipo,useCurrentDatabase,tabla,instr.columna,OPCIONESCREATE_TABLE.FORANEA,instr.referencia,ids)
    elif instr.tipo == 'CHECK':
        if instr.opciones_constraint != []:
            temp = TS.Simbolo(instr.id,'CONSTRAINT',0,tabla)
            ts.agregar(temp)
            for ids in instr.opciones_constraint:
                if type(ids.exp1) == ExpresionIdentificador:
                    tipo = TC.Tipo(useCurrentDatabase,tabla,ids.exp1.id,None,OPCIONES_CONSTRAINT.CHECK,None,None)
                    tc.actualizarRestriccion(tipo,useCurrentDatabase,tabla,ids.exp1.id,OPCIONES_CONSTRAINT.CHECK)
                else: 
                    tipo = TC.Tipo(useCurrentDatabase,tabla,ids.exp2.id,None,OPCIONES_CONSTRAINT.CHECK,None,None)
                    tc.actualizarRestriccion(tipo,useCurrentDatabase,tabla,ids.exp2.id,OPCIONES_CONSTRAINT.CHECK)
    
def procesar_check(instr,ts,tc):
    print('Check')

def procesar_Expresion_Relacional(instr,ts,tc):
    print('Expresion Relacional')

def procesar_Expresion_Binaria(instr,ts,tc):
    print('Expresion Binaria')

def procesar_Expresion_logica(instr,ts,tc):
    print('Expresion Logica')

def resolver_expresion_aritmetica(instr,ts,tc):
    print('Expresion aritmetica')
    
def procesar_Expresion_Numerica(instr,ts,tc):
    print('Entero')

def procesar_createDatabase(instr,ts,tc) :
    if instr.replace == 1:
        
        result = j.dropDatabase(str(instr.nombre.id))
        global salida
        if result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "

        result1 = j.createDatabase(str(instr.nombre.id))
        if result1 == 0:
            temp1 = TS.Simbolo(instr.nombre.id,'Database',0,"")
            ts.agregar(temp1)
            salida = "\nCREATE DATABASE"
            
        elif result1 == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
    else:
        result1 = j.createDatabase(str(instr.nombre.id))
        if result1 == 0:
            salida = "\nCREATE DATABASE"
            temp1 = TS.Simbolo(instr.nombre.id,'Database',0,"")
            ts.agregar(temp1)
        elif result1 == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result1 == 2 :
            salida = "\nERROR:  database \"" + str(instr.nombre.id) +"\" already exists \nSQL state: 42P04 "

def procesar_showDatabases(instr,ts,tc):
    global salida
    data = []
    dataTables = j.showDatabases()
    data.append(['databases'])
    for databases in dataTables:
        data.append([databases])
    if dataTables == []:
        salida = "\nERROR:  databases does not exist \nSQL state: 3D000"
    else:
        salida = data

def procesar_showTables(instr,ts,tc):
    print("SHOW TABLES")
    global salida
    dataT = []
    dataTables = j.showTables(useCurrentDatabase)
    dataT.append(['tables'])
    for tables in dataTables:
        dataT.append([tables])
    if dataTables == []:
        salida = "\nERROR:  Tables does not exist \nSQL state: 3D000"
    else:
        salida = dataT

def procesar_dropDatabase(instr,ts,tc):
    global salida

    result = j.dropDatabase(str(instr.id.id))

    if instr.exists == 0:
        global salida
        if result == 0:
            global salida
            salida = "\nDROP DATABASE"
            ts.deleteDatabase(instr.id.id)
        elif result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
            print("ERROR:  internal_error \nSQL state: XX000 ")
        elif result == 2 :
            salida = "\nERROR:  database \"" + str(instr.id.id) +"\" does not exist \nSQL state: 3D000"
    else:
        if result == 0:
            salida = "\nDROP DATABASE"
        elif result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result == 2 :
            salida = "\nERROR:  database \"" + str(instr.id.id) +"\" does not exist, skipping DROP DATABASE"

def procesar_useDatabase(instr,ts,tc):
    #print(instr.id.id)
    global salida, useCurrentDatabase
    encontrado = False
    dataTables = j.showDatabases()
    for databases in dataTables:
        if databases == instr.id.id:
            encontrado = True
    
    if encontrado:
        global salida, useCurrentDatabase
        useCurrentDatabase = str(instr.id.id)
        salida = "\nYou are now connected to database  \"" + str(instr.id.id) +"\""
    else: 
        salida = "\nERROR:  database \"" + str(instr.id.id) +"\" does not exist \nSQL state: 3D000"
        useCurrentDatabase = ""
        
def procesar_alterdatabase(instr,ts,tc):
    global salida
    
    if isinstance(instr.tipo_id,ExpresionIdentificador) : 
        global salida
        print('OWNER ' + str(instr.tipo_id.id))

    elif isinstance(instr.tipo_id, ExpresionComillaSimple) : 
        print('OWNER ' + str(instr.tipo_id.val))
        
    else:
        result = j.alterDatabase(str(instr.id_tabla),str(instr.tipo_id))
        if result == 0:
            tipo = TC.Tipo(useCurrentDatabase,instr.id_tabla,instr.id_tabla,None,OPCIONES_CONSTRAINT.CHECK,None,None)
            tc.actualizarDatabase(tipo,instr.id_tabla,instr.tipo_id)
            temp1 = ts.obtener(instr.id_tabla,"")
            temp2 = TS.Simbolo(instr.tipo_id,temp1.tipo,temp1.valor,temp1.ambito)
            ts.actualizarDB(temp2,temp1.id)
            ts.actualizarDBTable(temp1.id,temp2.id)
            salida = "\nALTER DATABASE"            

        elif result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result == 2 :
            salida = "\nERROR:  database \"" + str(instr.id_tabla) +"\" does not exist \nSQL state: 3D000"
        elif result == 3 :
            salida = "\nERROR:  database \"" + str(instr.tipo_id) +"\" alredy exists\nSQL state: 42P04"

def procesar_drop(instr,ts,tc):
    if instr.lista_ids != []:
        for datos in instr.lista_ids:
            print(datos.id)

#Alter table

def procesar_altertable(instr,ts,tc):
    print(instr.etiqueta)
    if instr.etiqueta == TIPO_ALTER_TABLE.ADD_CHECK:
        if instr.expresionlogica.operador == TIPO_LOGICA.AND or instr.expresionlogica.operador == TIPO_LOGICA.OR: 
            print(instr.identificador)
            print(instr.expresionlogica.exp1.exp1.id)
            print(instr.expresionlogica.exp1.exp2.val)
            print(instr.expresionlogica.operador)
            print(instr.expresionlogica.exp2.exp1.id)
            print(instr.expresionlogica.exp2.exp2.val)
        else:
            print(instr.identificador)
            print(instr.expresionlogica.exp1.id)
            print(instr.expresionlogica.exp2.val)


    elif instr.etiqueta == TIPO_ALTER_TABLE.ADD_FOREIGN:
        print(instr.identificador)
        if instr.lista_campos != []:
            for datos in instr.lista_campos:
                print(datos.id)
        if instr.lista_ref != []:
            for datos in instr.lista_ref:
                print(datos.id)

    elif instr.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_CHECK:
        print(instr.identificador)
        print(instr.columnid)
        if instr.expresionlogica.operador == TIPO_LOGICA.AND or instr.expresionlogica.operador == TIPO_LOGICA.OR: 
            print(instr.expresionlogica.exp1.exp1.id)
            print(instr.expresionlogica.exp1.exp2.val)
            print(instr.expresionlogica.operador)
            print(instr.expresionlogica.exp2.exp1.id)
            print(instr.expresionlogica.exp2.exp2.val)
        else:
            print(instr.expresionlogica.exp1.id)
            print(instr.expresionlogica.exp2.val)
        
    elif instr.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_UNIQUE:
        print(instr.identificador)
        print(instr.columnid)
        if instr.lista_campos != []:
            for datos in instr.lista_campos:
                print(datos.id)
    elif instr.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_FOREIGN:
        print(instr.identificador)
        print(instr.columnid)
        if instr.lista_campos != []:
            for datos in instr.lista_campos:
                print(datos.id)
        print("references")
        if instr.lista_ref != []:
            for datos in instr.lista_ref:
                print(datos.id)

    elif instr.etiqueta == TIPO_ALTER_TABLE.ALTER_COLUMN:
        print(instr.identificador)
        if instr.lista_campos != []:
            for datos in instr.lista_campos:
                print(datos.identificador.id)
                print(datos.tipo.val)
                if datos.par1 != None:
                    print(datos.par1)
                if datos.par2 != None:
                    print(datos.par2)
    
    elif instr.etiqueta ==  TIPO_ALTER_TABLE.DROP_CONSTRAINT:
        print(instr.identificador)
        if instr.lista_campos != []:
            for datos in instr.lista_campos:
                print(datos.val)

    elif instr.etiqueta ==  TIPO_ALTER_TABLE.RENAME_COLUMN:
        print(instr.identificador)
        print(instr.columnid)
        print(instr.tocolumnid)

    elif instr.etiqueta ==  TIPO_ALTER_TABLE.ADD_COLUMN:
        print(instr.identificador)
        if instr.lista_campos != []:
            for datos in instr.lista_campos:
                print(datos.identificador.val)
                print(datos.tipo.val)
                if datos.par1 != None:
                    print(datos.par1)
                if datos.par2 != None:
                    print(datos.par2)


def procesar_instrucciones(instrucciones,ts,tc) :
    try:
        global salida,useCurrentDatabase
        salida = ""
        ## lista de instrucciones recolectadas
        for instr in instrucciones :
            #CREATE DATABASE
            if isinstance(instr,CreateDatabase) : 
                procesar_createDatabase(instr,ts,tc)
            elif isinstance(instr, Create_Table) : 
                if useCurrentDatabase != "":
                    procesar_createTable(instr,ts,tc)
                else:
                    salida = "\nSELECT DATABASE"
            elif isinstance(instr, ExpresionRelacional) : 
                procesar_Expresion_Relacional(instr,ts,tc)
            elif isinstance(instr, ExpresionBinaria) : 
                procesar_Expresion_Binaria(instr,ts,tc)
            elif isinstance(instr, ExpresionLogica) : 
                procesar_Expresion_logica(instr,ts,tc)
            elif isinstance(instr, showDatabases) : 
                procesar_showDatabases(instr,ts,tc)
            elif isinstance(instr, dropDatabase) : 
                procesar_dropDatabase(instr,ts,tc)
            elif isinstance(instr, useDatabase) : 
                procesar_useDatabase(instr,ts,tc)
            elif isinstance(instr, Create_Alterdatabase) :
                procesar_alterdatabase(instr,ts,tc)
            elif isinstance(instr, showTables) : 
                if useCurrentDatabase != "":
                    procesar_showTables(instr,ts,tc)
                else:
                    salida = "\nSELECT DATABASE"
            elif isinstance(instr, Crear_Drop) : 
                procesar_drop(instr,ts,tc)
            elif isinstance(instr, Crear_altertable) :
                 procesar_altertable(instr,ts,tc)
            else : print('Error: instrucción no válida ' + str(instr))
        return salida 
    except:
        pass

f = open("./entrada.txt", "r")
input = f.read()
listaErrores = []
instrucciones = g.parse(input)
instrucciones_Global = instrucciones
ts_global = TS.TablaDeSimbolos()
tc_global = TC.TablaDeTipos()
procesar_instrucciones(instrucciones,ts_global,tc_global)
erroressss = ErrorHTML()
erroressss.crearReporte()
typeC = TipeChecker()
typeC.crearReporte(tc_global)
typeS = RTablaDeSimbolos()
typeS.crearReporte(ts_global)
astG = AST()
astG.generarAST(instrucciones)
