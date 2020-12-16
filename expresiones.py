from enum import Enum

class OPCIONESCREATE_TABLE(Enum):
    PRIMARIA = 1
    FORANEA = 2
    REFERENCES = 3
    NOT_NULL = 4
    NULL = 5
    PRIMARIA_SOLA = 6
    CONSTRAINT = 7
    UNIQUE = 8

class OPERACION_TIEMPO(Enum):
    YEAR = 1
    DAY = 2
    MOUNTH = 3
    HOUR = 4
    MINUTE = 5
    SECOND = 6

class OPCIONES_CONSTRAINT(Enum):
    CHECK = 1
    UNIQUE = 2
    FOREIGN = 3

class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    ASTERISCO = 3
    DIVIDIDO = 4

class OPERACION_RELACIONAL(Enum):
    MAYQUE = 1
    MENQUE = 2
    MAYIGQUE = 3
    MENIGQUE = 4
    DOBLEIGUAL = 5
    NOIG   = 6
    DIFERENTE = 7
    IGUAL = 8

class OPERACION_LOGICA(Enum):
    AND = 1
    OR = 2
    NOT = 3
    
class TIPO_DE_DATOS(Enum):
    text_ = 1
    float_ = 2
    integer_ = 3
    smallint_ = 4
    money = 5
    bigint = 6
    real = 7
    double = 8
    interval = 9
    time = 10
    timestamp = 11
    date = 12
    varing = 13
    varchar = 14
    char = 15
    character = 16
    decimal = 17
    numeric = 18
    double_precision = 19

class TIPO_VALOR(Enum):
    IDENTIFICADOR = 1
    NUMERO = 2
    CADENA = 3

class TIPO_INSERT(Enum):
    CON_PARAMETROS = 1
    SIN_PARAMETROS = 2

class TIPO_LOGICA(Enum):
    AND = 1
    OR = 2
    NOT = 3

class TIPO_ALTER_TABLE(Enum):
    DROP_CONSTRAINT = 1
    RENAME_COLUMN = 2
    ADD_COLUMN = 3
    ADD_CHECK = 4
    ADD_FOREIGN = 5
    ADD_CONSTRAINT_CHECK = 6
    ADD_CONSTRAINT_UNIQUE = 7
    ADD_CONSTRAINT_FOREIGN = 8
    ALTER_COLUMN = 9

class TIPO_DELETE(Enum):
    DELETE_NORMAL = 1
    DELETE_RETURNING = 2
    DELETE_EXIST = 3
    DELETE_CONDIFION = 4
    DELETE_USING = 5
    DELETE_EXIST_RETURNING = 6
    DELETE_CONDICION_RETURNING = 7
    DELETE_USING_returnin = 8

class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''

class ExpresionEntero(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self,etiqueta, val = 0) :
        self.etiqueta = etiqueta
        self.val = val


class ExpresionBinaria(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Aritmética Binaria.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionIdentificador(ExpresionNumerica) :
    def __init__(self,etiqueta, id = "") :
        self.etiqueta = etiqueta
        self.id = id

class ExpresionIdentificadorDoble(ExpresionNumerica) :
    def __init__(self, id = "", id1 = ""):
        self.id = id
        self.id1 = id1

class ExpresionNumero(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, etiqueta ,val = 0, val1 = 0) :
        self.val = val
        self.val1 = val1
        self.etiqueta = etiqueta

class ExpresionNumeroSimple(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, val = 0) :
        self.val = val


class Expresion_Caracter(ExpresionNumero):

    def __init__(self, etiqueta, val = 0):
        self.etiqueta = etiqueta
        self.val = val



class ExpresionCadena :
    '''
        Esta clase representa una Expresión de tipo cadena.
    '''

class ExpresionComillaSimple(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas doble.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self,etiqueta, val) :
        self.val = val
        self.etiqueta = etiqueta

class ExpresionRelacional() :
    '''
        Esta clase representa la expresión lógica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador


class ExpresionLogica() :
    '''
        Esta clase representa la expresión lógica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionTiempo():
    def __init__(self, operador):
        self.operador = operador

class ExpresionBooleana():
    def __init__(self, expresion):
        self.expresion = expresion