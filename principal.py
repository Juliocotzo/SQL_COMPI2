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
pks = []

def procesar_createTable(instr,ts,tc) :
    global pks
    columns = []
    numC = 0
    i = 0
    if instr.instrucciones != []:
        
        global salida
        for ins in instr.instrucciones:
            if instr.herencia != None:
                columnsH = tc.obtenerColumns(useCurrentDatabase,instr.herencia)
                numC = len(columnsH)
                #ACTUALIZAR NUM TABLA
                '''temp1 = ts.obtener(instr.val,useCurrentDatabase)
                temp2 = TS.Simbolo(temp1.val,temp1.tipo,temp1.valor+numC,temp1.ambito)
                ts.actualizarTableNum(temp2,instr.val,useCurrentDatabase)'''
                if columnsH != []:
                    for col in columnsH:
                        typeC = tc.obtenerReturn(useCurrentDatabase,instr.herencia,col)
                        newType = TC.Tipo(typeC.database,instr.val,typeC.val,typeC.tipo,typeC.tamanio,typeC.referencia,typeC.tablaRef,[])
                        if typeC != False:
                            tc.agregar(newType) 
            if isinstance(ins, Definicion_Columnas): 
                i+=1
                columns.append(i)
                procesar_Definicion(ins,ts,tc,instr.val)
            elif isinstance(ins, LLave_Primaria): 
                procesar_primaria(ins,ts,tc,instr.val)
            elif isinstance(ins, Definicon_Foranea): 
                procesar_Foranea(ins,ts,tc,instr.val)
            elif isinstance(ins, Lista_Parametros): 
                procesar_listaId(ins,ts,tc,instr.val)
            elif isinstance(ins, definicion_constraint): 
                procesar_constraint(ins,ts,tc,instr.val)
    
        

    

    try:
        #print(str(useCurrentDatabase),str(instr.val),int(len(columns)))
        result = j.createTable(str(useCurrentDatabase),str(instr.val),int(len(columns))+numC)
        if result == 0:
            salida = "\nCREATE TABLE"
            temp1 = TS.Simbolo(str(instr.val),'Table',int(len(columns)+numC),str(useCurrentDatabase))
            ts.agregar(temp1)
        elif result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result == 2 :
            salida = "\nERROR:  database \"" + useCurrentDatabase +"\" does not exist \nSQL state: 3D000"
        elif result == 3 :
            salida = "\nERROR:  relation \"" + str(instr.val) +"\" alredy exists\nSQL state: 42P07"
    except :
        pass

    try:
        #print(pks)
        result = j.alterAddPK(str(useCurrentDatabase),str(instr.val),pks)
        pks = []
        #print(pks)

    except :
        pass

    

            
def procesar_Definicion(instr,ts,tc,tabla) :
    tipo_dato = ""
    tamanio = ""
    if(isinstance(instr.tipo_datos,Etiqueta_tipo)):
        tipo_dato = instr.tipo_datos.etiqueta
        tamanio = ""
    elif(isinstance(instr.tipo_datos,ExpresionNumero)):
        tipo_dato = instr.tipo_datos.etiqueta
        tamanio = instr.tipo_datos.val
    elif(isinstance(instr.tipo_datos,Etiqueta_Interval)):
        tipo_dato = instr.tipo_datos.etiqueta
        tamanio = instr.tipo_datos.ext_time
    elif(isinstance(instr.tipo_datos,ExpresionTiempo)):
        tipo_dato = instr.tipo_datos.operador
        tamanio =  ""
    elif(isinstance(instr.tipo_datos,Expresion_Caracter)):
        tipo_dato = instr.tipo_datos.etiqueta
        tamanio =  instr.val
    
    if instr.opciones_constraint == None:
        buscar = tc.obtenerReturn(useCurrentDatabase,tabla,instr.val)
        if buscar == False:
            tipo = TC.Tipo(useCurrentDatabase,tabla,instr.val,tipo_dato,tamanio,"","",[])
            tc.agregar(tipo)
        else:
            print('No Encontrado')
            
    else:
        buscar = tc.obtenerReturn(useCurrentDatabase,tabla,instr.val)
        if buscar == False:
            tipo = TC.Tipo(useCurrentDatabase,tabla,instr.val,tipo_dato,tamanio,"","",[])
            tc.agregar(tipo)
        else:
            print('No Encontrado')
            
        for ins in instr.opciones_constraint:
            if isinstance(ins, definicion_constraint): 
                procesar_constraintDefinicion(ins,ts,tc,tabla,instr.val)

        

        
    
