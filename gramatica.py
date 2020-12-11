# -----------------------------------------------------------------------------
# Gramatica del Proyecto Fase 1 - Compiladores 2
# -----------------------------------------------------------------------------
from ply import lex
import ply.yacc as yacc

entradaa = ""

reservadas = {
    'create' : 'CREATE',
    'table':'TABLE',
    'inherits': 'INHERITS',
    'integer': 'INTEGER',
    # CREATE DATABASE
    'database': 'DATABASE',
    'if' : 'IF',
    'replace' : 'REPLACE',
    'exists' : 'EXISTS',    
    'or': 'OR',
    'owner': 'OWNER',
    'not' : 'NOT',
    'mode' : 'MODE'
}

tokens = [
    'PTCOMA',
    'PAR_A',
    'PAR_C',
    'ID',
    'ENTERO',
    'IGUAL',
    'COMA'
] + list(reservadas.values())

#tokens
t_PTCOMA        = r';'
t_PAR_A         = r'\('
t_PAR_C         = r'\)'
t_COMA          = r','
t_IGUAL         = r'\='

def t_FLOTANTE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    print('FILA: ' + str(t.lineno)+ ' COLUMNA: ' + str(find_column(entradaa,t)))
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()
# Asociación de operadores y precedencia


# Definición de la gramática
from instrucciones import *
from expresiones import *

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : create_Table
                        | createDB_insrt'''
    t[0] = t[1]

def p_create_Table(t) :
    '''create_Table :  CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C PTCOMA
                       | CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C opcion_herencia PTCOMA '''
    if t[7] == ';':
        t[0] = CrearTable(t[3],t[5])
    else:
        t[0] = CrearTable_Herencia(t[3],t[7],t[5])     

def p_cuerpo_createTable_lista(t):
    ' cuerpo_createTable_lista : cuerpo_createTable_lista COMA cuerpo_createTable'
    t[1].append(t[3])
    t[0] = t[1]

def p_cuerpo_createTable(t):
    ' cuerpo_createTable_lista : cuerpo_createTable'
    t[0] = [t[1]]

def p_cuerpo_createTable_lista_(t):
    ' cuerpo_createTable : ID INTEGER'
    t[0] = Definicion(t[2],ExpresionIdentificador(t[1]))

def p_herencia(t):
    ' opcion_herencia :  INHERITS PAR_A ID PAR_C '
    t[0] = ExpresionIdentificador(t[3])


#----------------------------------------------------------------
' -----------GRAMATICA PARA LA INSTRUCCION CREATE DB------------'
#----------------------------------------------------------------

#***********************************************
'             CREATE DATABASE SIMPLE '
#************************************************

def p_createDB(t):
    'createDB_insrt : CREATE DATABASE ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[3]), None, 1)

def p_createDB_wRP(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[5]), None, 1)

def p_createDB_wIfNot(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[6]), None, 1)

def p_createDB_wRP_wIN(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[8]), None, 1)


#***********************************************
'             CREATE DATABASE UN PARAMETRO '
#************************************************
def p_createDB_up(t):
    'createDB_insrt : CREATE DATABASE ID createDB_unParam PTCOMA'

def p_createDB_wRP_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_unParam PTCOMA'

def p_createDB_wIfNot_up(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'

def p_createDB_wRP_wIN_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'

def p_createDB_unParam_Owner(t):
    'createDB_unParam : OWNER ID'

def p_createDB_un_Param_Mode(t):
    'createDB_unParam : MODE ENTERO'

def p_createDB_unParam_Owner_I(t):
    'createDB_unParam : OWNER IGUAL ID'

def p_createDB_un_Param_Mode_I(t):
    'createDB_unParam : MODE IGUAL ENTERO'


#***********************************************
'             CREATE DATABASE DOS PARAMETROS '
#************************************************

def p_createDB_dp(t):
    'createDB_insrt : CREATE DATABASE ID createDB_dosParam PTCOMA'

def p_createDB_wRP_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_dosParam PTCOMA'

def p_createDB_wIfNot_dp(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'

def p_createDB_wRP_wIN_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'

def p_createDB_dosParam_Owner(t):
    'createDB_dosParam : OWNER ID MODE ENTERO'

def p_createDB_dosParam_Owner_b(t):
    'createDB_dosParam : OWNER ID MODE IGUAL ENTERO'

def p_createDB_dosParam_Mode(t):
    'createDB_dosParam : MODE ENTERO OWNER ID'

def p_createDB_dosParam_Mode_b(t):
    'createDB_dosParam : MODE ENTERO OWNER IGUAL ID'

def p_createDB_dosParam_Owner_I(t):
    'createDB_dosParam : OWNER IGUAL ID MODE ENTERO'

def p_createDB_dosParam_Owner_I_b(t):
    'createDB_dosParam : OWNER IGUAL ID MODE IGUAL ENTERO'

def p_createDB_dosParam_Mode_I(t):
    'createDB_dosParam : MODE IGUAL ENTERO OWNER ID'

def p_createDB_dosParam_Mode_I_b(t):
    'createDB_dosParam : MODE IGUAL ENTERO OWNER IGUAL ID'

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)
    print('FILA: '+ str(t.lineno) + ' COLUMNA: ' + str(find_column(entradaa,t)) )
    
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    global entradaa
    entradaa = input
    return parser.parse(input)