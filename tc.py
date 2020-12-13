
class Tipo() :
    'Esta clase representa un tipo dentro de nuestra tabla de tipos'

    def __init__(self, id, tipo, valor) :
        self.id = id
        self.tipo = tipo
        self.valor = valor

class TablaDeTipos() :
    'Esta clase representa la tabla de tipos'

    def __init__(self, tipos = {}) :
        self.tipos = tipos

    def agregar(self, tipo) :
        self.tipos[tipo.id] = tipo
    
    def obtener(self, id) :
        if not id in self.tipos :
            print('Error: variable ', id, ' no definida.')

        return self.tipos[id]

    def actualizar(self, tipo) :
        if not tipo.id in self.tipos :
            print('Error: variable ', tipo.id, ' no definida.')
        else :
            self.tipos[tipo.id] = tipo

    def clear(self):
        self.tipos = {}