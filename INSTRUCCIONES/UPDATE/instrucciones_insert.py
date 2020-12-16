class Instruccion:
    pass

class Definicion_Insert(Instruccion):
    def __init__(self, id, etiqueta ,lista_parametros = [], lista_datos = []):
        self.id = id
        self.etiqueta = etiqueta
        self.lista_parametros = lista_parametros
        self.lista_datos = lista_datos

class Create_update(Instruccion):
    def __init__(self,identificador,expresion,lista_update = []):
        self.identificador = identificador
        self.lista_update = lista_update
        self.expresion = expresion

class Create_Parametro_update(Instruccion):
    def __init__(self,ids,expresion):
        self.ids = ids
        self.expresion = expresion