from enum import Enum

class OPCIONES_DATOS(Enum):
    TRIM = 1
    SUBSTR = 2
    SUBSTRING = 3

class OPCIONES_SELECT(Enum):
    distinct = 1
    case = 2
    subconsulta = 3
    expresion = 4
    funciones = 5

class OPCIONESCREATE_TABLE(Enum):
    primaria = 1
    forenea = 2
    references = 3
    not_null = 4
    null = 5

class OPCIONES_UNIONES(Enum):
    union = 1
    intersect = 2
    excepts = 3

class OPERACION_TIEMPO(Enum):
    YEAR = 1
    DAY = 2
    MOUNTH = 3
    HOUR = 4
    MINUTE = 5
    SECOND = 6

class OPCIONES_CONSTRAINT(Enum):
    check = 1
    unique = 2
    foreign = 3

class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    ASTERISCO = 3
    DIVIDIDO = 4
    MODULO = 5
    MAYMAY = 6
    MENMEN = 7
    CEJILLA = 8
    HASTAG = 9
    S_OR = 9
    D_OR = 10
    AMPERSON = 11
    NOT_LIKE = 12
    BETWEEN = 13
    IN = 14
    NOT_IN = 15
    AVG = 16
    MAX = 17
    MIN = 18
    SIN_SOME_ANY = 19
    ALL = 20
    SOME = 21
    NOW = 22
    ANYS = 23
    ABS = 24
    LENGTH = 25
    CBRT = 26
    CEIL = 27
    CEILING = 28

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
    TRUES = 4
    FALSES = 5

class OPCION_VERIFICAR(Enum):
    NULL = 1
    N_NULL = 2
    ISNULL = 3
    NOTNULL = 4
    TRUE = 5
    FALSE = 6
    N_TRUE = 7
    N_FALSE = 8
    UNKNOWN = 9
    N_UNKNOWN = 10  

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
    varying = 13
    varchar = 14
    char = 15
    character = 16
    decimal = 17
    numeric = 18
    double_precision = 19
    current_time = 20
    current_date = 21
    now = 22
    date_part = 23
    extract = 24
    varing = 25

class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''

class ExpresionEntero(ExpresionNumerica) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, val = 0) :
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
    '''
        Esta clase representa un identificador.
    '''

    def __init__(self, id = "") :
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

    def __init__(self, val) :
        self.val = val

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

class Expresionesdatos():
    def __init__(self,tipostring,para1,para2,para3):
        self.tipostring = tipostring
        self.para1 = para1
        self.para2 = para2
        self.para3 = para3

class ExpresionVerificadora():
    def __init__(self,dato,etiqueta):
        self.dato = dato
        self.etiqueta = etiqueta