from enum import Enum

class TIPO_INSERT(Enum):
    CON_PARAMETROS = 1
    SIN_PARAMETROS = 2


class OPERACION_RELACIONAL(Enum):
    MAYQUE = 1
    MENQUE = 2
    MAYIGQUE = 3
    MENIGQUE = 4
    DOBLEIGUAL = 5
    NOIG   = 6
    DIFERENTE = 7
    IGUAL = 8

class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    ASTERISCO = 3
    DIVIDIDO = 4

class TIPO_VALOR(Enum):
    IDENTIFICADOR = 1
    NUMERO = 2

class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''

class ExpresionIdentificador(ExpresionNumerica) :
    '''
        Esta clase representa un identificador.
    '''

    def __init__(self,etiqueta, id = "") :
        self.etiqueta = etiqueta
        self.id = id


class ExpresionEntero(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self,etiqueta ,val = 0) :
        self.val = val
        self.etiqueta = etiqueta


class ExpresionIdentificadorDoble(ExpresionNumerica) :
    def __init__(self, id = "", id1 = ""):
        self.id = id
        self.id1 = id1


class ExpresionBinaria(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Aritmética Binaria.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador


class ExpresionRelacional() :
    '''
        Esta clase representa la expresión lógica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador


class ExpresionCadena :
    '''
        Esta clase representa una Expresión de tipo cadena.
    '''

class ExpresionComillaSimple(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas doble.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, etiqueta,val):
        self.val = val
        self.etiqueta = etiqueta