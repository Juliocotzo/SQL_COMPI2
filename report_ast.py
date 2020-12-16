import ts as TS
from expresiones import *
from instrucciones import *
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
            if isinstance(instruccion, CreateDatabase):
                self.crearNodoCreateDatabase("node2", instruccion)
            elif isinstance(instruccion, Create_Table):
                self.crearNodoCreateTable("node2", instruccion)
            elif isinstance(instruccion, showDatabases):
                self.crearNodoshowDatabases("node2", instruccion)
            elif isinstance(instruccion, dropDatabase):
                self.crearNododropDatabase("node2", instruccion)
            elif isinstance(instruccion, useDatabase) : 
                self.crearNodo_useDatabase("node2", instruccion)
            elif isinstance(instruccion, Create_Alterdatabase) : 
                self.crearNodo_alterDatabase("node2", instruccion)
            elif isinstance(instruccion, showTables):
                self.crearNodoshowTables("node2", instruccion)
            elif isinstance(instruccion, Crear_Drop):
                self.crearNodoDropTable("node2",instruccion)
            if isinstance(instruccion, Crear_altertable):
                self.crearNodoAlterTable("node2",instruccion)
            indice = indice +1
        dot.view('reportes/AST', cleanup=True)


    

    def crearNodoCreateDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CREATE DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoNombreDatabase(temp1,instruccion)
        if instruccion.usuario.id != "":
            self.crearNodoUsuarioDatabase(temp1,instruccion)
        self.crearNodoModoDatabase(temp1,instruccion)

    def crearNodoNombreDatabase(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'NOMBRE DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.nombre)

    def crearNodoUsuarioDatabase(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'USUARIO DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.usuario)

    def crearNodoModoDatabase(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'MODO DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.modo)

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
        elif isinstance(expresion, ExpresionNumeroSimple):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.val))
            dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionComillaSimple):
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
        elif isinstance(expresion, ExpresionLogica):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.exp1))
            dot.node("node" + str(contadorNodos), str(expresion.exp2))
            dot.node("node" + str(contadorNodos), str(expresion.operador))
            dot.edge(padre, "node" + str(contadorNodos))
        else:
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion))
            dot.edge(padre, "node" + str(contadorNodos))

    def crearNodoCreateTable(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CREATE TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoNombreTabla(temp1,instruccion)
        if instruccion.instrucciones != []:
            for ins in instruccion.instrucciones:
                if isinstance(ins, Definicion_Columnas): 
                    self.crearNodoDefinicion(temp1, ins)
                elif isinstance(ins, LLave_Primaria): 
                    self.crearNodoConstraintLlavePrimaria(temp1, ins)
                elif isinstance(ins, Definicon_Foranea): 
                    self.crearNodoConstraintLlaveForanea(temp1, ins)
                elif isinstance(ins, Lista_Parametros): 
                    self.crearNodoConstraintUnique(temp1, ins)
                elif isinstance(ins, definicion_constraint): 
                    self.crearNodoConstraint(temp1, ins)
    
    def crearNodoNombreTabla(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'NOMBRE TABLA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoNombreTablaID(temp1,instruccion)

    def crearNodoNombreTablaID(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), instruccion.id)
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)

    def crearNodoDefinicion(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DEFINICION')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoDefinicionNombreTabla(temp1,instruccion)
        self.crearNodoDefinicionTipoDato(temp1,instruccion)
        self.crearNodoDefinicionRestriccion(temp1,instruccion)
        self.crearNodoDefinicionReferencia(temp1,instruccion)
       
    def crearNodoDefinicionNombreTabla(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'NOMBRE COLUMNA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.id)

    def crearNodoDefinicionTipoDato(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TIPO DATO')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.id)

    def crearNodoDefinicionRestriccion(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'RESTRICCION')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.etiqueta)

    def crearNodoDefinicionReferencia(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'REFERENCIA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.id_referencia)
    
    def crearNodoConstraintLlavePrimaria(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintLlavePrimariaTipoConstraint(temp1,instruccion)
        self.crearNodoConstraintLlavePrimariaId(temp1,instruccion)

    def crearNodoConstraintLlavePrimariaTipoConstraint(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TIPO CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintLlavePrimariaTipo(temp1,instruccion)

    def crearNodoConstraintLlavePrimariaTipo(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), str(OPCIONESCREATE_TABLE.PRIMARIA))
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
    
    def crearNodoConstraintLlavePrimariaId(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.id)

    def crearNodoConstraintLlaveForanea(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintLlaveForaneaTipoConstraint(temp1,instruccion)
        self.crearNodoConstraintLlaveForaneaId(temp1,instruccion)
        self.crearNodoConstraintLlaveForaneaTablaRef(temp1,instruccion)
        self.crearNodoConstraintLlaveForaneaIdRef(temp1,instruccion)

    def crearNodoConstraintLlaveForaneaTipoConstraint(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TIPO CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintLlaveForaneaTipo(temp1,instruccion)

    def crearNodoConstraintLlaveForaneaTipo(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), str(OPCIONESCREATE_TABLE.FORANEA))
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
    
    def crearNodoConstraintLlaveForaneaId(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.nombre_tabla)

    def crearNodoConstraintLlaveForaneaTablaRef(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TABLA REFERENCIA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.referencia_tabla)

    def crearNodoConstraintLlaveForaneaIdRef(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID REFERENCIA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.campo_referencia)

    def crearNodoConstraintUnique(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintUniqueTipoConstraint(temp1,instruccion)
        self.crearNodoConstraintUniqueListaIds(temp1,instruccion)
       
    def crearNodoConstraintUniqueTipoConstraint(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TIPO CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintUniqueTipo(temp1,instruccion)

    def crearNodoConstraintUniqueTipo(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), str(OPCIONESCREATE_TABLE.UNIQUE))
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  

    def crearNodoConstraintUniqueListaIds(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'LISTA ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.identificadores != []:
            for ids in instruccion.identificadores:
                self.crearNodoExpresion(temp1,ids.id)

    def crearNodoConstraint(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        self.crearNodoConstraintTipoConstraint(temp1,instruccion)
        self.crearNodoConstraintId(temp1,instruccion)
        if instruccion.tipo == 'UNIQUE':
            self.crearNodoConstraintLISTA(temp1,instruccion)
        elif instruccion.tipo == 'FOREING':
            self.crearNodoConstraintForaneaId(temp1,instruccion)
            self.crearNodoConstraintForaneaTablaRef(temp1,instruccion)
            self.crearNodoConstraintForaneaIdRef(temp1,instruccion)
        elif instruccion.tipo == 'CHECK':
            self.crearNodoConstraintCheckId(temp1,instruccion) 

    def crearNodoConstraintId(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 
        self.crearNodoExpresion(temp1,instruccion.id)

    def crearNodoConstraintTipoConstraint(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TIPO CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintTipo(temp1,instruccion)

    def crearNodoConstraintTipo(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        if instruccion.tipo == 'UNIQUE':
            dot.node("node" + str(contadorNodos), str(OPCIONES_CONSTRAINT.UNIQUE))
        elif instruccion.tipo == 'FOREING':
            dot.node("node" + str(contadorNodos), str(OPCIONES_CONSTRAINT.FOREIGN))
        elif instruccion.tipo == 'CHECK':
            dot.node("node" + str(contadorNodos), str(OPCIONES_CONSTRAINT.CHECK))
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 
     
    def crearNodoConstraintLISTA(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'LISTA ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'UNIQUE':
            if instruccion.opciones_constraint != []:
                for ids in instruccion.opciones_constraint:
                    self.crearNodoExpresion(temp1,ids.id)
        
    def crearNodoConstraintForaneaId(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'FOREING':
            if instruccion.opciones_constraint != []:
                for ids in instruccion.opciones_constraint:
                    self.crearNodoExpresion(temp1,instruccion.columna)

    def crearNodoConstraintForaneaTablaRef(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TABLA REFERENCIA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'FOREING':
            if instruccion.opciones_constraint != []:
                for ids in instruccion.opciones_constraint:
                    self.crearNodoExpresion(temp1,instruccion.referencia)

    def crearNodoConstraintForaneaIdRef(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID REFERENCIA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'FOREING':
            if instruccion.opciones_constraint != []:
                for ids in instruccion.opciones_constraint:
                    self.crearNodoExpresion(temp1,ids)

    def crearNodoConstraintCheckId(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'CHECK':
            if instruccion.opciones_constraint != []:
                for ids in instruccion.opciones_constraint:
                    if type(ids.exp1) == ExpresionIdentificador:
                        self.crearNodoExpresion(temp1,ids.exp1.id)
                    else: 
                        self.crearNodoExpresion(temp1,ids.exp2.id)

    def crearNodoshowDatabases(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'SHOW DATABASES')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)

    def crearNodoshowTables(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'SHOW TABLES')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)

    def crearNododropDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DROP DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNododropDatabaseID(temp1,instruccion)

    def crearNododropDatabaseID(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.id)

    def crearNodo_useDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'USE DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodo_useDatabaseID(temp1,instruccion)

    def crearNodo_useDatabaseID(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.id)

    def crearNodo_alterDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ALTER DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodo_alterDatabaseDatabase(temp1,instruccion)
        self.crearNodo_alterDatabaseID(temp1,instruccion)
        
    def crearNodo_alterDatabaseDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.id_tabla)

    def crearNodo_alterDatabaseID(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        if isinstance(instruccion.tipo_id,ExpresionIdentificador) : 
            dot.node("node" + str(contadorNodos), 'OWNER ID')
        elif isinstance(instruccion.tipo_id, ExpresionComillaSimple) : 
            dot.node("node" + str(contadorNodos), 'OWNER ID')            
        else:
            dot.node("node" + str(contadorNodos), 'NEW ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.tipo_id)

    def crearNodoDropTable(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DROP_TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.Crear_lista_parametros(temp1,instruccion)
        

    def Crear_lista_parametros(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Tablas')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.lista_ids != []:
            for datos in instruccion.lista_ids:
                self.crearNodoExpresion(temp1,datos.id)

            
    def crearNodoAlterTable(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ALTER TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.etiqueta == TIPO_ALTER_TABLE.ADD_CHECK:
            self.crearAlterTable_addcheck(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ADD_FOREIGN:
            self.crearAlterTable_foreign(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_CHECK:
            self.crearAlterTable_addContraintCheck(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_UNIQUE:
            self.crearAlterTable_Unique(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_FOREIGN:
            self.crearAlterTable_ConstraintForeign(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ALTER_COLUMN:
            self.crearAlterTable_Column(temp1, instruccion)

    def crearAlterTable_Column(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Alter Column')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)   
        self.crearNodoExpresion(temp1,instruccion.identificador)
        if instruccion.lista_campos != []:
            for datos in instruccion.lista_campos:
                self.crearNodoExpresion(temp1,datos.identificador.id)
                self.crearNodoExpresion(temp1,datos.tipo.id)
                if datos.par1 != None:
                    self.crearNodoExpresion(temp1,datos.par1)
                if datos.par2 != None:
                    self.crearNodoExpresion(temp1,datos.par2)

    def crearAlterTable_ConstraintForeign(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Constraint Foreign')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.identificador)
        self.crearNodoExpresion(temp1,instruccion.columnid)
        self.crearAlterTable_foreign_columna(temp1, instruccion)
        self.crearAlterTable_foreign_referencia(temp1, instruccion)

    def crearAlterTable_Unique(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Unique')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.identificador)
        self.crearNodoExpresion(temp1,instruccion.columnid)
        self.crearAlterTable_foreign_columna(temp1, instruccion)


    def crearAlterTable_addContraintCheck(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Add Contraint Check')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.identificador)
        self.crearNodoExpresion(temp1,instruccion.columnid)   
        self.crearAlterTable_addcheck_Condicion(temp1, instruccion)


    def crearAlterTable_foreign(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Add Foreign')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)                
        self.crearNodoExpresion(temp1,instruccion.identificador)
        self.crearAlterTable_foreign_columna(temp1, instruccion)
        self.crearAlterTable_foreign_referencia(temp1, instruccion)

    def crearAlterTable_foreign_columna(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Columna')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)                
        self.crearNodoExpresion(temp1,instruccion.identificador)
        if instruccion.lista_campos != []:
            for datos in instruccion.lista_campos:
                self.crearNodoExpresion(temp1,datos.id)


    def crearAlterTable_foreign_referencia(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'referencia')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)                
        self.crearNodoExpresion(temp1,instruccion.identificador)
      
        if instruccion.lista_ref != []:
            for datos in instruccion.lista_ref:
                self.crearNodoExpresion(temp1,datos.id)

    def crearAlterTable_addcheck(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Add check')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)                
        self.crearNodoExpresion(temp1,instruccion.identificador)
        self.crearAlterTable_addcheck_Condicion(temp1, instruccion)

    def crearAlterTable_addcheck_Condicion(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Condicion')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        print(instruccion.expresionlogica.operador)
        if instruccion.expresionlogica.operador == OPERACION_LOGICA.AND or instruccion.expresionlogica.operador == OPERACION_LOGICA.OR: 
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.exp1.exp1.id)
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.exp1.exp2.val)
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.operador)
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.exp2.exp1.id)
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.exp2.exp2.val)
        else:
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.exp1.id)
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.operador)
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.exp2.val)