
class Instruccion:
    ''' Esta sera la clase de Instrucciones '''


class CrearTable(Instruccion):

    def __init__(self, nombre_tabla, intrucc = []):
        self.intrucc = intrucc
        self.nombre_tabla = nombre_tabla


class CrearTable_Herencia(Instruccion):

    def __init__(self,nombre_tabla, herencia, intrucc = []):
        self.intrucc = intrucc
        self.nombre_tabla = nombre_tabla
        self.herencia = herencia

class Definicion(Instruccion):
    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id