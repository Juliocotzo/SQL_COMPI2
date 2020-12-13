reporte_sintactico=""
reporte_lexico = ""

# -----------------------------------------------------------------------------
# Gramatica del Proyecto Fase 1 - Compiladores 2
# -----------------------------------------------------------------------------


reservadas = {
    'select': 'SELECT',
    'insert': 'INSERT',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'count': 'COUNT',
    'from': 'FROM',
    'into': 'INTO',
    'values': 'VALUES',
    'sum' : 'SUM',
    'set': 'SET',
    'inner': 'INNER',
    'join': 'JOIN',
    'on': 'ON',
    'case': 'CASE',
    'when': 'WHEN',
    'then': 'THEN',
    'end': 'END',
    'and': 'AND',
    'or': 'OR',
    'else': 'ELSE',
    'where': 'WHERE',
    'as': 'AS',
    'create': 'CREATE',
    'table': 'TABLE',
    'inherits': 'INHERITS',
    'alter': 'ALTER',
    'database': 'DATABASE',
    'to': 'TO',
    'rename': 'RENAME',
    'owner': 'OWNER',
    'drop': 'DROP',
    'currUser' : 'CURRENT_USER',
    'sessUser' : 'SESSION_USER',
    'foreign' : 'FOREIGN',
    'key': 'KEY',
    'add' : 'ADD',
    'check' : 'CHECK',
    'constraint': 'CONSTRAINT',
    'column' : 'COLUMN',
    'unique' : 'UNIQUE',
    'references' : 'REFERENCES',
    'type' : 'TYPE',
    'set' : 'SET',
    'not' : 'NOT',
    'like' : 'LIKE',
    'null' : 'NULL',
    # ---- DATA TYPES AND SPECIFICATIONS--------
    'text': 'TEXT',
    'float': 'FLOAT',
    'integer': 'INTEGER',
    'char': 'CHAR',
    'varchar' : 'VARCHAR',
    'smallint':'SMALLINT',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'extract' : 'EXTRACT',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'now' : 'NOW',
    'date_part' : 'DATE_PART',
    'current_date': 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'to' : 'TO',
    'enum' : 'ENUM',
    'money' : 'MONEY',
    # ---- DELETE --------
    'only' : 'ONLY',
    'in' :  'IN',
    'returning' : 'RETURNING',
    'using' : 'USING',
    'exists' : 'EXISTS',
    # ---- USE DATABASE --------
    'use' : 'USE',
    #----- SELECT-----------
    'distinct' : 'DISTINCT',
    'group' : 'GROUP',
    'by' : 'BY',
    'order' : 'ORDER',
    'asc' : 'ASC',
    'desc' : 'DESC',
    'primary' : 'PRIMARY',
    'key' : 'KEY',
    'foreing' : 'FOREING',
    'avg' : 'AVG',
    'min' : 'MIN',
    'max' : 'MAX',
    'between' : 'BETWEEN',
    'having' : 'HAVING',
    #----- FUNCIONES TRIGONOMETRICAS -----------
    'acos' : 'ACOS',
    'acos' : 'ACOS',
    'acosd' : 'ACOSD',
    'asin' : 'ASIN',
    'asind' : 'ASIND',
    'atan' : 'ATAN',
    'atand' : 'ATAND',
    'atan2' : 'ATAN2',
    'atan2d' : 'ATAN2D',
    'cos' : 'COS',
    'cosd' : 'COSD',
    'cot' : 'COT',
    'cotd' : 'COTD',
    'sin' : 'SIN',
    'sind' : 'SIND',
    'tan' : 'TAN',
    'tand' : 'TAND',
    'sinh' : 'SINH',
    'cosh' : 'COSH',
    'tanh' : 'TANH',
    'asinh' : 'ASINH',
    'acosh' : 'ACOSH',
    'atanh' : 'ATANH',
    #----- FUNCIONES MATEMATICAS-----------
    'abs' : 'ABS',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',
    'div' : 'DIV',
    'exp' : 'EXP',
    'factorial' : 'FACTORIAL',
    'floor' : 'FLOOR',
    'gcd' : 'GCD',
    'lcm' : 'LCM',
    'ln' : 'LN',
    'log' : 'LOG',
    'log10' : 'LOG10',
    'min_scale' : 'MIN_SCALE',
    'mod' : 'MOD',
    'pi' : 'PI',
    'power' : 'POWER',
    'radians' : 'RADIANS',
    'round' : 'ROUND',
    'scale' : 'SCALE',
    'sign' : 'SIGN',
    'sqrt' : 'SQRT',
    'trim_scale' : 'TRIM_SCALE',
    'truc' : 'TRUC',
    'width_bucket' : 'WIDTH_BUCKET',
    'random' : 'RANDOM',
    'setseed' : 'SETSEED',
    #----- DATATYPES -----------
    'symmetric' : 'SYMMETRIC',
    'isnull' : 'ISNULL',
    'true': 'TRUE',
    'notnull' : 'NOTNULL',
    'is' : 'IS',
    'false' : 'FALSE',
    'unknown' : 'UNKNOWN',
    #----- BYNARY STRING FUNCTIONS -----------
    'length' : 'LENGTH',
    'substring' : 'SUBSTRING',
    'trim' : 'TRIM',
    'get_byte' : 'GET_BYTE',
    'md5' : 'MD5',
    'set_byte' : 'SET_BYTE',
    'sha256' : 'SHA256',
    'substr' : 'SUBSTR',
    'convert' : 'CONVERT',
    'encode' : 'ENCODE',
    'decode' : 'DECODE',
    #----- COMBINING QUERIES -----------
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    'all' : 'ALL',
    #----- LIMIT AND OFFSET -----------
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',
    'some' : 'SOME',
    'any' : 'ANY',
    ##----- COMBINING QUERIES -----------
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'natural' : 'NATURAL',
    'outer' : 'OUTER'
}

tokens = [
    'PTCOMA',
    'ASTERISCO',
    'COMA',
    'PAR_A',
    'PAR_C',
    'FLOTANTE',
    'ENTERO',
    'CADENA',
    'ID',
    'PUNTO',
    'MENIGQUE',
    'NOIG',
    'MAYIGQUE',
    'MAYMAY',
    'MENMEN',
    'MENQUE',
    'MAYQUE',
    'DOBLEIG',
    'NOIGUAL',
    'IGUAL',
    'SUMA',
    'RESTA',
    'MULTI',
    'DIVISION',
    'MODULO',
    'Y',
    'S_OR',
    'HASHTAG',
    'CEJILLA',
    'D_OR'
    
] + list(reservadas.values())

