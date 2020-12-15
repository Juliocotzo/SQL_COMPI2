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
    'foreing' : 'FOREING',
    'avg' : 'AVG',
    'min' : 'MIN',
    'max' : 'MAX',
    'between' : 'BETWEEN',
    'having' : 'HAVING',
    #----- FUNCIONES TRIGONOMETRICAS -----------
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
    'outer' : 'OUTER',
    #------CREATE DB --------------------
    'if' : 'IF',
    'replace' : 'REPLACE',
    'mode' : 'MODE',
    
    'exists' : 'EXISTS'
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
def p_instruccion_f_create_table(t):
    'instruccion : create_Table_isnrt'

def p_instruccion_f_select(t):
    'instruccion : select_insrt'


def p_instruccion_f_insert(t):
    'instruccion : insert_insrt'

def p_instruccion_f_delete(t):
    'instruccion : delete_insrt'

def p_instruccion_f_update(t):
    'instruccion : update_insrt'
    t[0] = t[1]

def p_instruccion_f_createDB(t):
    'instruccion : createDB_insrt'

def p_instruccion_f_drop(t):
    'instruccion : drop_insrt'
    t[0] = t[1]

def p_instruccion_f_alterDB(t):
    'instruccion : alterDB_insrt'
    t[0] = t[1]

def p_instruccion_f_altertable(t):
    'instruccion : alterTable_insrt'
    t[0] = t[1]

def p_instruccion_f_useDB(t):
    'instruccion : USE ID DATABASE PTCOMA'
    t[0] = Use_DB(t[2])

def p_instruccion_f_tipoenum(t):
    'instruccion : TIPO_ENUM_INSRT'
    t[0] = t[1]
#-------------------------------------------------------------------------
#
#          FIN MODIFICACIONES LopDlMa
#-------------------------------------------------------------------------
#----------------------------------------------------------------
' -----------GRAMATICA PARA LA INSTRUCCION CREATE DB------------'
#----------------------------------------------------------------

#***********************************************
'             CREATE DATABASE SIMPLE '
#************************************************

def p_createDB(t):
    'createDB_insrt : CREATE DATABASE ID PTCOMA'

