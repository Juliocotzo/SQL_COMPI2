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
            if isinstance(instruccion, Create_update):
                self.crearNodoUpdate("node2",instruccion)
            indice = indice +1
        dot.view('reportes/AST', cleanup=True)

    def crearNodoUpdate(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'UPDATE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.CrearNombreTabla(temp1, instruccion)
        self.Crear_lista_parametros(temp1, instruccion)
        
        

    def CrearNombreTabla(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Nombre Tabla')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)

        self.crearNodoExpresion(temp1,instruccion.identificador.id)

    def Crear_lista_parametros(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Lista_parametros')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.lista_update != []:
            for datos in instruccion.lista_update:
                self.crearNodoExpresion(temp1,datos.ids.id)
                self.crearNodoExpresion(temp1,datos.expresion.val)
            
        self.crearNodoWhere(temp1, instruccion)



    def crearNodoWhere(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'WHERE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 

        if instruccion.expresion.operador == OPERACION_RELACIONAL.MAYQUE:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.MENQUE:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.MAYIGQUE:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.MENIGQUE:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.DOBLEIGUAL:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.NOIG:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.DIFERENTE:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.IGUAL:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)    
    

    def operador(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Operador')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1, instruccion.expresion.operador)      

    def Valores1(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'expresion 1')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 
        if instruccion.expresion.exp1.etiqueta == TIPO_VALOR.IDENTIFICADOR:
            self.crearNodoExpresion(temp1,instruccion.expresion.exp1.id)

          
    def Valores2(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'expresion 2')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.expresion.exp2.etiqueta == TIPO_VALOR.NUMERO:
            self.crearNodoExpresion(temp1, instruccion.expresion.exp2.val)   

    def crearNodoExpresion(self, padre, expresion):
        global contadorNodos, dot
        if isinstance(expresion, ExpresionIdentificador):
            if expresion.id != "":
                contadorNodos = contadorNodos + 1
                dot.node("node" + str(contadorNodos), str(expresion.id))
                dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionComillaSimple):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.val))
            dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionEntero):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.val))
            dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionRelacional):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.exp1))
            dot.node("node" + str(contadorNodos), str(expresion.exp2))
            dot.node("node" + str(contadorNodos), str(expresion.operador))
            dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionBinaria):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.exp1))
            dot.node("node" + str(contadorNodos), str(expresion.exp2))
            dot.node("node" + str(contadorNodos), str(expresion.operador))
            dot.edge(padre, "node" + str(contadorNodos))
        else:
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion))
            dot.edge(padre, "node" + str(contadorNodos))