def procesar_constraintDefinicion(instr,ts,tc,tabla,id_column):
    #print(tabla,id,instr.val,instr.tipo)
    global pks
    if instr.val == None:
        if instr.tipo == OPCIONES_CONSTRAINT.NOT_NULL:
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
            if buscar == False:
                print('Encontrado')
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.NOT_NULL)
                tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
        elif instr.tipo == OPCIONES_CONSTRAINT.NULL:
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
            if buscar == False:
                print('Encontrado')
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.NULL)
                tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
        elif instr.tipo == OPCIONES_CONSTRAINT.PRIMARY:
            pk = []
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
            if buscar == False:
                print('Encontrado')
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.PRIMARY)
                tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
                pos = tc.getPos(useCurrentDatabase,tabla,id_column)
                pk.append(pos)
                
            pks = pk
                
            


        elif instr.tipo == OPCIONES_CONSTRAINT.FOREIGN:
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
            if buscar == False:
                print('Encontrado')
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.FOREIGN)
                tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
        elif instr.tipo == OPCIONES_CONSTRAINT.UNIQUE:
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
            if buscar == False:
                print('Encontrado')
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.UNIQUE)
                tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
        elif instr.tipo == OPCIONES_CONSTRAINT.DEFAULT:
            if instr.opciones_constraint != []:
                buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
                if buscar == False:
                    print('Encontrado')
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.DEFAULT)
                    tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
        elif instr.tipo == OPCIONES_CONSTRAINT.CHECK:
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
            if buscar == False:
                print('Encontrado')
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.CHECK)
                tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)

    else:
        if instr.tipo == OPCIONES_CONSTRAINT.UNIQUE:
            if instr.opciones_constraint == None:
                temp = TS.Simbolo(instr.val,'CONSTRAINT',0,tabla)
                ts.agregar(temp)
                buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
                if buscar == False:
                    print('Encontrado')
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.UNIQUE)
                    tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
        elif instr.tipo == OPCIONES_CONSTRAINT.CHECK:
            if instr.opciones_constraint != None:
                temp = TS.Simbolo(instr.val,'CONSTRAINT',0,tabla)
                ts.agregar(temp)
                buscar = tc.obtenerReturn(useCurrentDatabase,tabla,id_column)
                if buscar == False:
                    print('Encontrado')
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.CHECK)
                    tipo = TC.Tipo(useCurrentDatabase,tabla,id_column,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,tabla,id_column)
    

def procesar_listaId(instr,ts,tc,tabla):
    if instr.identificadores != []:
        for ids in instr.identificadores:
            buscar = tc.obtenerReturn(useCurrentDatabase,tabla,ids.val)
            if buscar == False:
                print('No Encontrado')
            else:
                tempA = buscar.listaCons
                tempA.append(OPCIONES_CONSTRAINT.UNIQUE)
                tipo = TC.Tipo(useCurrentDatabase,tabla,ids.val,buscar.tipo,buscar.tamanio,"","",tempA)
                tc.actualizar(tipo,useCurrentDatabase,tabla,ids.val)

def procesar_primaria(instr,ts,tc,tabla):
    global pks
    pk = []
    for ids in instr.val:
        buscar = tc.obtenerReturn(useCurrentDatabase,tabla,ids.val)
        if buscar == False:
            print('No Encontrado')
        else:
            tempA = buscar.listaCons
            tempA.append(OPCIONES_CONSTRAINT.PRIMARY)
            tipo = TC.Tipo(useCurrentDatabase,tabla,ids.val,buscar.tipo,buscar.tamanio,"","",tempA)
            tc.actualizar(tipo,useCurrentDatabase,tabla,ids.val)
            
            pos = tc.getPos(useCurrentDatabase,tabla,ids.val)
            pk.append(pos)

    pks = pk

def procesar_Foranea(instr,ts,tc,tabla):
    buscar = tc.obtenerReturn(useCurrentDatabase,tabla,instr.nombre_tabla)
    if buscar == False:
        print('No Encontrado')
    else:
        tempA = buscar.listaCons
        tempA.append(OPCIONES_CONSTRAINT.FOREIGN)
        tipo = TC.Tipo(useCurrentDatabase,tabla,instr.nombre_tabla,buscar.tipo,buscar.tamanio,instr.campo_referencia,instr.referencia_tabla,tempA)
        tc.actualizar(tipo,useCurrentDatabase,tabla,instr.nombre_tabla)

