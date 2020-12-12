import gramatica as gASC
import ts as TS
from expresiones import *
from instrucciones import *
import collections.abc
import json
from graphviz import Digraph
import tempfile

instrucciones_Global = None
dot = Digraph('AST', node_attr={'shape': 'note','color': 'lightblue2', 'style': 'filled'})
contadorNodos = 0


class Person:
    def __init__(self):
        print('HOLa')

    def ejecutarAscendente(self):
        global instrucciones_Global, gram, tablaELexicos, tablaESintacticos
        f = open("./entrada.txt", "r")
        input = f.read()
        instrucciones = gASC.parse(input)
        instrucciones_Global = instrucciones
        self.procesar_instrucciones(instrucciones, 0)

    def generarAST(self):
        global contadorNodos, dot, instrucciones_Global
        dot = Digraph('AST')
        contadorNodos = 2
        dot.node('node1','INIT')
        dot.node('node2','Instrucciones')
        dot.edge('node1','node2')
        indice = 0
        while indice < len(instrucciones_Global) :
            instruccion = instrucciones_Global[indice]
            if isinstance(instruccion, CrearTable):
                temp1 = self.crearNodoCrearTable("node2", instruccion)
                if instruccion.intrucc != []:
                    self.crearNodoListaDefinicion(temp1,instruccion)
            elif isinstance(instruccion, CrearTable_Herencia):
                temp1 = self.crearNodoCrearTable_Herencia("node2", instruccion)
                if instruccion.intrucc != []:
                    self.crearNodoListaDefinicion(temp1,instruccion)
            elif isinstance(instruccion, Definicion):
                self.crearNodoDefinicion("node2", instruccion)

            indice = indice +1

        dot.view('AST', cleanup=True)

    def crearNodoCrearTable(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CreateTable')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoNombreTabla(temp1,instruccion.nombre_tabla)
        self.crearNodoExpresion(temp1, instruccion.intrucc)
        return temp1

    def crearNodoNombreTabla(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), instruccion)
        dot.edge(padre, "node" + str(contadorNodos))

    def crearNodoCrearTable_Herencia(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CreateTableHerencia')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoNombreTabla(temp1,instruccion.nombre_tabla)
        self.crearNodoExpresion(temp1, instruccion.intrucc)
        self.crearNodoExpresion(temp1, instruccion.herencia)
        return temp1;
    
    def crearNodoNombreHerencia(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), str(instruccion))
        dot.edge(padre, "node" + str(contadorNodos))
  
    def crearNodoListaDefinicion(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), "LISTA DEFINICION")
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        for insd in instruccion.intrucc:
            self.crearNodoDefinicion(temp1,insd)

    def crearNodoDefinicion(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), "DEFINICION")
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.id)
        self.crearNodoTipo(temp1,instruccion.tipo)
    
    def procesar_createTable(self,instr) :
        print('Crear Tabla Normal')


    def procesar_createTable_Herencia(self,instr) :
        print('Crear Tabla con herencia')
    
    def procesar_Definicion(self,instr) :
        print('Definicion1')

    def procesar_instrucciones(self,instrucciones,indice) :
        ## lista de instrucciones recolectadas
        while indice < len(instrucciones):
            instruccion = instrucciones[indice]
            if isinstance(instruccion, CrearTable) : 
                self.procesar_createTable(instruccion)
                if instruccion.intrucc != []:
                    self.procesar_instrucciones(instruccion.intrucc,indice)
            elif isinstance(instruccion, CrearTable_Herencia) : 
                self.procesar_createTable_Herencia(instruccion)
                if instruccion.intrucc != []:
                    self.procesar_instrucciones(instruccion.intrucc,indice)
            elif isinstance(instruccion, Definicion) : 
                self.procesar_Definicion(instruccion)

            else : print('Error: instrucción no válida')

            indice = indice + 1

    def crearNodoExpresion(self, padre, expresion):
        global contadorNodos, dot
        if isinstance(expresion, ExpresionIdentificador):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.id))
            dot.edge(padre, "node" + str(contadorNodos))

    def crearNodoTipo(self, padre, expresion):
        global contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), str(expresion))
        dot.edge(padre, "node" + str(contadorNodos))
        

if __name__ == "__main__":
    p = Person()
    p.ejecutarAscendente()
    p.generarAST()