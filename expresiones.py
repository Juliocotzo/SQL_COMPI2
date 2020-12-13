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

class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''
class ExpresionIdentificador(ExpresionNumerica) :
    def __init__(self, id = "") :
        self.id = id

class ExpresionNumero(ExpresionNumerica) :
    def __init__(self, val = 0) :
        self.val = val