def procesar_constraint(instr,ts,tc,tabla):
    if instr.tipo == 'UNIQUE':
        if instr.opciones_constraint != []:
            temp = TS.Simbolo(instr.val,'CONSTRAINT',0,tabla)
            ts.agregar(temp)
            for ids in instr.opciones_constraint:
                buscar = tc.obtenerReturn(useCurrentDatabase,tabla,ids.val)
                if buscar == False:
                    print('No Encontrado')
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.UNIQUE)
                    tipo = TC.Tipo(useCurrentDatabase,tabla,ids.val,buscar.tipo,buscar.tamanio,ids,instr.referencia,tempA)
                    tc.actualizar(tipo,useCurrentDatabase,tabla,ids.val)
                
    elif instr.tipo == 'FOREIGN':
        if instr.opciones_constraint != []:
            temp = TS.Simbolo(instr.val,'CONSTRAINT',0,tabla)
            ts.agregar(temp)
            for ids in instr.opciones_constraint:
                buscar = tc.obtenerReturn(useCurrentDatabase,tabla,instr.columna)
                if buscar == False:
                    print('No Encontrado')
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.FOREIGN)
                    tipo = TC.Tipo(useCurrentDatabase,tabla,instr.columna,buscar.tipo,buscar.tamanio,ids,instr.referencia,tempA)
                    tc.actualizar(tipo,useCurrentDatabase,tabla,instr.columna)

    elif instr.tipo == 'CHECK':
        if instr.opciones_constraint != []:
            temp = TS.Simbolo(instr.val,'CONSTRAINT',0,tabla)
            ts.agregar(temp)
            for ids in instr.opciones_constraint:
                if type(ids.exp1) == ExpresionIdentificador:
                    buscar = tc.obtenerReturn(useCurrentDatabase,tabla,ids.exp1.val)
                    if buscar == False:
                        print('No Encontrado')
                    else:
                        tempA = buscar.listaCons
                        tempA.append(OPCIONES_CONSTRAINT.CHECK)
                        tipo = TC.Tipo(useCurrentDatabase,tabla,ids.exp1.val,buscar.tipo,buscar.tamanio,"","",tempA)
                        tc.actualizar(tipo,useCurrentDatabase,tabla,ids.exp1.val)
                else: 
                    buscar = tc.obtenerReturn(useCurrentDatabase,tabla,ids.exp2.val)
                    if buscar == False:
                        print('No Encontrado')
                    else:
                        tempA = buscar.listaCons
                        tempA.append(OPCIONES_CONSTRAINT.CHECK)
                        tipo = TC.Tipo(useCurrentDatabase,tabla,ids.exp2.val,buscar.tipo,buscar.tamanio,"","",tempA)
                        tc.actualizar(tipo,useCurrentDatabase,tabla,ids.exp2.val)
    
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
        
        result = j.dropDatabase(str(instr.nombre.val))
        global salida
        if result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "

        result1 = j.createDatabase(str(instr.nombre.val))
        if result1 == 0:
            temp1 = TS.Simbolo(instr.nombre.val,'Database',0,"")
            ts.agregar(temp1)
            salida = "\nCREATE DATABASE"
            
        elif result1 == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
    else:
        result1 = j.createDatabase(str(instr.nombre.val))
        if result1 == 0:
            salida = "\nCREATE DATABASE"
            temp1 = TS.Simbolo(instr.nombre.val,'Database',0,"")
            ts.agregar(temp1)
        elif result1 == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result1 == 2 :
            salida = "\nERROR:  database \"" + str(instr.nombre.val) +"\" already exists \nSQL state: 42P04 "

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

    result = j.dropDatabase(str(instr.val.val))

    if instr.exists == 0:
        global salida
        if result == 0:
            global salida
            salida = "\nDROP DATABASE"
            ts.deleteDatabase(instr.val.val)
            tc.eliminarDatabase(instr.val.val)
        elif result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
            print("ERROR:  internal_error \nSQL state: XX000 ")
        elif result == 2 :
            salida = "\nERROR:  database \"" + str(instr.val.val) +"\" does not exist \nSQL state: 3D000"
    else:
        if result == 0:
            salida = "\nDROP DATABASE"
        elif result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result == 2 :
            salida = "\nERROR:  database \"" + str(instr.val.val) +"\" does not exist, skipping DROP DATABASE"

def procesar_useDatabase(instr,ts,tc):
    #print(instr.val.val)
    global salida, useCurrentDatabase
    encontrado = False
    dataTables = j.showDatabases()
    for databases in dataTables:
        if databases == instr.val.val:
            encontrado = True
    
    if encontrado:
        global salida, useCurrentDatabase
        useCurrentDatabase = str(instr.val.val)
        salida = "\nYou are now connected to database  \"" + str(instr.val.val) +"\""
    else: 
        salida = "\nERROR:  database \"" + str(instr.val.val) +"\" does not exist \nSQL state: 3D000"
        useCurrentDatabase = ""
        
def procesar_alterdatabase(instr,ts,tc):
    global salida
    
    if isinstance(instr.tipo_id,ExpresionIdentificador) : 
        global salida
        print('OWNER ' + str(instr.tipo_id.val))

    elif isinstance(instr.tipo_id, ExpresionComillaSimple) : 
        print('OWNER ' + str(instr.tipo_id.val))
        
    else:
        result = j.alterDatabase(str(instr.id_tabla),str(instr.tipo_id))
        if result == 0:
            tipo = TC.Tipo(useCurrentDatabase,instr.id_tabla,instr.id_tabla,"",OPCIONES_CONSTRAINT.CHECK,None,None)
            tc.actualizarDatabase(tipo,instr.id_tabla,instr.tipo_id)
            temp1 = ts.obtener(instr.id_tabla,"")
            temp2 = TS.Simbolo(instr.tipo_id,temp1.tipo,temp1.valor,temp1.ambito)
            ts.actualizarDB(temp2,temp1.val)
            ts.actualizarDBTable(temp1.val,temp2.val)
            salida = "\nALTER DATABASE"            

        elif result == 1 :
            salida = "\nERROR:  internal_error \nSQL state: XX000 "
        elif result == 2 :
            salida = "\nERROR:  database \"" + str(instr.id_tabla) +"\" does not exist \nSQL state: 3D000"
        elif result == 3 :
            salida = "\nERROR:  database \"" + str(instr.tipo_id) +"\" alredy exists\nSQL state: 42P04"

def procesar_update(instr,ts,tc):
    print(instr.identificador.val)
    if instr.lista_update != []:
        for datos in instr.lista_update:
            print(datos.ids.val)
            print(datos.expresion.val)
    