#tokens
t_PTCOMA        = r';'
t_COMA          = r','
t_MENIGQUE      = r'<='
t_MAYIGQUE      = r'>='
t_MAYMAY        = r'>>'
t_MENMEN        = r'<<'
t_NOIG          = r'<>'
t_NOIGUAL       = r'!='
t_DOBLEIG       = r'=='


t_SUMA          = r'\+'
t_RESTA         = r'\-'
t_DIVISION      = r'\\'
t_ASTERISCO     = r'\*'
t_MODULO        = r'\%'
t_PAR_A         = r'\('
t_PAR_C         = r'\)'
t_PUNTO         = r'\.'
t_MENQUE        = r'\<'
t_MAYQUE        = r'\>'
t_IGUAL         = r'\='
t_D_OR          = r'\|\|'
t_Y             = r'\&'
t_S_OR          = r'\|'
t_HASHTAG       = r'\#'
t_CEJILLA       = r'\~'




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
    print("Illegal character '%s'" % t.value[0], t.lineno, t.lexpos)
    global reporte_lexico
    reporte_lexico += "<tr> <td> Lexico </td> <td>" + t.value[0] + "</td>" + "<td>" + str(t.lineno) + "</td> <td> "+ str(t.lexpos)+"</td></th>"
 
    t.lexer.skip(1)
# TOKENIZAR

   

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()
 
from instrucciones import *
from expresiones import *


# Asociación de operadores y precedencia
precedence = (
    ('left','MAYQUE','MENQUE','MAYIGQUE','MENIGQUE'),
    ('left','IGUAL','NOIG','NOIGUAL'),
    ('left','AND','OR'),
    ('left','SUMA','RESTA'),
    ('left','MULTI','DIVISION'),
    )

# Definición de la gramática

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
                        

#-------------------------------------------------------------------------
#
#           MODIFICACIONES LopDlMa
#
#-------------------------------------------------------------------------
#

def p_instruccion_f_create_table(t):
    'instruccion : create_Table_isnrt'
    t[0] = t[1]

# --------- ALTER TABLE ADD PRODUCCIONES-------------------------
def p_constraint_esp(t):
    'constraint_esp : CHECK PAR_A expresion_logica PAR_C '
    temp = [] 
    temp.append(t[1].upper())
    temp.append([t[3]])
    t[0] = temp



def p_constraint_esp1(t):
    'constraint_esp :  UNIQUE PAR_A campos_c PAR_C '
    temp = [] 
    temp.append(t[1].upper())
    temp.append(t[3])
    t[0] = temp

def p_constraint_esp2(t):
    'constraint_esp : FOREING KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C '
    temp = []
    temp.append(t[1].upper())
    temp.append(t[4])
    temp.append(t[7])
    temp.append([t[9]])
    t[0] = temp




def p_alerTable_alter(t):
    ' alterTable_alter :  alterTable_alter COMA Table_alter '
def p_alerTable_alter2(t):
    'alterTable_alter : Table_alter'
def p_Table_alter(t):
    ' Table_alter :  ALTER COLUMN ID TYPE TIPO_DATO '
def p_Table_alter2(t):
    ' Table_alter : ALTER COLUMN ID SET NOT NULL '

#YA ESTA
def p_cons_campos(t):
    'campos_c : campos_c COMA ID '
    t[1].append(ExpresionIdentificador(t[3]))
    t[0] = t[1]

def p_cons_campos_id(t):
    ' campos_c : ID'
    t[0] = [ExpresionIdentificador(t[1])]

#-------------------------------------------------------------------------
#
#           MODIFICACIONES LopDlMa
#
#-------------------------------------------------------------------------
#
' ---------- GRAMATICA PARA LA INSTRUCCION CREATE TABLE ---------'

def p_create_table(t):
    ''' create_Table_isnrt : CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C PTCOMA 
                            | CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C INHERITS PAR_A ID PAR_C PTCOMA '''

    if t[7] == ';' :
        t[0] = Create_Table(t[3], None , t[5])
    else:
        t[0] = Create_Table(t[3], t[7], t[5])


def p_cuerpo_createTable_lista(t):
    ' cuerpo_createTable_lista : cuerpo_createTable_lista COMA cuerpo_createTable'
    t[1].append(t[3])
    t[0] = t[1]


def p_cuerpo_createTable(t):
    ' cuerpo_createTable_lista : cuerpo_createTable'
    t[0] = [t[1]]


def p_createTable(t):
    ' cuerpo_createTable :  ID TIPO_DATO '
    t[0] = Definicion_Columnas(t[1],t[2], None,None,None)

def p_createTable_id_pk(t):
    ' cuerpo_createTable : ID TIPO_DATO PRIMARY KEY'
    t[0] = Definicion_Columnas(t[1],t[2], OPCIONESCREATE_TABLE.PRIMARIA,None,None)    


def p_createTable_id_ref(t):
    ' cuerpo_createTable : ID TIPO_DATO REFERENCES ID'
    t[0] = Definicion_Columnas(t[1], t[2], OPCIONESCREATE_TABLE.REFERENCES, t[4],None)


def p_createTable_id_not_null(t):
    ' cuerpo_createTable : ID TIPO_DATO NOT NULL'
    t[0] = Definicion_Columnas(t[1], t[2], OPCIONESCREATE_TABLE.NOT_NULL, None,None)

def p_createTable_null(t):
    ' cuerpo_createTable : ID TIPO_DATO NULL'
    t[0] = Definicion_Columnas(t[1], t[2], OPCIONESCREATE_TABLE.NULL, None,None)


def p_createTable_pk(t):
    ' cuerpo_createTable :  PRIMARY KEY PAR_A ID PAR_C'
    t[0] = LLave_Primaria(t[4])

def p_createTable_fk(t):
    ' cuerpo_createTable : FOREING KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C'
    t[0] = Definicon_Foranea(t[4], t[7], t[9])

def p_createTable_unique(t):
    ' cuerpo_createTable : UNIQUE PAR_A campos_c PAR_C '
    t[0] = Lista_Parametros(t[3])

def p_createTable_constraint(t):
    ' cuerpo_createTable : CONSTRAINT ID constraint_esp '''
    if t[3][0] == 'CHECK':
        t[0] = definicion_constraint(t[2], t[3][0], None, None ,t[3][1])
    elif t[3][0] == 'UNIQUE':
        t[0] = definicion_constraint(t[2], t[3][0], None, None ,t[3][1])
    elif t[3][0] == 'FOREING':
        t[0] = definicion_constraint(t[2], t[3][0], t[3][2], t[3][1] ,t[3][3])
        
    

