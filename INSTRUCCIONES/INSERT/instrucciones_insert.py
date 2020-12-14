class Instruccion:
    pass

class Definicion_Insert(Instruccion):
    def __init__(self, id, etiqueta ,lista_parametros = [], lista_datos = []):
        self.id = id
        self.etiqueta = etiqueta
        self.lista_parametros = lista_parametros
        self.lista_datos = lista_datos