
class Tipo() :
    'Esta clase representa un tipo dentro de nuestra tabla de tipos'

    def __init__(self, database, tabla, id, tipo, restriccion, referencia, tablaRef, listaCons = []) :
        self.database = database
        self.tabla = tabla
        self.id = id
        self.tipo = tipo
        self.restriccion = restriccion
        self.referencia = referencia
        self.tablaRef = tablaRef
        self.listaCons = listaCons

class TablaDeTipos() :
    'Esta clase representa la tabla de tipos'

    def __init__(self, tipos = []) :
        self.tipos = tipos

    def agregar(self, tipo) :
        self.tipos.append(tipo)
    
    def obtener(self, id) :
        if not id in self.tipos :
            print('Error: variable ', id, ' no definida.')

        return self.tipos[id]

    def obtenerReturn(self,database,tabla,column) :
        i = 0
        while i < len(self.tipos):
            if self.tipos[i].database == database and self.tipos[i].tabla == tabla and self.tipos[i].id == column:
                return self.tipos[i]
            i += 1
        return False

    def actualizar(self,tipo,database, tabla, column) :
        i = 0
        while i < len(self.tipos):
            if self.tipos[i].database == database and self.tipos[i].tabla == tabla and self.tipos[i].id == column:
                self.tipos[i] = tipo
            i += 1

    def actualizarRestriccion(self,tipo, database, tabla, column, restriccion) :
        i = 0
        while i < len(self.tipos):
            if self.tipos[i].database == database and self.tipos[i].tabla == tabla and self.tipos[i].id == column:
                self.tipos[i].restriccion = restriccion
            i += 1

            
    def actualizarRestriccion2(self,tipo, database, tabla, column, restriccion) :
        i = 0
        while i < len(self.tipos):
            if self.tipos[i].database == database and self.tipos[i].tabla == tabla and self.tipos[i].id == column and self.tipos[i].restriccion == "":
                self.tipos[i].restriccion = restriccion
            i += 1

    def actualizarLlaveForanea(self,tipo,database, tabla, column, restriccion,tablaRef, referencia) :
        i = 0
        while i < len(self.tipos):
            if self.tipos[i].database == database and self.tipos[i].tabla == tabla and self.tipos[i].id == column:
                self.tipos[i].restriccion = restriccion
                self.tipos[i].referencia = referencia
                self.tipos[i].tablaRef = tablaRef
            i += 1

    def actualizarDatabase(self,tipo,database, newDatabase) :
        i = 0
        while i < len(self.tipos):
            if self.tipos[i].database == database:
                self.tipos[i].database = newDatabase
            i += 1

    def eliminarDatabase(self,database):
        for elem in list(self.tipos):
            if elem.database == database:
                self.tipos.remove(elem)

    def eliminarTabla(self,database,tabla):
        for elem in list(self.tipos):
            if elem.database == database and elem.tabla == tabla:
                self.tipos.remove(elem)

    def eliminarID(self,database,tabla,id):
        for elem in list(self.tipos):
            if elem.database == database and elem.tabla == tabla and elem.id == id:
                self.tipos.remove(elem)


    def clear(self):
        self.tipos = []