def p_createDB_wRP(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID PTCOMA'

def p_createDB_wIfNot(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID PTCOMA'

def p_createDB_wRP_wIN(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA'

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
#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION TIPO ENUM ----------'
#--------------------------------------------------------------
def p_Create_Type_Enum(t):
    ' TIPO_ENUM_INSRT : CREATE TYPE ID AS ENUM PAR_A lista_datos PAR_C PTCOMA'
    t[0] = Create_type(t[3],t[7])

#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION DROP TABLE----------'
#--------------------------------------------------------------
def p_dropTable(t):
    ' drop_insrt : DROP TABLE lista_drop_id PTCOMA'
    t[0] = Crear_Drop(t[3])

def p_lista_tabla_lista(t):
    ' lista_drop_id :   lista_drop_id COMA ID '
    t[1].append(ExpresionIdentificador(t[3]))
    t[0] = t[1]

def p_lista_tabla_lista2(t):
    ' lista_drop_id : ID '
    t[0] = [ExpresionIdentificador(t[1])]
#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION ALTER DATABASE ---------'
#--------------------------------------------------------------
def p_AlterDB_opc1(t):
    ' alterDB_insrt : ALTER DATABASE ID RENAME TO ID PTCOMA'
    t[0] = Create_Alterdatabase(t[3],t[6])
def p_AlterDB_opc2(t):
    ' alterDB_insrt : ALTER DATABASE ID OWNER TO usuariosDB PTCOMA'
    t[0] = Create_Alterdatabase(t[3],t[6]) 
def p_usuarioDB(t):
    ' usuariosDB :  ID '
    t[0] = ExpresionIdentificador(t[1])
def p_usuarioDB2(t):
    ' usuariosDB : CURRENT_USER '
    t[0] = ExpresionIdentificador(t[1])
def p_usuarioDB3(t):
    ' usuariosDB : SESSION_USER '
    t[0] = ExpresionIdentificador(t[1])
def p_usuarioDB4(t):
    ' usuariosDB : CADENA '
    t[0] = ExpresionComillaSimple(t[1])
#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION ALTER TABLE ---------'
#--------------------------------------------------------------
def p_Table_alter(t):
    'Table_alter : ALTER COLUMN ID TYPE TIPO_DATO'
    if t[5][0] == 'VARCHAR':
        t[0] = Create_sub_altersimple(t[3],TIPO_DE_DATOS.varchar,t[5][1],None)
    elif t[5][0] == 'DECIMAL':
        t[0] = Create_sub_altersimple(t[3],TIPO_DE_DATOS.decimal,t[5][1],t[5][2])
    elif t[5][0] == 'NUMERIC':
        t[0] = Create_sub_altersimple(t[3],TIPO_DE_DATOS.numeric,t[5][1],t[5][2])
    elif t[5][0] == 'VARING':
        t[0] = Create_sub_altersimple(t[3],TIPO_DE_DATOS.varing,t[5][1],None)
    elif t[5][0] == 'CHAR':
        t[0] = Create_sub_altersimple(t[3],TIPO_DE_DATOS.char,t[5][1],None)
    elif t[5][0] == 'CHARACTER':
        t[0] = Create_sub_altersimple(t[3],TIPO_DE_DATOS.character,t[5][1],None)
    elif t[5][0] == 'INTERVAL':
        t[0] = Create_sub_altersimple(t[3],TIPO_DE_DATOS.interval,t[5][1],t[5][2])
    else:
        t[0] = Create_sub_altersimple(t[3],t[5][0],None,None)

def p_alterTable3(t):
    'alterTable_insrt : ALTER TABLE ID DROP CONSTRAINT campos_c PTCOMA'
    t[0] = Create_altertable_drop(t[3],t[6])

def p_alterTable4(t):
    'alterTable_insrt : ALTER TABLE ID RENAME COLUMN ID TO ID PTCOMA'
    t[0] = Create_altertable_rename(t[3],t[6],t[8])

def p_alterTable5(t):
    'alterTable_insrt : ALTER TABLE ID ADD COLUMN campos_add_Column PTCOMA' 
    t[0] = Create_altertable_addcolumn(t[3],t[6])

def p_alterTable_add_column(t):
    'campos_add_Column : campos_add_Column COMA ID TIPO_DATO '
    t[1].append(Create_addcolumna(t[3],t[4]))
    t[0] = t[1]

def p_alterTable_add_columna(t):
    'campos_add_Column : ID TIPO_DATO '
    t[0] = [Create_addcolumna(t[1],t[2])]

def p_alterTable6(t):
    'alterTable_insrt : ALTER TABLE ID ADD CHECK PAR_A expresion_logica PAR_C PTCOMA' 
    t[0] =  Create_addcheck(t[3],t[7])

def p_alterTable8(t):
    'alterTable_insrt : ALTER TABLE ID ADD FOREIGN KEY PAR_A campos_c PAR_C REFERENCES campos_c PTCOMA' 
    t[0] = Create_addforeign(t[3],t[8],t[11])
     
def p_alterTable7(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID CHECK PAR_A expresion_logica PAR_C PTCOMA'  
    t[0] = Create_const_check(t[3],t[6],None)

def p_constraint_esp(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PAR_A campos_c PAR_C PTCOMA'
    t[0] = Create_const_unique(t[3],t[6],t[9])

def p_constraint_esp_1(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PAR_A campos_c PAR_C REFERENCES campos_c PTCOMA'
    t[0] = Create_const_foreign(t[3],t[6],t[10],t[13])

def p_alterTable2(t):
    'alterTable_insrt : ALTER TABLE ID alterTable_alter PTCOMA'
    t[0] = Create_altertable_simple(t[3],t[4])

def p_alerTable_alter(t):
    'alterTable_alter : alterTable_alter COMA Table_alter'
    t[1].append(t[3])
    t[0] = t[1]

def p_alerTable_alter_1(t):
    'alterTable_alter : Table_alter'
    t[0] = [t[1]]

def p_Table_alter2(t):
    'Table_alter : ALTER COLUMN ID SET NOT NULL'
    t[0] = Create_sub_altersimple(t[3],"NULL",None,None)
                 
def p_cons_campos(t):
    'campos_c : campos_c COMA ID'
    t[1].append(ExpresionIdentificador(t[3]))
    t[0] = t[1]

def p_cons_campos2(t):
    'campos_c : ID'
    t[0] = [ExpresionIdentificador(t[1])]
#-------------------------------------------------------------------------
#           MODIFICACIONES LopDlMa
#-------------------------------------------------------------------------
' ---------- GRAMATICA PARA LA INSTRUCCION CREATE TABLE ---------'

def p_create_table(t):
    ' create_Table_isnrt : CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C opcion_herencia '

def p_herencia(t):
    ' opcion_herencia : INHERITS PAR_A ID PAR_C PTCOMA '

def p_herencia_fin(t):
    ' opcion_herencia :  PTCOMA '

def p_cuerpo_createTable_lista(t):
    ' cuerpo_createTable_lista : cuerpo_createTable_lista COMA cuerpo_createTable'

def p_cuerpo_createTable(t):
    ' cuerpo_createTable_lista : cuerpo_createTable'

def p_createTable(t):
    ' cuerpo_createTable :  ID TIPO_DATO '

def p_createTable_id_pk(t):
    ' cuerpo_createTable : ID TIPO_DATO PRIMARY KEY'

def p_createTable_id_ref(t):
    ' cuerpo_createTable : ID TIPO_DATO REFERENCES ID'

def p_createTable_id_not_null(t):
    ' cuerpo_createTable : ID TIPO_DATO NOT NULL'

def p_createTable_null(t):
    ' cuerpo_createTable : ID TIPO_DATO NULL'

def p_createTable_pk(t):
    ' cuerpo_createTable :  PRIMARY KEY PAR_A campos_c PAR_C'

def p_createTable_fk(t):
    ' cuerpo_createTable : FOREING KEY PAR_A campos_c PAR_C REFERENCES ID PAR_A campos_c PAR_C'

def p_createTable_unique(t):
    ' cuerpo_createTable : UNIQUE PAR_A campos_c PAR_C '

def p_createTable_constraint(t):
    ' cuerpo_createTable : CONSTRAINT ID '''

def p_tipo_dato_text(t):
    ' TIPO_DATO : TEXT'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato_float(t):
    ' TIPO_DATO : FLOAT'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato_integer(t):
    ' TIPO_DATO : INTEGER'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato_smallint(t):
    ' TIPO_DATO : SMALLINT'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato_money(t):
    ' TIPO_DATO : MONEY'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato_decimal(t):
    ' TIPO_DATO : DECIMAL PAR_A ENTERO COMA ENTERO PAR_C'
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    temp.append(t[5])
    t[0] = temp

def p_tipo_dato_numerico(t):
    ' TIPO_DATO : NUMERIC PAR_A ENTERO COMA ENTERO PAR_C'
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    temp.append(t[5])
    t[0] = temp

def p_tipo_dato_bigint(t):
    ' TIPO_DATO : BIGINT'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato_real(t):
    ' TIPO_DATO : REAL'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato_double_precision(t):
    ' TIPO_DATO : DOUBLE PRECISION'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato_interval_to(t):
    ' TIPO_DATO : INTERVAL extract_time TO extract_time'
    temp = []
    temp.append(t[1].upper())
    temp.append(t[2])
    temp.append(t[4])
    t[0] = temp

def p_tipo_dato_interval(t):
    ' TIPO_DATO :  INTERVAL'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato_time(t):
    ' TIPO_DATO :  TIME'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato_interval_tsmp(t):
    ' TIPO_DATO :  TIMESTAMP'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato(t):
    'TIPO_DATO : DATE'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato_character_varying(t):
    ' TIPO_DATO : CHARACTER VARYING PAR_A ENTERO PAR_C'
    temp = []
    temp.append(t[2].upper())
    temp.append(t[3])
    t[0] = temp

def p_tipo_dato_varchar(t):
    ' TIPO_DATO : VARCHAR PAR_A ENTERO PAR_C'
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    t[0] = temp

def p_tipo_dato_char(t):
    ' TIPO_DATO : CHAR PAR_A ENTERO PAR_C'
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    t[0] = temp

def p_tipo_dato_character(t):
    ' TIPO_DATO : CHARACTER PAR_A ENTERO PAR_C'
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    t[0] = temp

def p_tipo_dato_char_no_esp(t):
    ' TIPO_DATO : CHAR PAR_A PAR_C'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp

def p_tipo_dato_character_no_esp(t):
    ' TIPO_DATO : CHARACTER PAR_A PAR_C'
    temp = []
    temp.append(ExpresionIdentificador(t[1]))
    t[0] = temp
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
    t[0] = Create_update(t[2],t[6],t[8],t[4])
def p_lista_update(t):
    ' lista_update :  lista_update COMA parametro_update'
    t[1].append(t[3])
    t[0] = t[1]
def p_lista_update_lista(t):
    ' lista_update : parametro_update'
    t[0] = t[1]
def p_parametro_update(t):
    ' parametro_update : ID IGUAL expresion'
    t[0] = [Create_Parametro_update(ExpresionIdentificador(t[1]),t[3])]
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
    ' delete_insrt : DELETE FROM ID AS as_ID WHERE EXISTS expresion_logica PTCOMA '
def p_delete_insrt13(t):
    ' delete_insrt : DELETE FROM ID AS as_ID WHERE EXISTS expresion_logica RETURNING returning_exp PTCOMA '
def p_delete_insrt14(t):
    ' delete_insrt : DELETE FROM ID AS as_ID WHERE expresion_logica PTCOMA '
def p_delete_insrt15(t):
    ' delete_insrt : DELETE FROM ID AS as_ID WHERE expresion_logica RETURNING returning_exp PTCOMA '

def p_returning_exp(t):
    ''' returning_exp : ASTERISCO 
                      | campos_c'''

def p_as_id(t):
    ''' as_ID :   ID
                | CADENA '''
#-------------------------------------------------------------------------
#
#        fin   MODIFICACIONES LopDlMa
#-------------------------------------------------------------------------
#

#--------------------------------------------------------------
' ------------- GRAMATICA PARA LA INSTRUCCION SELECT --------------'
#--------------------------------------------------------------
def p_instruccion_select_insrt(t):
    ' select_insrt : SELECT DISTINCT campos_c FROM ID PTCOMA'
   
def p_instruccion_select_insrt_union(t):
    ' select_insrt : select_insrt UNION select_insrt'
    
def p_instruccion_select_insrt_intersect(t):
    ' select_insrt : select_insrt INTERSECT select_insrt'
    
def p_instruccion_select_insrt_except(t):
    ' select_insrt : select_insrt EXCEPT select_insrt'
    
def p_opcion_select_tm(t):
    'opcion_select_tm :  opcion_select_lista  FROM opcion_from'

def p_opcion_select_tm_op(t):
    'opcion_select_tm : opcion_select_lista AS as_ID FROM opcion_from'

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
    t[0] = ExpresionIdentificador(t[1])




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
                        | expresion_dato BETWEEN expresion_dato AND expresion_dato 
                        | expresion_dato NOT BETWEEN expresion_dato AND expresion_dato
                        | expresion_dato BETWEEN SYMMETRIC expresion_dato AND expresion_dato
                        | expresion_dato NOT BETWEEN SYMMETRIC expresion_dato AND expresion_dato
                        | expresion_dato IS DISTINCT FROM expresion_dato
                        | expresion_dato IS NOT DISTINCT FROM expresion_dato 
                        | expresion_dato IS NOT DISTINCT FROM expresion_dato AND expresion_dato
                        | expresion_dato IS NULL
                        | expresion_dato IS NOT NULL
                        | expresion_dato ISNULL
                        | expresion_dato NOTNULL
                        | expresion_dato IS TRUE
                        | expresion_dato IS FALSE
                        | expresion_dato IS NOT TRUE
                        | expresion_dato IS NOT FALSE
                        | expresion_dato IS UNKNOWN
                        | expresion_dato IS NOT UNKNOWN '''

#----------terminar el distinct ------------
def p_select_lista(t):
    ' opcion_select_lista : DISTINCT campos_c'
    t[0] = Create_s_distinct(t[1],t[2])

def p_select_lista2(t):
    ' opcion_select_lista : opciones_select_lista'
            
def p_opciones_select_lista(t):
    ''' opciones_select_lista : opciones_select_lista COMA opcion_select
                              | opcion_select '''


def p_opcion_select_lista(t):
    ' opcion_select_lista : opcion_select '

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
    ' opcional_join : AS as_ID ON CONDICION_INNER_JOIN'

def p_opcional_join_on(t):
    ' opcional_join :  ON expresion_relacional'

def p_optional_join_using(t):
    ' opcional_join :  USING PAR_A campos_c PAR_C'

def p_optional_join_join(t):
    ' opcional_join : JOIN ID'


def p_CONDICION_INNER_JOIN(t):
    'CONDICION_INNER_JOIN : expresion_logica'


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
    ' lista_datos : lista_datos COMA CADENA'
    t[1].append(ExpresionComillaSimple(t[3]))
    t[0] = t[1]

def p_expresion_lista(t):
    ' lista_datos : CADENA '
    t[0] = [ExpresionComillaSimple(t[1])]

def p_expresion_dato(t):
    '''expresion : ENTERO'''
    t[0] = ExpresionEntero(t[1])


def p_expresion_dato2(t):
    '''expresion_dato : ID'''

def p_expresion(t):
    ''' expresion :    expresion SUMA expresion
                     | expresion RESTA expresion
                     | expresion ASTERISCO expresion
                     | expresion DIVISION expresion'''
    if t[2] == '+' : t[0] = ExpresionBinaria(t[1],t[3], OPERACION_ARITMETICA.MAS)
    if t[2] == '-' : t[0] = ExpresionBinaria(t[1],t[3], OPERACION_ARITMETICA.MENOS)
    if t[2] == '*' : t[0] = ExpresionBinaria(t[1],t[3], OPERACION_ARITMETICA.ASTERISCO)
    if t[2] == '/' : t[0] = ExpresionBinaria(t[1],t[3], OPERACION_ARITMETICA.DIVIDIDO)

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

def p_expresion_relacional_exp(t):
    ' expresion_relacional : expresion '

def p_expresion_logica(t):
    ''' expresion_logica : expresion_relacional AND expresion_logica
                        |  expresion_relacional OR expresion_logica'''

def p_expresion_logica_not(t):
    ''' expresion_logica : NOT expresion_logica'''

def p_expresion_logica_rel(t):
    ''' expresion_logica : expresion_relacional''' 



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