def procesar_drop(instr,ts,tc):
    if instr.lista_ids != []:
        for datos in instr.lista_ids:
            #print(datos.val)
            result = j.dropTable(str(useCurrentDatabase),str(datos.val))
            global salida
            if result == 0:
                global salida
                salida = "\nDROP TABLE"
                ts.deleteDatabase(datos.val)
                tc.eliminarTabla(useCurrentDatabase,datos.val)
            elif result == 1 :
                salida = "\nERROR:  internal_error \nSQL state: XX000 "
            elif result == 2 :
                salida = "\nERROR:  database \"" + str(useCurrentDatabase) +"\" does not exist \nSQL state: 3D000"
            elif result == 3 :
                salida = "\nERROR:  table \"" + str(datos.val) +"\" does not exist \nSQL state: 42P01"
        

#Alter table

def procesar_altertable(instr,ts,tc):
    if instr.etiqueta == TIPO_ALTER_TABLE.ADD_CHECK:
        global salida
        if instr.expresionlogica.operador == OPERACION_LOGICA.AND or instr.expresionlogica.operador == OPERACION_LOGICA.OR: 
            print(instr.identificador)
            print(instr.expresionlogica.exp1.exp1.val)
            print(instr.expresionlogica.exp1.exp2.val)
            print(instr.expresionlogica.operador)
            print(instr.expresionlogica.exp2.exp1.val)
            print(instr.expresionlogica.exp2.exp2.val)
        else:
            print(instr.identificador)
            if isinstance(instr.expresionlogica.exp1,ExpresionIdentificador):
                print(instr.expresionlogica.exp1.val)
                buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp1.val)
                if buscar == False:
                    print('No Encontrado')
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.CHECK)
                    tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp1.val,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.expresionlogica.exp1.val)
                    
                    salida = "\nALTER TABLE" 

            elif isinstance(instr.expresionlogica.exp2,ExpresionIdentificador):
                print(instr.expresionlogica.exp2.val)
                buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp2.val)
                if buscar == False:
                    print('No Encontrado')
                else:
                    salida = "\nALTER TABLE" 
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.CHECK)
                    tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp2.val,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.expresionlogica.exp2.val)
                    salida = "\nALTER TABLE" 


    elif instr.etiqueta == TIPO_ALTER_TABLE.ADD_FOREIGN:
        buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.columnid)
        if buscar == False:
            print('No Encontrado')
        else:
            tempA = buscar.listaCons
            tempA.append(OPCIONES_CONSTRAINT.FOREIGN)
            tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.columnid,buscar.tipo,buscar.tamanio,instr.lista_campos,instr.tocolumnid,tempA)
            tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.columnid)
            salida = "\nALTER TABLE" 

    elif instr.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_CHECK:
        if instr.expresionlogica.operador == TIPO_LOGICA.AND or instr.expresionlogica.operador == TIPO_LOGICA.OR: 
            print(instr.expresionlogica.exp1.exp1.val)
            print(instr.expresionlogica.exp1.exp2.val)
            print(instr.expresionlogica.operador)
            print(instr.expresionlogica.exp2.exp1.val)
            print(instr.expresionlogica.exp2.exp2.val)
            
        else:
            temp = TS.Simbolo(instr.columnid,'CONSTRAINT',0,instr.identificador)
            ts.agregar(temp)
            if type(instr.expresionlogica.exp1) == ExpresionIdentificador:
                buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp1.val)
                if buscar == False:
                    print('No Encontrado')
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.CHECK)
                    tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp1.val,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.expresionlogica.exp1.val)
                    salida = "\nALTER TABLE" 
            else:
                print(instr.expresionlogica.exp1.val)
                print(instr.expresionlogica.exp2.val)
                buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp2.val)
                if buscar == False:
                    print('No Encontrado')
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.CHECK)
                    tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.expresionlogica.exp2.val,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.expresionlogica.exp2.val)
                    salida = "\nALTER TABLE" 

    elif instr.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_UNIQUE:
        print(instr.identificador)
        print(instr.columnid)
        if instr.lista_campos != []:
            temp = TS.Simbolo(instr.columnid,'CONSTRAINT',0,instr.identificador)
            ts.agregar(temp)
            
            for datos in instr.lista_campos:
                print(datos.val)
                buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,datos.val)
                if buscar == False:
                    print('Encontrado')
                else:
                    tempA = buscar.listaCons
                    tempA.append(OPCIONES_CONSTRAINT.UNIQUE)
                    tipo = TC.Tipo(useCurrentDatabase,instr.identificador,datos.val,buscar.tipo,buscar.tamanio,"","",tempA)
                    tc.actualizar(tipo,useCurrentDatabase,instr.identificador,datos.val)
                    salida = "\nALTER TABLE" 

    elif instr.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_FOREIGN:
        temp = TS.Simbolo(instr.columnid,'CONSTRAINT',0,instr.identificador)
        ts.agregar(temp)
        buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.tocolumnid)
        if buscar == False:
            print('No Encontrado')
        else:
            tempA = buscar.listaCons
            tempA.append(OPCIONES_CONSTRAINT.FOREIGN)
            tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.tocolumnid,buscar.tipo,buscar.tamanio,instr.lista_ref,instr.lista_campos,tempA)
            tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.tocolumnid)
            salida = "\nALTER TABLE" 
        

        salida = "\nALTER TABLE" 

    elif instr.etiqueta == TIPO_ALTER_TABLE.ALTER_COLUMN:
        print(instr.identificador)
        if instr.lista_campos != []:
            for lista in instr.lista_campos:
                print(lista.identificador.val)
                print(lista.tipo.val)
                print(lista.par1)

                tipodatoo = TIPO_DE_DATOS.text_ 
                tamanioD = ""
                if lista.tipo.val.upper() == 'TEXT':
                    tipodatoo = TIPO_DE_DATOS.text_ 
                    tamanioD = ""
                elif lista.tipo.val.upper() == 'FLOAT':
                    tipodatoo = TIPO_DE_DATOS.float_ 
                elif lista.tipo.val.upper() == 'INTEGER':
                    tipodatoo = TIPO_DE_DATOS.integer_ 
                    tamanioD = ""
                elif lista.tipo.val.upper() == 'SMALLINT':
                    tipodatoo = TIPO_DE_DATOS.smallint_ 
                elif lista.tipo.val.upper() == 'MONEY':
                    tipodatoo = TIPO_DE_DATOS.money 
                elif lista.tipo.val.upper() == 'BIGINT':
                    tipodatoo = TIPO_DE_DATOS.bigint 
                elif lista.tipo.val.upper() == 'REAL':
                    tipodatoo = TIPO_DE_DATOS.real 
                elif lista.tipo.val.upper() == 'DOUBLE':
                    tipodatoo = TIPO_DE_DATOS.double 
                elif lista.tipo.val.upper() == 'INTERVAL':
                    tipodatoo = TIPO_DE_DATOS.interval 
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'TIME':
                    tipodatoo = TIPO_DE_DATOS.time 
                elif lista.tipo.val.upper() == 'TIMESTAMP':
                    tipodatoo = TIPO_DE_DATOS.timestamp 
                elif lista.tipo.val.upper() == 'DATE':
                    tipodatoo = TIPO_DE_DATOS.date 
                elif lista.tipo.val.upper() == 'VARYING':
                    tipodatoo = TIPO_DE_DATOS.varying 
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'VARCHAR':
                    tipodatoo = TIPO_DE_DATOS.varchar 
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'CHAR':
                    tipodatoo = TIPO_DE_DATOS.char 
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'CHARACTER':
                    tipodatoo = TIPO_DE_DATOS.character 
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'DECIMAL':
                    tipodatoo = TIPO_DE_DATOS.decimal 
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'NUMERIC':
                    tipodatoo = TIPO_DE_DATOS.numeric           
                    tamanioD = lista.par1
                elif lista.tipo.val.upper() == 'DOUBLE':
                    tipodatoo = TIPO_DE_DATOS.double_precision

                buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,lista.identificador.val)
                if buscar == False:
                    print('No Encontrado')
                else:
                    tipo = TC.Tipo(useCurrentDatabase,instr.identificador,lista.identificador.val,buscar.tipo,tamanioD,buscar.referencia,buscar.tablaRef,buscar.listaCons)
                    tc.actualizar(tipo,useCurrentDatabase,instr.identificador,lista.identificador.val)
                    salida = "\nALTER TABLE"
    
    elif instr.etiqueta == TIPO_ALTER_TABLE.ALTER_COLUMN_NULL:
        #print(instr.identificador,instr.columnid)
        
        buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.columnid)
        if buscar == False:
            print('No Encontrado')
        else:
            tempA = buscar.listaCons
            tempA.append(OPCIONES_CONSTRAINT.NULL)
            tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.columnid,buscar.tipo,buscar.tamanio,"","",tempA)
            tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.columnid)
            salida = "\nALTER TABLE"   

    elif instr.etiqueta == TIPO_ALTER_TABLE.ALTER_COLUMN_NOT_NULL:
        buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,instr.columnid)
        if buscar == False:
            print('No Encontrado')
        else:
            tempA = buscar.listaCons
            tempA.append(OPCIONES_CONSTRAINT.NOT_NULL)
            tipo = TC.Tipo(useCurrentDatabase,instr.identificador,instr.columnid,buscar.tipo,buscar.tamanio,"","",tempA)
            tc.actualizar(tipo,useCurrentDatabase,instr.identificador,instr.columnid)
            salida = "\nALTER TABLE"        
    
    elif instr.etiqueta ==  TIPO_ALTER_TABLE.DROP_CONSTRAINT:
        print(instr.identificador)
        if instr.lista_campos != []:
            for datos in instr.lista_campos:
                print(datos.val)
                ts.deleteConstraint(datos.val,instr.identificador)
            salida = "\nALTER TABLE" 

    elif instr.etiqueta ==  TIPO_ALTER_TABLE.RENAME_COLUMN:
        # NO EXISTE :(
        print(instr.identificador)
        print(instr.columnid)
        print(instr.tocolumnid)
        salida = "\nALTER TABLE" 
    
    elif instr.etiqueta == TIPO_ALTER_TABLE.DROP_COLUMN:
        #print('Tabla',instr.identificador)
        if instr.lista_campos != []:
            for datos in instr.lista_campos:
                #print('Columna',datos.val)
                
                pos = tc.getPos(useCurrentDatabase,instr.identificador,datos.val)
                print(pos)
                #result = j.alterDropColumn('world','countries',1)
                #print(result)
                result = 0
                if result == 0:
                    tc.eliminarID(useCurrentDatabase,instr.identificador,datos.val)
                    temp1 = ts.obtener(instr.identificador,useCurrentDatabase)
                    temp2 = TS.Simbolo(temp1.val,temp1.tipo,temp1.valor-1,temp1.ambito)
                    ts.actualizarDB(temp2,instr.identificador)
                    salida = "\nALTER TABLE"            
                    print(salida)

                elif result == 1 :
                    salida = "\nERROR:  internal_error \nSQL state: XX000 "
                elif result == 2 :
                    salida = "\nERROR:  database \"" + str(useCurrentDatabase) +"\" does not exist \nSQL state: 3D000"
                elif result == 3 :
                    salida = "\nERROR:  relation \"" + str(instr.identificador) +"\" does not exist\nSQL state: 42P01"
                elif result == 4 :
                    salida = "\nERROR:  key cannot be removed\nSQL state: 42P04"
                elif result == 5 :
                    salida = "\nERROR:  column out of bounds\nSQL state: 42P05"

                

    elif instr.etiqueta ==  TIPO_ALTER_TABLE.ADD_COLUMN:
        tipodatoo = TIPO_DE_DATOS.text_ 
        tamanioD = ""
        if instr.lista_campos[0].tipo.val.upper() == 'TEXT':
            tipodatoo = TIPO_DE_DATOS.text_ 
            tamanioD = ""
        elif instr.lista_campos[0].tipo.val.upper() == 'FLOAT':
            tipodatoo = TIPO_DE_DATOS.float_ 
        elif instr.lista_campos[0].tipo.val.upper() == 'INTEGER':
            tipodatoo = TIPO_DE_DATOS.integer_ 
            tamanioD = ""
        elif instr.lista_campos[0].tipo.val.upper() == 'SMALLINT':
            tipodatoo = TIPO_DE_DATOS.smallint_ 
        elif instr.lista_campos[0].tipo.val.upper() == 'MONEY':
            tipodatoo = TIPO_DE_DATOS.money 
        elif instr.lista_campos[0].tipo.val.upper() == 'BIGINT':
            tipodatoo = TIPO_DE_DATOS.bigint 
        elif instr.lista_campos[0].tipo.val.upper() == 'REAL':
            tipodatoo = TIPO_DE_DATOS.real 
        elif instr.lista_campos[0].tipo.val.upper() == 'DOUBLE':
            tipodatoo = TIPO_DE_DATOS.double 
        elif instr.lista_campos[0].tipo.val.upper() == 'INTERVAL':
            tipodatoo = TIPO_DE_DATOS.interval 
            tamanioD = instr.lista_campos[0].par1
        elif instr.lista_campos[0].tipo.val.upper() == 'TIME':
            tipodatoo = TIPO_DE_DATOS.time 
        elif instr.lista_campos[0].tipo.val.upper() == 'TIMESTAMP':
            tipodatoo = TIPO_DE_DATOS.timestamp 
        elif instr.lista_campos[0].tipo.val.upper() == 'DATE':
            tipodatoo = TIPO_DE_DATOS.date 
        elif instr.lista_campos[0].tipo.val.upper() == 'VARYING':
            tipodatoo = TIPO_DE_DATOS.varying 
            tamanioD = instr.lista_campos[0].par1
        elif instr.lista_campos[0].tipo.val.upper() == 'VARCHAR':
            tipodatoo = TIPO_DE_DATOS.varchar 
            tamanioD = instr.lista_campos[0].par1
        elif instr.lista_campos[0].tipo.val.upper() == 'CHAR':
            tipodatoo = TIPO_DE_DATOS.char 
            tamanioD = instr.lista_campos[0].par1
        elif instr.lista_campos[0].tipo.val.upper() == 'CHARACTER':
            tipodatoo = TIPO_DE_DATOS.character 
            tamanioD = instr.lista_campos[0].par1
        elif instr.lista_campos[0].tipo.val.upper() == 'DECIMAL':
            tipodatoo = TIPO_DE_DATOS.decimal 
            tamanioD = instr.lista_campos[0].par1
        elif instr.lista_campos[0].tipo.val.upper() == 'NUMERIC':
            tipodatoo = TIPO_DE_DATOS.numeric           
            tamanioD = instr.lista_campos[0].par1 
        elif instr.lista_campos[0].tipo.val.upper() == 'DOUBLE':
            tipodatoo = TIPO_DE_DATOS.double_precision
        
        if instr.lista_campos != []:
            for datos in instr.lista_campos:
                result = j.alterAddColumn(str(useCurrentDatabase),str(instr.identificador),1)
                if result == 0:
                    buscar = tc.obtenerReturn(useCurrentDatabase,instr.identificador,datos.identificador.val)
                    if buscar == False:
                        tipo = TC.Tipo(useCurrentDatabase,instr.identificador,datos.identificador.val,tipodatoo,tamanioD,"","",[])
                        tc.agregar(tipo)
                    else:
                        print('New')
                    
                    temp1 = ts.obtener(instr.identificador,useCurrentDatabase)
                    temp2 = TS.Simbolo(temp1.val,temp1.tipo,temp1.valor+1,temp1.ambito)
                    ts.actualizarDB(temp2,instr.identificador)
                    salida = "\nALTER TABLE"            

                elif result == 1 :
                    salida = "\nERROR:  internal_error \nSQL state: XX000 "
                elif result == 2 :
                    salida = "\nERROR:  database \"" + str(useCurrentDatabase) +"\" does not exist \nSQL state: 3D000"
                elif result == 3 :
                    salida = "\nERROR:  relation \"" + str(instr.tipo_id) +"\" does not exist\nSQL state: 42P01"
                
                