def p_tipo_dato_text(t):
    ' TIPO_DATO : TEXT'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.text_)

def p_tipo_dato_float(t):
    ' TIPO_DATO : FLOAT'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.float_)

def p_tipo_dato_integer(t):
    ' TIPO_DATO : INTEGER'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.integer_)

def p_tipo_dato_smallint(t):
    ' TIPO_DATO : SMALLINT'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.smallint_)

def p_tipo_dato_money(t):
    ' TIPO_DATO : MONEY'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.money)

def p_tipo_dato_decimal(t):
    ' TIPO_DATO : DECIMAL PAR_A ENTERO COMA ENTERO PAR_C'
    t[0] = ExpresionNumero(TIPO_DE_DATOS.decimal,t[3], t[5])

def p_tipo_dato_numerico(t):
    ' TIPO_DATO : NUMERIC PAR_A ENTERO COMA ENTERO PAR_C'
    t[0] = ExpresionNumero(TIPO_DE_DATOS.numeric,t[3],t[5])

def p_tipo_dato_bigint(t):
    ' TIPO_DATO : BIGINT'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.bigint)

def p_tipo_dato_real(t):
    ' TIPO_DATO : REAL'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.real)

def p_tipo_dato_double_precision(t):
    ' TIPO_DATO : DOUBLE PRECISION'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.double_precision)

def p_tipo_dato_interval_to(t):
    ' TIPO_DATO :  INTERVAL extract_time TO extract_time'
    t[0] = Etiqueta_Interval(t[2],t[4], TIPO_DE_DATOS.interval)


def p_tipo_dato_interval(t):
    ' TIPO_DATO :  INTERVAL'
    t[0] = ExpresionTiempo(OPERACION_TIEMPO.YEAR)

def p_tipo_dato_time(t):
    ' TIPO_DATO :  TIME'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.time)

def p_tipo_dato_interval_tsmp(t):
    ' TIPO_DATO :  TIMESTAMP'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.timestamp)

def p_tipo_dato(t):
    'TIPO_DATO : DATE'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.date)

def p_tipo_dato_character_varying(t):
    ' TIPO_DATO : CHARACTER VARYING PAR_A ENTERO PAR_C'
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.character, t[4])

def p_tipo_dato_varchar(t):
    ' TIPO_DATO : VARCHAR PAR_A ENTERO PAR_C'
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.varchar,t[3])

def p_tipo_dato_char(t):
    ' TIPO_DATO : CHAR PAR_A ENTERO PAR_C'
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.char,t[3])

def p_tipo_dato_character(t):
    ' TIPO_DATO : CHARACTER PAR_A ENTERO PAR_C'
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.character,t[3])

def p_tipo_dato_char_no_esp(t):
    ' TIPO_DATO : CHAR PAR_A PAR_C'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.char)

def p_tipo_dato_character_no_esp(t):
    ' TIPO_DATO : CHARACTER PAR_A PAR_C'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.character)

#-------------------------------------------------------------------------
#
#        fin   MODIFICACIONES LopDlMa
#-------------------------------------------------------------------------
#

#--------------------------------------------------------------
' ----------- GRAMATICA PARA LA INSTRUCCION UPDATE ------'
#--------------------------------------------------------------
def p_update_insrt(t):
    ' update_insrt : UPDATE ID SET lista_update WHERE ID IGUAL expresion PTCOMA'
def p_lista_update(t):
    ' lista_update :  lista_update COMA parametro_update'
def p_lista_update_lista(t):
    ' lista_update : parametro_update'
def p_parametro_update(t):
    ' parametro_update : ID IGUAL expresion'
#--------------------------------------------------------------
' ---------- GRAMATICA PARA LA INSTRUCCION DELETE --------'
#--------------------------------------------------------------
def p_delete_insrt(t):
    ' delete_insrt : DELETE FROM ONLY ID PTCOMA'
def p_delete_insert2(t):
    ' delete_insrt : DELETE FROM ONLY ID RETURNING returning_exp PTCOMA'
def p_delete_insrt3(t):
    ' delete_insrt : DELETE FROM ID WHERE EXISTS expresion_logica PTCOMA '
def p_delete_insrt4(t):
    ' delete_insrt : DELETE FROM ID WHERE EXISTS expresion_logica RETURNING returning_exp PTCOMA '
def p_delete_insrt5(t):
    ' delete_insrt : DELETE FROM ID WHERE expresion_logica PTCOMA ' 
def p_delete_insrt6(t):
    ' delete_insrt : DELETE FROM ID WHERE expresion_logica RETURNING returning_exp PTCOMA'
def p_delete_insrt7(t):
    ' delete_insrt : DELETE FROM ID RETURNING returning_exp PTCOMA '
