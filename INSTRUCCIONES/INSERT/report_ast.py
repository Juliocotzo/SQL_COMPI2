from expresion_insert import *
from instrucciones_insert import *
from graphviz import Digraph

dot = Digraph('AST', node_attr={'shape': 'note','color': 'lightblue2', 'style': 'filled'})
contadorNodos = 0
instrucciones_Global = []

class AST: 

    def __init__(self):
        '''print('AST')'''


    def generarAST(self,instrucciones):
        global contadorNodos, dot, instrucciones_Global
        instrucciones_Global = instrucciones
        dot = Digraph('AST')
        contadorNodos = 2
        dot.node('node1','INIT')
        dot.node('node2','INSTRUCCIONES')
        dot.edge('node1','node2')
        indice = 0
        while indice < len(instrucciones_Global) :
            instruccion = instrucciones_Global[indice]
            #print(instruccion)
            if isinstance(instruccion, Definicion_Insert):
                self.crearNodoInsert("node2",instruccion)
            indice = indice +1
        dot.view('reportes/AST', cleanup=True)

    def crearNodoInsert(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'INSERT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoTABLA(temp1,instruccion)

    def crearNodoTABLA(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TABLA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.id)
        
    

    def crearNodoExpresion(self, padre, expresion):
        global contadorNodos, dot
        if isinstance(expresion, ExpresionIdentificador):
            if expresion.id != "":
                contadorNodos = contadorNodos + 1
                dot.node("node" + str(contadorNodos), str(expresion.id))
                dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionEntero):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.val))
            dot.edge(padre, "node" + str(contadorNodos))
        else:
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion))
            dot.edge(padre, "node" + str(contadorNodos))