#INSERT
def procesar_insert(instr,ts,tc):
    # tabla -> print(instr.val)
    
    global salida
    columns = tc.obtenerColumns(useCurrentDatabase,instr.val)
    numC = len(columns)
    arrayInsert = []
    arrayInserteFinal = []
    arrayParametros = []
    if instr.etiqueta == TIPO_INSERT.CON_PARAMETROS:

        if instr.lista_parametros != []:
            for parametros in instr.lista_parametros:
                #print(parametros.val)
                typeC = tc.obtenerReturn(useCurrentDatabase,instr.val,parametros.val)
                #print('tc',typeC.val)
                arrayParametros.append(typeC.val)

        if instr.lista_datos != []:
            for parametros in instr.lista_datos:
                if isinstance(parametros, ExpresionIdentificador):
                    #print(parametros.val)
                    arrayInsert.append(parametros.val)
                elif isinstance(parametros, ExpresionEntero):
                    #print(parametros.val) 
                    arrayInsert.append(parametros.val)

        arrayNew = []           
        ar = 0
        while ar < len(columns):
            if ar < len(arrayInsert):
                arrayNew.append([arrayParametros[ar],arrayInsert[ar]])
            else:
                arrayNew.append([None,None])
            ar+=1

        
        arrayNone = []
        ii = 0
        jj = 0
        while ii < len(columns):
            iii = 0
            arrPP = []
            while iii < len(arrayNew):
                arrPP.append(arrayNew[iii][0])
                iii+=1
            if columns[ii] in arrPP:
                arrayNone.append(arrayNew[jj][1])
                jj+=1
            else:
                arrayNone.append(None)
            ii+=1

        #print(columns)
        #print(arrayNone)

        if len(arrayNone) == numC:
            i = 0
            while i < numC:
                restricciones = []
                it = 0
                typeC = tc.obtenerReturn(useCurrentDatabase,instr.val,columns[i])

                while it < len(typeC.listaCons):
                    restricciones.append(typeC.listaCons[it])
                    it+=1
                #print(typeC.val,typeC.tamanio,restricciones)

                insertBool = False
                if restricciones != []:
                    for res in restricciones:
                        if res == OPCIONES_CONSTRAINT.CHECK:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.UNIQUE:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.FOREIGN:
                            if arrayNone[i] == None:
                                insertBool = False
                            else:
                                insertBool = True
                        if res == OPCIONES_CONSTRAINT.NULL:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.NOT_NULL:
                            if arrayNone[i] == None:
                                insertBool = False
                            else:
                                insertBool = True
                        if res == OPCIONES_CONSTRAINT.DEFAULT:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.PRIMARY:
                            if arrayNone[i] == None:
                                insertBool = False
                            else:
                                insertBool = True
                else:
                    insertBool = True

                
                if insertBool:
                    arrayInserteFinal.append(arrayNone[i])

                i+=1 
            #print(arrayInserteFinal)

        elif len(arrayInsert) > numC:
            salida = "\nERROR:  INSERT has more expressions than target columns\nSQL state: 42601"
            print(salida)
       
    else:
        if instr.lista_datos != []:
            #print(columns)
            #print(numC)
            for parametros in instr.lista_datos:
                if isinstance(parametros, ExpresionIdentificador):
                    arrayInsert.append(parametros.val)
                elif isinstance(parametros, ExpresionEntero):
                    arrayInsert.append(parametros.val)

        # LLENAR CAMPOS CON None
        if len(arrayInsert) < numC:
            i = len(arrayInsert)
            while i < numC:
                arrayInsert.append(None)
                i+=1

        if len(arrayInsert) == numC:
            i = 0
            while i < numC:
                restricciones = []
                it = 0
                typeC = tc.obtenerReturn(useCurrentDatabase,instr.val,columns[i])

                while it < len(typeC.listaCons):
                    restricciones.append(typeC.listaCons[it])
                    it+=1
                #print(typeC.val,typeC.tamanio,restricciones)

                insertBool = False
                if restricciones != []:
                    for res in restricciones:
                        if res == OPCIONES_CONSTRAINT.CHECK:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.UNIQUE:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.FOREIGN:
                            if arrayInsert[i] == None:
                                insertBool = False
                            else:
                                insertBool = True
                        if res == OPCIONES_CONSTRAINT.NULL:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.NOT_NULL:
                            if arrayInsert[i] == None:
                                insertBool = False
                            else:
                                insertBool = True
                        if res == OPCIONES_CONSTRAINT.DEFAULT:
                            insertBool = True
                        if res == OPCIONES_CONSTRAINT.PRIMARY:
                            if arrayInsert[i] == None:
                                insertBool = False
                            else:
                                insertBool = True
                else:
                    insertBool = True

                
                if insertBool:
                    arrayInserteFinal.append(arrayInsert[i])

                i+=1 
            #print(arrayInserteFinal)

        elif len(arrayInsert) > numC:
            salida = "\nERROR:  INSERT has more expressions than target columns\nSQL state: 42601"
            print(salida)


    #FUNCION INSERTAR
    '''print(arrayInserteFinal)
    print(str(useCurrentDatabase),str(instr.val), arrayInserteFinal)'''

    result = j.insert(useCurrentDatabase,instr.val, arrayInserteFinal)

    if result == 0:
        salida = "\nINSERT 0 1"            
    elif result == 1 :
        salida = "\nERROR:  internal_error \nSQL state: XX000 "
    elif result == 2 :
        salida = "\nERROR:  database \"" + str(useCurrentDatabase) +"\" does not exist \nSQL state: 3D000"
    elif result == 3 :
        salida = "\nERROR:  relation \"" + str(instr.val) +"\" does not exist\nSQL state: 42P01"
    elif result == 4:
        salida = "\nERROR:  duplicate key value violates unique constraint \"" + str(instr.val) + "_pkey\"\nSQL state: 23505"
    elif result == 5:
        salida = "\nERROR:  INSERT has more expressions than target columns\nSQL state: 42601"

    #print(salida)

    


    

