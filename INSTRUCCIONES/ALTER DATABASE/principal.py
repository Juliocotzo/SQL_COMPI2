import gramat as g
from expresiones import *
from instrucciones import *

def procesar_createTable(instr) :
    print('Crear Tabla Normal')
    if instr.intrucc != []:
        procesar_instrucciones(instr.intrucc)

def procesar_createTable_Herencia(instr) :
    print('Crear Tabla con herencia')

def procesar_Definicion(instr) :
    print('Definicion')

def procesar_primarykey(instr):
    print('LLave Primaria')

def procesar_references(instr):
    print('Referencia')

def procesar_null_notnull(instr):
    print('Tiene null')

def procesar_Foranea(instr):
    print('Tiene Foranea')


def procesar_constraint(instr):
    print('Constraint')
    if instr.instrucciones != []:
        procesar_instrucciones(instr.instrucciones)
        print(procesar_Expresion_logica(instr))

def procesar_check(instr):
    print('Check')


def procesar_Expresion_Relacional(instr):
    print('Expresion Relacional')

def procesar_Expresion_Binaria(instr):
    print('Expresion Binaria')

def procesar_Expresion_logica(instr):
    pass

def resolver_expresion_aritmetica(expNum):
    if isinstance(expNum, ExpresionBinaria):
        pass
def procesar_Expresion_Numerica(instr):
    print('Entero')

# PROCESAR DROP
def procesar_drop(instr):
    print('Drop')
    if instr.lista_ids != []:
        for ids in instr.lista_ids:
            print("     "+ids.id)

# PROCESAR USE DATABASE
def procesar_usedatabase(instr):
    print('Use Database: '+ instr.idbase)

def procesar_creartype(instr):
    print('CREATE TYPE ' + instr.identificador)
    if instr.lista_datos != []:
        for cadenas in instr.lista_datos:
            print("     "+cadenas.val)

def procesar_alterdatabase(instr):
    global salida
    #print(instr.tipo_id)
    if isinstance(instr.tipo_id, ExpresionComillaSimple):
        print(instr.tipo_id.val)
    salida = "hola"
    # print('AlterBase: '+ instr.id_tabla + " to " + str(instr.tipo_id))

def procesar_update(instr):
    print('update ' + instr.identificador + " tabla2: "+ instr.idtabla + " expresion: " + str(instr.expresion.exp1))

def procesar_parametro_update(instr):
    print('parametros update')

def procesar_altertable_drop(instr):
    print('Alter table drop')

def procesar_altertable_rename(instr):
    print('Alter table rename')

def procesar_altertable_simple(instr):
    print('Alter table simple')
    if instr.lista_alter != []:
        print(instr.lista_alter[1].tipodato.id)
        print(instr.lista_alter[0].tipodato.id)

def procesar_subalter_simple(instr):
    print('Sub alter table simple')

def procesar_alteradd_colum(instr):
    print('ALTERTABLE ADD')
    if instr.lista_add != []:
        print(instr.lista_add[1].tipodato[0].id)

def procesar_addcolumna(instr):
    print('add columna')

def procesar_addalter_foreign(instr):
    print('add foreign key ')

def procesar_addalter_check(instr):
    print('add alter check')
    print(instr.ids)

def procesar_const_check(instr):
    print('constraint check')

def procesar_const_unique(instr):
    print('constraint unique')

def procesar_const_foreign(instr):
    print('constraint foreign key')

def procesar_select(instr):
    print('Mostrar select')
    print(instr.ids)
    print(instr.asid)
    if instr.lista2 != []:
        print(instr.lista2)

def procesar_distinct(instr):
    print('Mostrar distinct')

def procesar_uniones_select(instr):
    print('Mostrar tipo select union ')
    print(instr.izquierda.ids)
    print(instr.derecha.ids)

def procesar_opciones_select(instr):
    print('UNA FUNCION ' + str(instr.cadena))

def procesar_case(instr):
    print('Se creo un case')


def procesar_instrucciones(instrucciones) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if isinstance(instr, CrearTable) : procesar_createTable(instr)
        elif isinstance(instr, CrearTable_Herencia) : procesar_createTable_Herencia(instr)
        elif isinstance(instr, Definicion) : procesar_Definicion(instr)
        elif isinstance(instr, Definicion_primaria) : procesar_primarykey(instr)
        elif isinstance(instr, Definicion_references) : procesar_references(instr)
        elif isinstance(instr, Definicion_nulla) : procesar_null_notnull(instr)
        elif isinstance(instr, Definicon_Foranea) : procesar_Foranea(instr)
        elif isinstance(instr, Definicion_contraint) : procesar_constraint(instr)
        elif isinstance(instr, Definicion_check) : procesar_check(instr)
        elif isinstance(instr, ExpresionRelacional) : procesar_Expresion_Relacional(instr)
        elif isinstance(instr, ExpresionBinaria) : procesar_Expresion_Binaria(instr)
        elif isinstance(instr, ExpresionLogica) : procesar_Expresion_logica(instr)
        elif isinstance(instr, Crear_Drop) : procesar_drop(instr)
        elif isinstance(instr, Use_DB) : procesar_usedatabase(instr)
        elif isinstance(instr, Create_type) : procesar_creartype(instr)
        elif isinstance(instr, Create_Alterdatabase) : procesar_alterdatabase(instr)
        elif isinstance(instr, Create_update) : procesar_update(instr)
        elif isinstance(instr, Create_Parametro_update) : procesar_parametro_update(instr)
        elif isinstance(instr, Create_altertable_drop) : procesar_altertable_drop(instr)
        elif isinstance(instr, Create_altertable_rename) : procesar_altertable_rename(instr)
        elif isinstance(instr, Create_altertable_simple) : procesar_altertable_simple(instr)
        elif isinstance(instr, Create_sub_altersimple) : procesar_subalter_simple(instr)
        elif isinstance(instr, Create_altertable_addcolumn) : procesar_alteradd_colum(instr)
        elif isinstance(instr, Create_addcolumna) : procesar_addcolumna(instr)
        elif isinstance(instr, Create_addforeign) : procesar_addalter_foreign(instr)
        elif isinstance(instr, Create_addcheck) : procesar_addalter_check(instr)
        elif isinstance(instr, Create_const_check) : procesar_const_check(instr)
        elif isinstance(instr, Create_const_unique) : procesar_const_unique(instr)
        elif isinstance(instr, Create_const_foreign) : procesar_const_foreign(instr)
        # PARA EL SELECT
        elif isinstance(instr, Create_select) : procesar_select(instr)
        elif isinstance(instr, Create_s_distinct) : procesar_distinct(instr)
        elif isinstance(instr, Create_uniones_select) : procesar_uniones_select(instr)
        elif isinstance(instr, opciones_cuerpo_select) : procesar_opciones_select(instr)
        elif isinstance(instr, Create_case) : procesar_case(instr)
        else : print('Error: instrucción no válida')

f = open("./entrada.txt", "r")
input = f.read()

instrucciones = g.parse(input)
procesar_instrucciones(instrucciones)