class Instruccion:
    ''' Esta sera la clase de Instrucciones '''

class CrearTable(Instruccion):

    def __init__(self, nombre_tabla  ,intrucc = []):
        self.intrucc = intrucc
        self.nombre_tabla = nombre_tabla

class CrearTable_Herencia(Instruccion): 
    def __init__(self,nombre_tabla, herencia  ,intrucc = []):
        self.intrucc = intrucc
        self.nombre_tabla = nombre_tabla
        self.herencia = herencia

class Definicion(Instruccion):
    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id

class Definicion_primaria(Instruccion):
    def __init__(self, tipo, id, tipo_definicion):
        self.tipo = tipo
        self.id = id
        self.tipo_definicion = tipo_definicion

class Definicion_references(Instruccion):
    def __init__(self, id, tipo, tipo_definicion, id_referencia):
        self.id = id
        self.tipo = tipo
        self.tipo_definicion = tipo_definicion
        self.id_referencia = id_referencia

class Definicion_nulla(Instruccion):
    def __init__(self, id, tipo, null_notnull):
        self.id = id
        self.tipo = tipo
        self.null_notnull = null_notnull

class Definicon_Foranea(Instruccion):
    def __init__(self, nombre_tabla, referencia_tabla , campo_referencia):
        self.nombre_tabla = nombre_tabla
        self.referencia_tabla = referencia_tabla
        self.campo_referencia = campo_referencia

class Definicion_contraint(Instruccion):
    def __init__(self, id, instrucciones = []):
        self.id = id
        self.instrucciones = instrucciones

class Definicion_check(Instruccion):
    def __init__(self, exp_logica = []):
        self.exp_logica = exp_logica

class Definicion_unique(Instruccion):
    def __init__(self, identificadores = []):
        self.identificadores = identificadores

class Etiqueta_tipo(Instruccion):
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta

class Etiqueta_Interval(Instruccion):
    def __init__(self,ext_time, ext_time1,etiqueta):
        self.ext_time = ext_time
        self.ext_time1 = ext_time1
        self.etiqueta = etiqueta

class Crear_Drop(Instruccion):
    def __init__(self, lista_ids = []):
        self.lista_ids = lista_ids

class Use_DB(Instruccion):
    def __init__(self, idbase):
        self.idbase = idbase

class Create_type(Instruccion):
    def __init__(self,identificador,lista_datos = []):
        self.identificador = identificador
        self.lista_datos = lista_datos

class Create_Alterdatabase(Instruccion):
    def __init__(self,id_tabla, tipo_id):
        self.id_tabla = id_tabla
        self.tipo_id = tipo_id

class Create_update(Instruccion):
    def __init__(self,identificador,idtabla,expresion,lista_update = []):
        self.identificador = identificador
        self.lista_update = lista_update
        self.idtabla = idtabla
        self.expresion = expresion

class Create_Parametro_update(Instruccion):
    def __init__(self,ids,expresion):
        self.ids = ids
        self.expresion = expresion

#ALTERS 
class Create_altertable_drop(Instruccion):
    def __init__(self,identificador, lista_campos = []):
        self.identificador = identificador
        self.lista_campos = lista_campos

class Create_altertable_rename(Instruccion):
    def __init__(self,identificador,id1,id2):
        self.identificador = identificador
        self.id1 = id1
        self.id2 = id2

class Create_altertable_simple(Instruccion):
    def __init__(self,identificador, lista_alter = []):
        self.identificador = identificador
        self.lista_alter = lista_alter

class Create_sub_altersimple(Instruccion):
    def __init__(self,identificador,tipodato,tamano,tamano2):
        self.identificador =  identificador
        self.tipodato = tipodato
        self.tamano = tamano
        self.tamano2 = tamano2

# ALTER ADDS
class Create_altertable_addcolumn(Instruccion):
    def __init__(self,identificador,lista_add = []):
        self.identificador = identificador
        self.lista_add = lista_add

class Create_addcolumna(Instruccion):
    def __init__(self,ids,tipodato):
        self.ids = ids
        self.tipodato = tipodato

class Create_addforeign(Instruccion):
    def __init__(self,ids,listaids = [],listaref = []):
        self.ids = ids
        self.listaids = listaids
        self.listaref = listaref

class Create_addcheck(Instruccion):
    def __init__(self,ids,listaexp = []):
        self.ids = ids
        self.listaexp = listaexp

#CONSTRAINTS
class Create_const_check(Instruccion):
    def __init__(self,ids,tabid,lista_exp = []):
        self.ids = ids
        self.tabid = tabid
        self.lista_exp = lista_exp

class Create_const_unique(Instruccion):
    def __init__(self,ids,tabid,listac = []):
        self.ids = ids
        self.tabid = tabid
        self.listac = listac

class Create_const_foreign(Instruccion):
    def __init__(self,ids,tabid,listac = [],listaref = []):
        self.ids = ids
        self.tabid = tabid
        self.listac = listac
        self.listaref = listaref


# PARA EL SELECT
class Create_s_distinct(Instruccion):
    def __init__(self,etiqueta,listac = []):
        self.etiqueta = etiqueta
        self.listac =  listac

class Create_select(Instruccion):
    def __init__(self,ids,asid,lista2 = []):
        self.ids = ids
        self.asid = asid
        self.lista2 = lista2

class Create_uniones_select(Instruccion):
    def __init__(self, izquierda,derecha,tipo):
        self.izquierda = izquierda
        self.derecha = derecha
        self.tipo = tipo

class opciones_cuerpo_select(Instruccion):
    def __init__(self, etiqueta, cadena,cadena2):
        self.etiqueta = etiqueta
        self.cadena = cadena
        self.cadena2 = cadena2

# PARA EL CASE 
class Create_case(Instruccion):
    def __init__(self,expresion, lista_exp = []):
        self.expresion =  expresion
        self.lista_exp = lista_exp

class Create_when(Instruccion):
    def __init__(self,expresion, sentencia):
        self.expresion =  expresion
        self.sentencia = sentencia