#Enum
def procesar_create_type(instr,ts,tc):
    
    print("TYPE------------------------------")
    print(instr.identificador.val)
    if instr.lista_datos != []:
        for datos in instr.lista_datos:
            print(datos.val)

#delete
def procesar_delete(instr,ts,tc):
    if instr.etiqueta == TIPO_DELETE.DELETE_NORMAL:
        print(instr.val)

    elif instr.etiqueta == TIPO_DELETE.DELETE_RETURNING:
        print(instr.val)
        if instr.returning != []:
            for retornos in instr.returning:
                print(retornos.etiqueta)

    elif instr.etiqueta == TIPO_DELETE.DELETE_EXIST:    
        if instr.expresion.operador == OPERACION_RELACIONAL.MAYQUE:
            if instr.expresion.exp1.etiqueta == TIPO_VALOR.IDENTIFICADOR and instr.expresion.exp2.etiqueta ==  TIPO_VALOR.NUMERO:
                print(instr.expresion.exp1.val)
                print(instr.expresion.exp2.val)            

   
    elif instr.etiqueta == TIPO_DELETE.DELETE_EXIST_RETURNING:
        
        print(instr.val)

        if instr.expresion.operador == OPERACION_RELACIONAL.MAYQUE:
            if instr.expresion.exp1.etiqueta == TIPO_VALOR.IDENTIFICADOR and instr.expresion.exp2.etiqueta ==  TIPO_VALOR.NUMERO:
                print(instr.expresion.exp1.val)
                print(instr.expresion.exp2.val)

        if instr.returning != []:
            for retornos in instr.returning:
                print(retornos.etiqueta)

        
    elif instr.etiqueta == TIPO_DELETE.DELETE_CONDIFION:
        print(instr.val, instr.expresion)
    
    elif instr.etiqueta == TIPO_DELETE.DELETE_CONDICION_RETURNING:
        if instr.returning != []:
            for retornos in instr.returning:
                print(instr.val,instr.expresion, retornos.val)

    elif instr.etiqueta == TIPO_DELETE.DELETE_USING:
        print(instr.val, instr.id_using, instr.expresion)

    elif instr.etiqueta == TIPO_DELETE.DELETE_USING_returnin:
        if instr.returning != []:
            for retornos in instr.returning:
                print(instr.val,instr.id_using,instr.expresion)

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
                    #print(useCurrentDatabase)
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
            elif isinstance(instr,Create_update) : 
                procesar_update(instr,ts,tc)
            elif isinstance(instr, Crear_Drop) : 
                if useCurrentDatabase != "":
                    procesar_drop(instr,ts,tc)
                else:
                    salida = "\nSELECT DATABASE"
            elif isinstance(instr, Crear_altertable) :
                if useCurrentDatabase != "":
                    procesar_altertable(instr,ts,tc)
                else:
                    salida = "\nSELECT DATABASE"
            elif isinstance(instr, Definicion_Insert) :
                procesar_insert(instr,ts,tc)
            elif isinstance(instr, Create_type) :
                procesar_create_type(instr,ts,tc)
            elif isinstance(instr, Definicion_delete) :
                procesar_delete(instr,ts,tc)
            
            
            else : print('Error: instrucción no válida ' + str(instr))
        return salida 
    except:
        pass

f = open("./entrada.txt", "r")
input = f.read()
instrucciones = g.parse(input)

if listaErrores == []:
    instrucciones_Global = instrucciones
    ts_global = TS.TablaDeSimbolos()
    tc_global = TC.TablaDeTipos()
    procesar_instrucciones(instrucciones,ts_global,tc_global)
    typeC = TipeChecker()
    typeC.crearReporte(tc_global)
    typeS = RTablaDeSimbolos()
    typeS.crearReporte(ts_global)
    astt = AST()
    astt.generarAST(instrucciones)
else:
    erroressss = ErrorHTML()
    erroressss.crearReporte()
    listaErrores = []