def p_delete_insrt8(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE EXISTS expresion_logica PTCOMA '
def p_delete_insrt9(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE EXISTS expresion_logica RETURNING returning_exp PTCOMA '
def p_delete_insrt10(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE expresion_logica PTCOMA '
def p_delete_insrt11(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE expresion_logica RETURNING returning_exp PTCOMA '
def p_delete_insrt12(t):
    ' delete_insrt : DELETE FROM ID AS ID WHERE EXISTS expresion_logica PTCOMA '
def p_delete_insrt13(t):
    ' delete_insrt : DELETE FROM ID AS ID WHERE EXISTS expresion_logica RETURNING returning_exp PTCOMA '
def p_delete_insrt14(t):
    ' delete_insrt : DELETE FROM ID AS ID WHERE expresion_logica PTCOMA '
def p_delete_insrt15(t):
    ' delete_insrt : DELETE FROM ID AS ID WHERE expresion_logica RETURNING returning_exp PTCOMA '

def p_returning_exp(t):
    ''' returning_exp : ASTERISCO 
                      | campos_c'''
#-------------------------------------------------------------------------
#
#        fin   MODIFICACIONES LopDlMa
#-------------------------------------------------------------------------
#

#--------------------------------------------------------------
' ------------- GRAMATICA PARA LA INSTRUCCION SELECT --------------'
#--------------------------------------------------------------
def p_instruccion_select_insrt(t):
    ' select_insrt : SELECT opcion_select_tm'

def p_instruccion_select_insrt_union(t):
    ' select_insrt : select_insrt UNION select_insrt'

def p_instruccion_select_insrt_intersect(t):
    ' select_insrt : select_insrt INTERSECT select_insrt'

def p_instruccion_select_insrt_except(t):
    ' select_insrt : select_insrt EXCEPT select_insrt'

def p_opcion_select_tm(t):
    'opcion_select_tm :  opcion_select_lista  FROM opcion_from'

def p_opcion_select_tm_op(t):
    'opcion_select_tm : opcion_select_lista AS ID FROM opcion_from'

def p_opcion_select_tm_extract(t):
    'opcion_select_tm : EXTRACT PAR_A extract_time FROM TIMESTAMP CADENA  PAR_C PTCOMA'

def p_opcion_select_tm_date(t):
    'opcion_select_tm : DATE_PART PAR_A CADENA COMA INTERVAL CADENA PAR_C PTCOMA '

def p_opcion_select_tm_now(t):
    'opcion_select_tm : NOW PAR_A PAR_C PTCOMA'

def p_opcion_select_tm_current(t):
    'opcion_select_tm : CURRENT_DATE PTCOMA'

def p_opcion_select_tm_crtm(t):
    'opcion_select_tm : CURRENT_TIME PTCOMA'

def p_opcion_select_tm_timestamp(t):
    'opcion_select_tm : TIMESTAMP CADENA PTCOMA'

#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_1_1_1_1_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_1_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_0_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_0_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_1_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_1_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_0_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_0_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'


def p_opcion_from_1_1_1_1_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_1_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_0_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_0_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_1_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_1_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_0_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_0_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'



def p_opcion_from_1_1_1_1_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_1_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_0_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_0_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_1_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_1_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_0_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_0_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN LIMIT opc_lim OFFSET ENTERO PTCOMA'


#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_1_1_1_1_1_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_1_1_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_0_1_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_0_1_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_1_0_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_1_0_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_0_0_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_0_0_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim PTCOMA'





def p_opcion_from_1_1_1_1_1_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_1_1_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_0_1_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_0_1_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_1_0_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_1_0_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_0_0_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_0_0_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c LIMIT opc_lim PTCOMA'




def p_opcion_from_1_1_1_1_1_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_1_1_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_0_1_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_0_1_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_1_0_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_1_0_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_0_0_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_0_0_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN LIMIT opc_lim PTCOMA'





def p_opcion_from_1_1_1_1_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_0_1_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_1_0_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_0_0_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_1_1_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_0_1_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_1_0_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_0_0_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c orden PTCOMA'





def p_opcion_from_1_1_1_1_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_0_1_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_1_0_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_0_0_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_1_1_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_0_1_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_1_0_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_0_0_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c PTCOMA'




def p_opcion_from_1_1_1_1_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_1_1_0_1_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_1_1_1_0_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica PTCOMA'

def p_opcion_from_1_1_0_0_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica PTCOMA'

def p_opcion_from_1_1_1_1_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  PTCOMA'

def p_opcion_from_1_1_0_1_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  PTCOMA'

def p_opcion_from_1_1_1_0_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where PTCOMA'

def p_opcion_from_1_1_0_0_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN PTCOMA'

    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_1_1_1_1_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_1_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_0_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_1_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_1_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_0_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'



def p_opcion_from_1_1_1_1_1_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_1_1_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_0_1_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_1_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_1_0_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_1_0_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_0_0_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_0_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'




def p_opcion_from_1_1_1_1_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_1_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_0_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_1_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_1_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_0_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN LIMIT opc_lim OFFSET ENTERO'

    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------



def p_opcion_from_1_1_1_1_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_0_1_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_1_0_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_0_0_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_1_1_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_0_1_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_1_0_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_0_0_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim'



def p_opcion_from_1_1_1_1_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_0_1_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_1_0_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_0_0_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_1_1_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_0_1_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_1_0_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_0_0_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c LIMIT opc_lim'



def p_opcion_from_1_1_1_1_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_1_0_1_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_1_1_0_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_1_0_0_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_1_1_1_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_1_1_0_1_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_1_1_1_0_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where LIMIT opc_lim'

def p_opcion_from_1_1_0_0_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN LIMIT opc_lim'



def p_opcion_from_1_1_1_1_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_1_0_1_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_1_1_0_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_1_0_0_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_1_1_1_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_1_1_0_1_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN  GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_1_1_1_0_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c orden'

def p_opcion_from_1_1_0_0_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c orden'




def p_opcion_from_1_1_1_1_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_1_0_1_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_1_1_0_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_1_0_0_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_1_1_1_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_1_1_0_1_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN  GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_1_1_1_0_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c'

def p_opcion_from_1_1_0_0_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c'





def p_opcion_from_1_1_1_1_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_1_1_0_1_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_1_1_1_0_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica'

def p_opcion_from_1_1_0_0_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica'

def p_opcion_from_1_1_1_1_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c '

def p_opcion_from_1_1_0_1_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c '

def p_opcion_from_1_1_1_0_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where'

def p_opcion_from_1_1_0_0_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN '

    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_1_0_1_1_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_1_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_0_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_0_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_1_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_1_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_0_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_0_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'



def p_opcion_from_1_0_1_1_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_1_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_0_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_0_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_1_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_1_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_0_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_0_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'


def p_opcion_from_1_0_1_1_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_1_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_0_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_0_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_1_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_1_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_0_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_0_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre LIMIT opc_lim OFFSET ENTERO PTCOMA'


#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_1_0_1_1_1_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_1_1_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_0_1_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_0_1_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_1_0_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_1_0_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_0_0_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_0_0_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre ORDER BY campos_c orden LIMIT opc_lim PTCOMA'




def p_opcion_from_1_0_1_1_1_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_1_1_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_0_1_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_0_1_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_1_0_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_1_0_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_0_0_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_0_0_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre ORDER BY campos_c LIMIT opc_lim PTCOMA'




def p_opcion_from_1_0_1_1_1_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_1_1_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_0_1_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_0_1_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_1_0_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_1_0_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_0_0_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_0_0_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre LIMIT opc_lim PTCOMA'



def p_opcion_from_1_0_1_1_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_0_1_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_1_0_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_0_0_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_1_1_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_0_1_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_1_0_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_0_0_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre ORDER BY campos_c orden PTCOMA'



def p_opcion_from_1_0_1_1_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_0_1_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_1_0_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_0_0_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_1_1_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_0_1_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_1_0_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_0_0_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre ORDER BY campos_c PTCOMA'




def p_opcion_from_1_0_1_1_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_1_0_0_1_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_1_0_0_1_0_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica PTCOMA'

def p_opcion_from_1_0_0_0_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica PTCOMA'

def p_opcion_from_1_0_1_1_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  PTCOMA'

def p_opcion_from_1_0_0_1_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  PTCOMA'

def p_opcion_from_1_0_1_0_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where PTCOMA'

def p_opcion_from_1_0_0_0_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre PTCOMA'



#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_1_0_1_1_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_1_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_0_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_0_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_1_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_1_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_0_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_0_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'



def p_opcion_from_1_0_1_1_1_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_1_1_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_0_1_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_0_1_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_1_0_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_1_0_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_0_0_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_0_0_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'





def p_opcion_from_1_0_1_1_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_1_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_0_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_0_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_1_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_1_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_0_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_0_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre LIMIT opc_lim OFFSET ENTERO'
    
    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------


def p_opcion_from_1_0_1_1_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_0_1_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_1_0_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_0_0_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_1_1_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_0_1_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_1_0_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_0_0_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre ORDER BY campos_c orden LIMIT opc_lim'



def p_opcion_from_1_0_1_1_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_0_1_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_1_0_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_0_0_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_1_1_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_0_1_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_1_0_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_0_0_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre ORDER BY campos_c LIMIT opc_lim'




def p_opcion_from_1_0_1_1_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_0_0_1_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_0_1_0_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_0_0_0_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_0_1_1_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_1_0_0_1_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_1_0_1_0_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where LIMIT opc_lim'

def p_opcion_from_1_0_0_0_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre LIMIT opc_lim'



def p_opcion_from_1_0_1_1_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_0_0_1_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_0_1_0_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_0_0_0_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_0_1_1_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_1_0_0_1_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_1_0_1_0_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c orden'

def p_opcion_from_1_0_0_0_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre ORDER BY campos_c orden'



def p_opcion_from_1_0_1_1_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_0_0_1_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_0_1_0_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_0_0_0_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_0_1_1_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_1_0_0_1_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_1_0_1_0_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c'

def p_opcion_from_1_0_0_0_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre ORDER BY campos_c'




def p_opcion_from_1_0_1_1_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_1_0_0_1_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_1_0_1_0_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica'

def p_opcion_from_1_0_0_0_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica'

def p_opcion_from_1_0_1_1_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c '

def p_opcion_from_1_0_0_1_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c '

def p_opcion_from_1_0_1_0_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where'

def p_opcion_from_1_0_0_0_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre'


#----------------------------------------------------
#
#               OPCION SOBRENOMBRE 
#
#----------------------------------------------------


#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_0_1_1_1_1_1_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_1_1_1_1_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_0_1_1_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_0_1_1_1_1(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_1_0_1_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_1_0_1_1_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_0_0_1_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_0_0_1_1_1(t):
    'opcion_from : ID INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'





def p_opcion_from_0_1_1_1_1_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_1_1_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_0_1_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_0_1_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_1_0_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_1_0_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_0_0_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_0_0_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'




def p_opcion_from_0_1_1_1_1_0_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_1_1_0_1_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_0_1_0_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_0_1_0_1_1(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_1_0_0_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_1_0_0_1_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_0_0_0_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_0_0_0_1_1(t):
    'opcion_from : ID INNER_JOIN LIMIT opc_lim OFFSET ENTERO PTCOMA'


#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_0_1_1_1_1_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_1_1_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_0_1_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_0_1_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_1_0_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_1_0_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_0_0_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_0_0_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim PTCOMA'





def p_opcion_from_0_1_1_1_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_1_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_0_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_0_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_1_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_1_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_0_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_0_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN ORDER BY campos_c LIMIT opc_lim PTCOMA'


def p_opcion_from_0_1_1_1_1_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_1_1_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_0_1_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_0_1_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_1_0_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_1_0_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_0_0_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_0_0_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN LIMIT opc_lim PTCOMA'




def p_opcion_from_0_1_1_1_1_1_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_0_1_1_1_0_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_1_0_1_1_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_0_0_1_1_0_1(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_1_1_0_1_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_0_1_0_1_0_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_1_0_0_1_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_0_0_0_1_0_1(t):
    'opcion_from : ID INNER_JOIN ORDER BY campos_c orden PTCOMA'



def p_opcion_from_0_1_1_1_1_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_0_1_1_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_1_0_1_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_0_0_1_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_1_1_0_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_0_1_0_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_1_0_0_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_0_0_0_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN ORDER BY campos_c PTCOMA'




def p_opcion_from_0_1_1_1_1_0_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_0_1_0_1_1_0_0_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_0_1_1_0_1_0_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica PTCOMA'

def p_opcion_from_0_1_0_0_1_0_0_1(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica PTCOMA'

def p_opcion_from_0_1_1_1_0_0_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  PTCOMA'

def p_opcion_from_0_1_0_1_0_0_0_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  PTCOMA'

def p_opcion_from_0_1_1_0_0_0_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where PTCOMA'

def p_opcion_from_0_1_0_0_0_0_0_1(t):
    'opcion_from : ID INNER_JOIN PTCOMA'

#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------
def p_opcion_from_0_1_1_1_1_1_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_1_1_1_1_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_0_1_1_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_0_1_1_1_0(t):
    'opcion_from :  ID INNER_JOIN  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_1_0_1_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_1_0_1_1_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_1_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_0_0_1_1_0(t):
    'opcion_from :  ID INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'



def p_opcion_from_0_1_1_1_1_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_1_1_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_0_1_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_0_1_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_1_0_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_1_0_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_0_0_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'



def p_opcion_from_0_1_1_1_1_0_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_1_1_0_1_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_0_1_0_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_0_1_0_1_0(t):
    'opcion_from :  ID INNER_JOIN HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_1_0_0_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_1_0_0_1_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_0_0_0_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_0_0_0_1_0(t):
    'opcion_from :  ID INNER_JOIN LIMIT opc_lim OFFSET ENTERO'

    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------
def p_opcion_from_0_1_1_1_1_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_1_0_1_1_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_1_1_0_1_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_1_0_0_1_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_1_1_1_0_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_1_0_1_0_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_0_0_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_1_0_0_0_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim'





def p_opcion_from_0_1_1_1_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_1_0_1_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_1_1_0_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_1_0_0_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_1_1_1_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_1_0_1_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_0_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_1_0_0_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN ORDER BY campos_c LIMIT opc_lim'






def p_opcion_from_0_1_1_1_1_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_1_0_1_1_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_1_1_0_1_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_1_0_0_1_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_1_1_1_0_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_0_1_0_1_0_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_0_1_1_0_0_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where LIMIT opc_lim'

def p_opcion_from_0_1_0_0_0_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN LIMIT opc_lim'







def p_opcion_from_0_1_1_1_1_1_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_1_0_1_1_1_0_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_1_1_0_1_1_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_1_0_0_1_1_0_0(t):
    'opcion_from :  ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_1_1_1_0_1_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_0_1_0_1_0_1_0_0(t):
    'opcion_from :  ID INNER_JOIN  GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_0_1_1_0_0_1_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where ORDER BY campos_c orden'

def p_opcion_from_0_1_0_0_0_1_0_0(t):
    'opcion_from :  ID INNER_JOIN ORDER BY campos_c orden'





def p_opcion_from_0_1_1_1_1_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_1_0_1_1_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_1_1_0_1_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_1_0_0_1_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_1_1_1_0_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_0_1_0_1_0_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN  GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_0_1_1_0_0_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where ORDER BY campos_c'

def p_opcion_from_0_1_0_0_0_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN ORDER BY campos_c'





def p_opcion_from_0_1_1_1_1_0_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_0_1_0_1_1_0_0_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_0_1_1_0_1_0_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica'

def p_opcion_from_0_1_0_0_1_0_0_0(t):
    'opcion_from :  ID INNER_JOIN HAVING expresion_logica'

def p_opcion_from_0_1_1_1_0_0_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c '

def p_opcion_from_0_1_0_1_0_0_0_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c '

def p_opcion_from_0_1_1_0_0_0_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where'

def p_opcion_from_0_1_0_0_0_0_0_0(t):
    'opcion_from :  ID INNER_JOIN '


#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------
def p_opcion_from_0_0_1_1_1_1_1_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_1_1_1_1_1(t):
    'opcion_from : ID GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_0_1_1_1_1(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_0_1_1_1_1(t):
    'opcion_from : ID HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_1_0_1_1_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_1_0_1_1_1(t):
    'opcion_from : ID GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_0_0_1_1_1(t):
    'opcion_from : ID WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_0_0_1_1_1(t):
    'opcion_from : ID ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'




def p_opcion_from_0_0_1_1_1_1_1_1_ordenno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_1_1_1_1_1_ordenno(t):
    'opcion_from : ID GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_0_1_1_1_1_ordenno(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_0_1_1_1_1_ordenno(t):
    'opcion_from : ID HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_1_0_1_1_1_ordenno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_1_0_1_1_1_ordenno(t):
    'opcion_from : ID GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_0_0_1_1_1_ordenno(t):
    'opcion_from : ID WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_0_0_1_1_1_ordenno(t):
    'opcion_from : ID ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'





def p_opcion_from_0_0_1_1_1_0_1_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_1_1_0_1_1(t):
    'opcion_from : ID GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_0_1_0_1_1(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_0_1_0_1_1(t):
    'opcion_from : ID HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_1_0_0_1_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_1_0_0_1_1(t):
    'opcion_from : ID GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_0_0_0_1_1(t):
    'opcion_from : ID WHERE expresion_where LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_0_0_0_1_1(t):
    'opcion_from : ID LIMIT opc_lim OFFSET ENTERO PTCOMA'

    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------
def p_opcion_from_0_0_1_1_1_1_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_1_1_1_1_1_offno(t):
    'opcion_from : ID GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_0_1_1_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_0_1_1_1_1_offno(t):
    'opcion_from : ID HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_1_0_1_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_1_0_1_1_1_offno(t):
    'opcion_from : ID GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_0_0_1_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_0_0_1_1_1_offno(t):
    'opcion_from : ID ORDER BY campos_c orden LIMIT opc_lim PTCOMA'



def p_opcion_from_0_0_1_1_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_1_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_0_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_0_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_1_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_1_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_0_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID WHERE expresion_where ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_0_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID ORDER BY campos_c LIMIT opc_lim PTCOMA'





def p_opcion_from_0_0_1_1_1_0_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_1_1_0_1_1_offno(t):
    'opcion_from : ID GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_0_1_0_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_0_1_0_1_1_offno(t):
    'opcion_from : ID HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_1_0_0_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_1_0_0_1_1_offno(t):
    'opcion_from : ID GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_0_0_0_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_0_0_0_1_1_offno(t):
    'opcion_from : ID LIMIT opc_lim PTCOMA'

    



def p_opcion_from_0_0_1_1_1_1_0_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_0_1_1_1_0_1(t):
    'opcion_from : ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_1_0_1_1_0_1(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_0_0_1_1_0_1(t):
    'opcion_from : ID HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_1_1_0_1_0_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_0_1_0_1_0_1(t):
    'opcion_from : ID GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_1_0_0_1_0_1(t):
    'opcion_from : ID WHERE expresion_where ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_0_0_0_1_0_1(t):
    'opcion_from : ID ORDER BY campos_c orden PTCOMA'


def p_opcion_from_0_0_1_1_1_1_0_1_ordeno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_0_1_1_1_0_1_ordeno(t):
    'opcion_from : ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_1_0_1_1_0_1_ordeno(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_0_0_1_1_0_1_ordeno(t):
    'opcion_from : ID HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_1_1_0_1_0_1_ordeno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_0_1_0_1_0_1_ordeno(t):
    'opcion_from : ID GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_1_0_0_1_0_1_ordeno(t):
    'opcion_from : ID WHERE expresion_where ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_0_0_0_1_0_1_ordeno(t):
    'opcion_from : ID ORDER BY campos_c PTCOMA'



def p_opcion_from_0_0_1_1_1_0_0_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_0_0_0_1_1_0_0_1(t):
    'opcion_from : ID GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_0_0_0_1_0_1_0_0_1(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica PTCOMA'

def p_opcion_from_0_0_0_0_1_0_0_1(t):
    'opcion_from : ID HAVING expresion_logica PTCOMA'

def p_opcion_from_0_0_1_1_0_0_0_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  PTCOMA'

def p_opcion_from_0_0_0_1_0_0_0_1(t):
    'opcion_from : ID GROUP BY campos_c  PTCOMA'

def p_opcion_from_0_0_1_0_0_0_0_1(t):
    'opcion_from : ID WHERE expresion_where PTCOMA'

def p_opcion_from_0_0_0_0_0_0_0_1(t):
    'opcion_from : ID PTCOMA'



#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------
def p_opcion_from_0_0_1_1_1_1_1_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_1_1_1_1_0(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_0_1_1_1_0(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_0_1_1_1_0(t):
    'opcion_from :  ID HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_1_0_1_1_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_1_0_1_1_0(t):
    'opcion_from :  ID GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_0_0_1_1_0(t):
    'opcion_from :  ID WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_0_0_1_1_0(t):
    'opcion_from :  ID ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'




def p_opcion_from_0_0_1_1_1_1_1_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_1_1_1_1_0_ordeno(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_0_1_1_1_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_0_1_1_1_0_ordeno(t):
    'opcion_from :  ID HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_1_0_1_1_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_1_0_1_1_0_ordeno(t):
    'opcion_from :  ID GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_0_0_1_1_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_0_0_1_1_0_ordeno(t):
    'opcion_from :  ID ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'




def p_opcion_from_0_0_1_1_1_0_1_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_1_1_0_1_0(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_0_1_0_1_0(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_0_1_0_1_0(t):
    'opcion_from :  ID HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_1_0_0_1_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_1_0_0_1_0(t):
    'opcion_from :  ID GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_0_0_0_1_0(t):
    'opcion_from :  ID WHERE expresion_where LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_0_0_0_1_0(t):
    'opcion_from :  ID LIMIT opc_lim OFFSET ENTERO'

    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_0_0_1_1_1_1_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_0_1_1_1_1_0_offno(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_1_0_1_1_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_0_0_1_1_1_0_offno(t):
    'opcion_from :  ID HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_1_1_0_1_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_0_1_0_1_1_0_offno(t):
    'opcion_from :  ID GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_1_0_0_1_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_0_0_0_1_1_0_offno(t):
    'opcion_from :  ID ORDER BY campos_c orden LIMIT opc_lim'





def p_opcion_from_0_0_1_1_1_1_1_0_offno_ordeno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_0_1_1_1_1_0_offno_ordeno(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_1_0_1_1_1_0_offno_ordeno(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_0_0_1_1_1_0_offno_ordeno(t):
    'opcion_from :  ID HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_1_1_0_1_1_0_offno_ordeno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_0_1_0_1_1_0_offno_ordeno(t):
    'opcion_from :  ID GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_1_0_0_1_1_0_offno_ordeno(t):
    'opcion_from :  ID WHERE expresion_where ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_0_0_0_1_1_0_offno_ordeno(t):
    'opcion_from :  ID ORDER BY campos_c LIMIT opc_lim'





def p_opcion_from_0_0_1_1_1_0_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_0_0_1_1_0_1_0_offno(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_0_1_0_1_0_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_0_0_0_1_0_1_0_offno(t):
    'opcion_from :  ID HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_0_1_1_0_0_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_0_0_0_1_0_0_1_0_offno(t):
    'opcion_from :  ID GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_0_0_1_0_0_0_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where LIMIT opc_lim'

def p_opcion_from_0_0_0_0_0_0_1_0_offno(t):
    'opcion_from :  ID LIMIT opc_lim'




def p_opcion_from_0_0_1_1_1_1_0_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_0_0_1_1_1_0_0(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_0_1_0_1_1_0_0(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_0_0_0_1_1_0_0(t):
    'opcion_from :  ID HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_0_1_1_0_1_0_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_0_0_0_1_0_1_0_0(t):
    'opcion_from :  ID GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_0_0_1_0_0_1_0_0(t):
    'opcion_from :  ID WHERE expresion_where ORDER BY campos_c orden'

def p_opcion_from_0_0_0_0_0_1_0_0(t):
    'opcion_from :  ID ORDER BY campos_c orden'




def p_opcion_from_0_0_1_1_1_1_0_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_0_0_1_1_1_0_0_ordeno(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_0_1_0_1_1_0_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_0_0_0_1_1_0_0_ordeno(t):
    'opcion_from :  ID HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_0_1_1_0_1_0_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_0_0_0_1_0_1_0_0_ordeno(t):
    'opcion_from :  ID GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_0_0_1_0_0_1_0_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where ORDER BY campos_c'

def p_opcion_from_0_0_0_0_0_1_0_0_ordeno(t):
    'opcion_from :  ID ORDER BY campos_c'









def p_opcion_from_0_0_1_1_1_0_0_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_0_0_0_1_1_0_0_0(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_0_0_1_0_1_0_0_0(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica'

def p_opcion_from_0_0_0_0_1_0_0_0(t):
    'opcion_from :  ID HAVING expresion_logica'

def p_opcion_from_0_0_1_1_0_0_0_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c '

def p_opcion_from_0_0_0_1_0_0_0_0(t):
    'opcion_from :  ID GROUP BY campos_c '

def p_opcion_from_0_0_1_0_0_0_0_0(t):
    'opcion_from :  ID WHERE expresion_where'

def p_opcion_from_0_0_0_0_0_0_0(t):
    'opcion_from :  ID'




def p_opcion_from_2(t):
    'opcion_from :  PAR_A select_insrt PAR_C ID PTCOMA'

def p_opcion_from_3(t):
    'opcion_from :  PAR_A select_insrt PAR_C PTCOMA'


#----------------------------------------------------
#
#               TERMINO SELECT TABLE 
#
#----------------------------------------------------


def p_extract_time(t):
    ''' extract_time : YEAR
                    | DAY
                    | MONTH
                    | HOUR
                    | MINUTE
                    | SECOND '''

def p_sobre_Nombre(t):
    ''' opcion_sobrenombre : AS ID
                            | ID'''

def p_empty(p):
    'empty :  '
    pass  

def p_opc_lim(t):
    '''opc_lim : ENTERO
               | ASTERISCO '''


def p_ORDER(t):
    ''' orden : DESC
              | ASC '''


def p_expresion_where(t):
    ''' expresion_where : expresion_logica
                        | expresion BETWEEN expresion AND expresion 
                        | expresion NOT BETWEEN expresion AND expresion
                        | expresion BETWEEN SYMMETRIC expresion AND expresion
                        | expresion NOT BETWEEN SYMMETRIC expresion AND expresion
                        | expresion IS DISTINCT FROM expresion
                        | expresion IS NOT DISTINCT FROM expresion 
                        | expresion IS NOT DISTINCT FROM expresion AND expresion
                        | expresion IS NULL
                        | expresion IS NOT NULL
                        | expresion ISNULL
                        | expresion NOTNULL
                        | expresion IS TRUE
                        | expresion IS FALSE
                        | expresion IS NOT TRUE
                        | expresion IS NOT FALSE
                        | expresion IS UNKNOWN
                        | expresion IS NOT UNKNOWN '''

#----------terminar el distinct ------------
def p_select_lista(t):
    ''' opcion_select_lista : DISTINCT campos_c
                            | opciones_select_lista'''
            
def p_opciones_select_lista(t):
    ''' opciones_select_lista : opciones_select_lista COMA opcion_select
                              | opcion_select '''


#def p_opcion_select_lista(t):
 #   ' opcion_select_lista : opcion_select '

def p_opcion_select(t):
    ''' opcion_select : case_insrt
                      | PAR_A select_insrt PAR_C
                      | expresion'''

' ---------- GRAMATICA PARA LA INSTRUCCION DE CASE --------------'
def p_case_insrt(t):
    ' case_insrt : CASE estructura_when_lista ELSE expresion END '


def p_estructura_when_lista(t):
    ' estructura_when_lista : estructura_when_lista estructura_when '

def p_opcion_estructura_when(t):
    ' estructura_when_lista : estructura_when'

def p_estructura_when(t):
    ' estructura_when : WHEN expresion_logica THEN expresion'

' ---------- GRAMATICA PARA LA INSTRUCCION DE  JOIN ----------'
def p_INNER_JOIN(t):
    ' INNER_JOIN : join_lista JOIN ID opcional_join '

def p_join_lista(t):
    '''join_lista : INNER
                  | OUTER
                  | LEFT  
                  | RIGHT
                  | FULL
                  | NATURAL '''

def p_opcional_join(t):
    ' opcional_join : AS ID ON CONDICION_INNER_JOIN'

def p_opcional_join_on(t):
    ' opcional_join :  ON expresion_relacional'

def p_optional_join_using(t):
    ' opcional_join :  USING PAR_A campos_c PAR_C'

def p_optional_join_join(t):
    ' opcional_join : JOIN ID'


def p_CONDICION_INNER_JOIN(t):
    'CONDICION_INNER_JOIN : expresion_logica'

' ---------- GRAMATICA PARA LA INSTRUCCION DE SUM ----------'
def p_sum_insert(t):
    ' sum_insrt : SUM agrupacion_expresion'

' ---------- GRAMATICA PAR LA INSTRUCCIONN DE COUNT ---------'
def p_count_insrt(t):
    ' count_insrt : COUNT agrupacion_expresion '

' --------- GRAMATICA PARA LA INSTRUCCION INSERT  -------'

def p_insert_insrt(t):
    ' insert_insrt : INSERT INTO ID PAR_A opcion_lista_parametros_lista PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA '

def p_opcion_lista_parametros_lista(t):
    ''' opcion_lista_parametros_lista : lista_parametros_lista
                                     | empty '''

' -------- GRAMATICA PARA LA LISTA DE PARAMETROS DEL INSERT ----------'

def p_lista_parametros_lista(t):
    ' lista_parametros_lista : lista_parametros_lista COMA lista_parametros'

def p_lista_parametros(t):
    ' lista_parametros_lista : lista_parametros'

def p_parametros(t):
    ' lista_parametros : ID'

'------- GRAMATICA PARA LA LISTA DE DATOS DEL INSERT -------' 

def p_parametros_lista_datos(t):
    ' lista_datos : lista_datos COMA expresion_relacional'

def p_expresion_lista(t):
    ' lista_datos : expresion_relacional'

def p_agrupacion_expresion(t):
    ' agrupacion_expresion : PAR_A expresion PAR_C'
    t[0] = t[2]

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = ExpresionComillaSimple(t[1])


def p_expresion1(t):
    '''expresion : ENTERO 
                   | FLOTANTE'''
    t[0] = ExpresionEntero(t[1])               


def p_expresion3(t):
    'expresion : ID'
    t[0] = ExpresionIdentificador(t[1])                  
                      
def p_expresion4(t):
    ' expresion : ID PUNTO ID '
    t[0] = ExpresionIdentificadorDoble(t[1],t[3])   

def p_expresion(t):
    '''expresion : expresion SUMA expresion 
                 | expresion RESTA expresion
                 | expresion DIVISION expresion
                 | expresion ASTERISCO expresion '''
    
    if t[2] == '+' : t[0] = ExpresionBinaria(t[1],t[3], OPERACION_ARITMETICA.MAS)
    if t[2] == '-' : t[0] = ExpresionBinaria(t[1],t[3], OPERACION_ARITMETICA.MENOS)
    if t[2] == '*' : t[0] = ExpresionBinaria(t[1],t[3], OPERACION_ARITMETICA.ASTERISCO)
    if t[2] == '/' : t[0] = ExpresionBinaria(t[1],t[3], OPERACION_ARITMETICA.DIVIDIDO)
   

def p_expresion_boolean(t):
    ''' expresion :  TRUE
                    | FALSE'''
    t[0] = ExpresionBooleana(t[1])
                         

def p_sin_some_any(t):
    '''sin_some_any : SOME
                    | ANY  '''

def p_string_type(t):
    ''' string_type : CADENA
                     | ID '''
    t[0] = ExpresionIdentificador(t[1])

' --------------- EXPRESIONES -----------------------'
def p_expresion_relacional(t):
    ''' expresion_relacional : expresion MAYQUE expresion
                             | expresion MENQUE expresion
                             | expresion MAYIGQUE expresion
                             | expresion MENIGQUE expresion
                             | expresion DOBLEIG expresion
                             | expresion IGUAL expresion
                             | expresion NOIG expresion
                             | expresion NOIGUAL expresion'''
    
    if t[2] == '>' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.MAYQUE)
    if t[2] == '<' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.MENQUE)
    if t[2] == '>=' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.MAYIGQUE)
    if t[2] == '<=' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.MENIGQUE)
    if t[2] == '==' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.DOBLEIGUAL)
    if t[2] == '<>' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.NOIG)
    if t[2] == '!=' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.DIFERENTE)

def p_expresion_relacional_exp(t):
    ' expresion_relacional : expresion '
    t[0] = t[1]

def p_expresion_logica_AND(t):
    ' expresion_logica : expresion_relacional AND expresion_relacional'
    t[0] = ExpresionLogica(t[1],t[3], OPERACION_LOGICA.AND) 

def p_expresion_logica_OR(t):
    ' expresion_logica : expresion_relacional OR expresion_relacional'
    t[0] = ExpresionLogica(t[1],t[3], OPERACION_LOGICA.OR) 

def p_expresion_logica_not(t):
    ''' expresion_logica : NOT expresion_relacional'''
    t[0] = ExpresionLogica(t[1],'', OPERACION_LOGICA.NOT)

def p_expresion_logica_rel(t):
    ''' expresion_logica : expresion_relacional''' 
    t[0] = t[1]




def p_error(t):
    print("Error sintáctico en '%s'" % t.value, str(t.lineno),find_column(str(input), t))
    global reporte_sintactico
    reporte_sintactico += "<tr> <td> Sintactico </td> <td>" + t.value + "</td>" + "<td>" + str(t.lineno) + "</td> <td> "+ str(find_column(str(input),t))+"</td></th>"
    

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    print((token.lexpos - line_start) + 1)
    return (token.lexpos - line_start) + 1

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)