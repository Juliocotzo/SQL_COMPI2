#?######################################################
# TODO        INSTRUCCIONES
#?######################################################

    
def p_instruccion9(t) :
    'instruccion      : insert_insrt'
    reporte_bnf.append("<instruccion> ::= <insert_insrt>")
    t[0] = t[1]                     



def p_instruccion_f_select(t):
    'instruccion : select_insrt PTCOMA'
    reporte_bnf.append("<instruccion> ::= <select_insrt> PTCOMA")
    t[0] = t[1]

def p_instruccion_f_select_union(t):
    'instruccion : select_uniones PTCOMA'  
    reporte_bnf.append("<instruccion> ::= <select_uniones> PTOCOMA") 
    t[0] = Select_Uniones(t[1][0],t[1][1])





#?######################################################
# TODO        GRAMATICA INSTRUCCION INSERT
#?######################################################

def p_insert_insrt(t):
    ' insert_insrt : INSERT INTO ID PARA lista_parametros_lista PARC  VALUES PARA lista_datos PARC PTCOMA '
    reporte_bnf.append("<insert_insrt> ::= INSERT INTO ID PARA <lista_parametros_lista> PARC  VALUES PARA <lista_datos> PARC PTCOMA")
    t[0] = Definicion_Insert(t[3], TIPO_INSERT.CON_PARAMETROS ,t[5], t[9])
    

def p_opcion_lista_parametros_(t):
    ' insert_insrt : INSERT INTO ID PARA  PARC  VALUES PARA lista_datos PARC PTCOMA '
    reporte_bnf.append("<insert_insrt> ::= INSERT INTO ID PARA  PARC  VALUES PARA <lista_datos> PARC PTCOMA")
    t[0] = Definicion_Insert(t[3], TIPO_INSERT.SIN_PARAMETROS ,None, t[8])

def p_opcion_lista_parametros_vacios(t):
    ' insert_insrt : INSERT INTO ID VALUES PARA lista_datos PARC PTCOMA '
    reporte_bnf.append("<insert_insrt> ::= INSERT INTO ID VALUES PARA <lista_datos> PARC PTCOMA")
    t[0] = Definicion_Insert(t[3], TIPO_INSERT.SIN_PARAMETROS ,None, t[6])


#?######################################################
# TODO        GRAMATICA INSTRUCCION LISTA INSERT
#?######################################################

def p_lista_parametros_lista(t):
    ' lista_parametros_lista : lista_parametros_lista COMA ID'
    reporte_bnf.append("<lista_parametros_lista> ::= <lista_parametros_lista> COMA ID")
    t[1].append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]))
    t[0] = t[1]

def p_lista_parametros(t):
    ' lista_parametros_lista : ID'
    reporte_bnf.append("<lista_parametros_lista> ::= ID")
    t[0] = [ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])]


def p_parametros_lista_datos(t):
    ' lista_datos : lista_datos COMA exclusiva_insert'
    t[1].append(t[3])
    t[0] = t[1]


def p_parametros_exclusiva(t):
    ' lista_datos : exclusiva_insert'
    reporte_bnf.append("<lista_datos> ::= <exclusiva_insert>")
    t[0] = [t[1]] 


def p_expresion_lista(t):
    ' exclusiva_insert : expresion'
    reporte_bnf.append("<exclusiva_insert> ::= <expresion>") 
    t[0] = t[1]


def p_expresiones_excluva(t):
    ''' exclusiva_insert : SUBSTRING PARA string_type COMA expresion COMA expresion PARC
                        | MD5 PARA string_type PARC
                        | TRIM PARA string_type PARC
                        | SUBSTR PARA string_type COMA expresion COMA expresion PARC
                        | NOW PARA PARC'''
    if t[1].upper() == 'SUBSTRING' : t[0] = Funcion_Exclusivas_insert(INSERT_EXCLUSIVA.SUBSTRING,t[3],t[5],t[7])
    elif t[1].upper() == 'MD5' : t[0] = Funcion_Exclusivas_insert(INSERT_EXCLUSIVA.MD5,t[3],None,None)
    elif t[1].upper() == 'TRIM' : t[0] = Funcion_Exclusivas_insert(INSERT_EXCLUSIVA.TRIM,t[3],None,None)
    elif t[1].upper() == 'SUBSTR' : t[0] = Funcion_Exclusivas_insert(INSERT_EXCLUSIVA.SUBSTRING,t[3],t[5],t[7])
    elif t[1].upper() == 'NOW' : t[0] = Funcion_Exclusivas_insert(INSERT_EXCLUSIVA.NOW,None,None,None)

#?######################################################
# TODO        GRAMATICA ALTER TABLE
#?######################################################







     










#?######################################################
# TODO      INSTRUCCION SELECT
#?######################################################


def p_instruccion_select_insrt(t):
    ' select_insrt : SELECT opcion_select_tm'  
    reporte_bnf.append("<select_insrt> ::= SELECT <opcion_select_tm>")
    t[0] = t[2]


def p_instruccion_select_insrt_union(t):
    ''' select_uniones : select_uniones tipo_union select_insrt'''
    reporte_bnf.append("<select_uniones> ::= <select_uniones> <tipo_union> <select_insrt>")
    temp = []
    if t[2].upper() == 'UNION':
        temp.append(OPCIONES_UNIONES.UNION)
        t[1].append(t[3])
        temp.append(t[1])
    elif t[2].upper() == 'INTERSECT':
        temp.append(OPCIONES_UNIONES.INTERSECT)
        t[1].append(t[3])
        temp.append(t[1])
    elif t[2].upper() == 'EXCEPT':
        temp.append(OPCIONES_UNIONES.EXCEPTS)
        t[1].append(t[3])
        temp.append(t[1])
    t[0] = temp

def p_instruccion_select_insrt_union_ALL(t):
    ''' select_uniones : select_uniones tipo_union ALL select_insrt'''
    reporte_bnf.append("<select_uniones> ::= <select_uniones> <tipo_union> ALL <select_insrt>")
    temp = []
    if t[2].upper() == 'UNION':
        temp.append(OPCIONES_UNIONES.UNION_ALL)
        t[1].append(t[4])
        temp.append(t[1])
    elif t[2].upper() == 'INTERSECT':
        temp.append(OPCIONES_UNIONES.INTERSECT_ALL)
        t[1].append(t[4])
        temp.append(t[1])
    elif t[2].upper() == 'EXCEPT':
        temp.append(OPCIONES_UNIONES.EXCEPTS_ALL)
        t[1].append(t[4])
        temp.append(t[1])
    t[0] = temp

def p_instruccion_select_insrt_union2(t):
    ' select_uniones : select_insrt '
    reporte_bnf.append("<select_uniones> ::= <select_insrt>")
    t[0] = [t[1]]

def p_instruccion_select_uniones(t):
    ' tipo_union : UNION'
    reporte_bnf.append("<tipo_union> ::= UNION")
    t[0] = t[1]

def p_instruccion_select_uniones1(t):
    ' tipo_union : INTERSECT'
    reporte_bnf.append("<tipo_union> ::= INTERSECT")
    t[0] = t[1]    

def p_instruccion_select_uniones2(t):
    ' tipo_union :  EXCEPT'
    reporte_bnf.append("<tipo_union> ::= EXCEPT")
    t[0] = t[1]

def p_opcion_select_tm3(t):
    'opcion_select_tm : greatest_insrt' #YA ESTA
    reporte_bnf.append("<opcion_select_tm> ::= <greatest_insrt>")
    t[0] = t[1]

def p_select_lista(t):
    ' opcion_select_lista : DISTINCT campos_c '
    reporte_bnf.append("<opcion_select_lista> ::= DISTINCT <campos_c>")
    t[0] = Create_select_uno(OPCIONES_SELECT.DISTINCT,None,None,None,None,t[2],None) #YA ESTA

def p_select_lista2(t):
    ' opcion_select_lista : opciones_select_lista'
    reporte_bnf.append("<opcion_select_lista> ::= <opciones_select_lista>")
    t[0] = Create_select_uno(OPCIONES_SELECT.SUBCONSULTA,None,None,None,t[1],None,None)

def p_opciones_select_lista(t):
    ''' opciones_select_lista : opciones_select_lista COMA opcion_select '''
    reporte_bnf.append("<opciones_select_lista> ::= <opciones_select_lista> COMA <opcion_select>")
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_select_lista2(t):
    ' opciones_select_lista : opcion_select'
    reporte_bnf.append("<opciones_select_lista> ::= <opcion_select>")
    t[0] = [t[1]]

def p_opcion_select_tm1(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_sobrenombres '
    reporte_bnf.append("<opcion_select_tm> ::= <opcion_select_lista>  FROM <opciones_sobrenombres>")
    t[0] = Create_select_general(OPCIONES_SELECT.SELECT,t[1],None,None,None,t[3])

def p_opcion_select_tm2(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_sobrenombres opcion_from '
    reporte_bnf.append("<opcion_select_tm> ::= <opcion_select_lista>  FROM <opciones_sobrenombres> <opcion_from>")
    t[0] = Create_select_general(OPCIONES_SELECT.SELECT,t[1],t[4],None,None,t[3])

def p_opciones_sobrenombre(t):
    '''opciones_sobrenombres : opciones_sobrenombres COMA opcion_sobrenombre '''
    reporte_bnf.append("<opciones_sobrenombres> ::= <opciones_sobrenombres> COMA <opcion_sobrenombre>")
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_sobrenombre2(t):
    ' opciones_sobrenombres : opcion_sobrenombre '
    reporte_bnf.append("<opciones_sobrenombres> ::= <opcion_sobrenombre>")
    t[0] = [t[1]]

def p_opcion_select_tm_op1(t):
    'opcion_select_tm : opcion_select_lista seguir_sobrenombre FROM otros_froms '
    reporte_bnf.append("<opcion_select_tm> ::= <opcion_select_lista> <seguir_sobrenombre> FROM <otros_froms>")
    t[0] = Create_select_general(OPCIONES_SELECT,None,t[1],t[2],t[4],None)

def p_otros_from(t):
    'otros_froms : otros_froms COMA otro_from'
    reporte_bnf.append("<otros_froms> ::= <otros_froms> COMA <otro_from>")
    t[1].append(t[3])
    t[0] = t[1]

def p_otros_from2(t):
    'otros_froms : otro_from'
    reporte_bnf.append("<otros_froms> ::= <otro_from>")
    t[0] = [t[1]]

def p_opcion_select_tm(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_from opcion_from'
    reporte_bnf.append("<opcion_select_tm> ::= <opcion_select_lista>  FROM <opciones_from> <opcion_from>")
    t[0] = Create_select_general(OPCIONES_SELECT.SELECT,t[1],None,t[4],t[3],None)

def p_opciones_from(t):
    '''opciones_from : opciones_from COMA from_s'''
    reporte_bnf.append("<opciones_from> ::= <opciones_from> COMA <from_s>")
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_from2(t):
    'opciones_from : from_s'
    reporte_bnf.append("<opciones_from> ::= <from_s>")
    t[0] = [t[1]]

def p_ins_1(t):
    'opcion_select_tm : varias_funciones'
    reporte_bnf.append("<opcion_select_tm> ::= <varias_funciones>")
    t[0] = Create_select_general(OPCIONES_SELECT.SELECT,None,None,None,None,t[1])

def p_varias_funciones(t):
    'varias_funciones : varias_funciones COMA funcion'
    reporte_bnf.append("<varias_funciones> ::= <varias_funciones> COMA <funcion>")
    t[1].append(t[3])
    t[0] = t[1]

def p_varias_funciones1(t):
    'varias_funciones : funcion'
    reporte_bnf.append("<varias_funciones> ::= <funcion>")
    t[0] = [t[1]]

def p_funcion(t):
    'funcion : funciones_select seguir_sobrenombre'
    reporte_bnf.append("<funcion> ::= <funciones_select> <seguir_sobrenombre>")
    t[0] = Create_select_uno(OPCIONES_SELECT.FUNCIONES,None,t[1],t[2],None,None,None)

def p_funcion1(t):
    'funcion : funciones_select'
    reporte_bnf.append("<funcion> ::= <funciones_select>")
    t[0] = Create_select_uno(OPCIONES_SELECT.FUNCIONES,None,t[1],None,None,None,None)

def p_opcion_select_tm_op2(t):
    '''otro_from : from_s '''
    reporte_bnf.append("<otro_from> ::= <from_s>")
    t[0] = Create_select_general(OPCIONES_SELECT.SELECT,t[1],None,None,None,None)

def p_opcion_select_tm_op3(t):
    'otro_from : from_s opcion_from'
    reporte_bnf.append("<otro_from> ::= <from_s><opcion_from>")
    t[0] = Create_select_general(OPCIONES_SELECT.SELECT,t[1],t[2],None,None,None)

def p_opcion_s(t):
    ''' from_s : ID'''
    reporte_bnf.append("<from_s> ::= ID")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

def p_opcion_s2(t):
    ' from_s : PARA'
    reporte_bnf.append("<from_s> ::= PARA")
    t[0] = t[1]

def p_sobre_Nombre(t):
    ''' opcion_sobrenombre : ID seguir_sobrenombre'''
    reporte_bnf.append("<opcion_sobrenombre> ::= ID <seguir_sobrenombre>")
    if t[2][0] == TIPO_VALOR.AS_ID:
        t[0] = ExpresionIdentificadorDoble(t[2][0],t[1],t[2][1])
    elif t[2][0] == TIPO_VALOR.DOBLE:
        t[0] = ExpresionIdentificadorDoble(t[2][0],t[1],t[2][1])
    else:
        t[0] = ExpresionIdentificadorDoble(TIPO_VALOR.IDENTIFICADOR,t[1],t[2])
    
def p_sobre_Nombre2(t):
    ' opcion_sobrenombre : ID '
    reporte_bnf.append("<opcion_sobrenombre> ::= ID")
    t[0] = ExpresionIdentificadorDoble(TIPO_VALOR.IDENTIFICADOR,t[1],None)

def p_as_ID(t):
    ''' as_ID : ID '''
    reporte_bnf.append("<as_ID> ::= ID")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

def p_as_ID2(t):
    'as_ID : CADENA'
    reporte_bnf.append("<as_ID> ::= CADENA")
    t[0] = ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[1])
#---------------------------------------------------------

def p_alias(t):
    ''' seguir_sobrenombre : AS as_ID'''
    reporte_bnf.append("<seguir_sobrenombre> ::= AS <as_ID>")
    temp = []
    temp.append(TIPO_VALOR.AS_ID)
    temp.append(t[2])
    t[0] = temp

def p_alias2(t):
    'seguir_sobrenombre : ID'
    reporte_bnf.append("<seguir_sobrenombre> ::= ID")
    t[0] = t[1]

def p_alias3(t):
    'seguir_sobrenombre : PUNTO ID'
    reporte_bnf.append("<seguir_sobrenombre> ::= PUNTO ID")
    temp = []
    temp.append(TIPO_VALOR.DOBLE)
    temp.append(t[2])
    t[0] = temp

def p_opcion_select_tm_extract(t):
    'opcion_select_tm : EXTRACT PARA extract_time FROM TIMESTAMP CADENA  PARC '
    reporte_bnf.append("<opcion_select_tm> ::= EXTRACT PARA <extract_time> FROM TIMESTAMP CADENA  PARC")
    t[0] = Create_select_time(SELECT_TIME.EXTRACT,t[3],t[6])

def p_opcion_select_tm_date(t):
    'opcion_select_tm : DATE_PART PARA CADENA COMA INTERVAL CADENA PARC  '
    reporte_bnf.append("<opcion_select_tm> ::= DATE_PART PARA CADENA COMA INTERVAL CADENA PARC")
    t[0] = Create_select_time(SELECT_TIME.DATE_PART,t[3],t[6])

def p_opcion_select_tm_now(t):
    'opcion_select_tm : NOW PARA PARC '
    reporte_bnf.append("<opcion_select_tm> ::= NOW PARA PARC")
    t[0] = Create_select_time(SELECT_TIME.NOW,None,None)

def p_opcion_select_tm_current(t):
    'opcion_select_tm : CURRENT_DATE '
    reporte_bnf.append("<opcion_select_tm> ::= CURRENT_DATE")
    t[0] = Create_select_time(SELECT_TIME.CURRENT_DATE,None,None)

def p_opcion_select_tm_crtm(t):
    'opcion_select_tm : CURRENT_TIME '
    reporte_bnf.append("<opcion_select_tm> ::= CURRENT_TIME")
    t[0] = Create_select_time(SELECT_TIME.CURRENT_TIME,None,None)

def p_opcion_select_tm_timestamp(t):
    'opcion_select_tm : TIMESTAMP CADENA '
    reporte_bnf.append("<opcion_select_tm> ::= TIMESTAMP CADENA")
    t[0] = Create_select_time(SELECT_TIME.TIMESTAMP,t[2],None)



#?######################################################
# TODO      OFFSET
#?######################################################

def p_opcion_from_0_0_1_1_1_1_1_0(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::=  <cond_where> <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],t[2],t[3],t[4],t[5],t[6],t[7],None)

def p_opcion_from_0_0_0_1_1_1_1_0(t):
    'opcion_from :  cond_gb cond_having cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,t[1],t[2],t[3],t[4],t[5],t[6],None)
    
def p_opcion_from_0_0_1_0_1_1_1_0(t):
    'opcion_from : cond_where cond_having cond_ob orden cond_limit OFFSET ENTERO'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <orden> <cond_limit> OFFSET ENTERO")
    t[0] = Create_padre_select(t[1],None,t[2],t[3],t[4],t[5],None,t[7])

def p_opcion_from_0_0_0_0_1_1_1_0(t):
    'opcion_from :  cond_having cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::=  <cond_having> <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,None,t[1],t[2],t[3],t[4],t[5],None)

def p_opcion_from_0_0_1_1_0_1_1_0(t):
    'opcion_from : cond_where cond_gb cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::=  <cond_where> <cond_gb> <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],t[2],None,t[3],t[4],t[5],t[6],None)

def p_opcion_from_0_0_0_1_0_1_1_0(t):
    'opcion_from :  cond_gb cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,t[1],None,t[2],t[3],t[4],t[5],None)

def p_opcion_from_0_0_1_0_0_1_1_0(t):
    'opcion_from : cond_where cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],None,None,t[2],t[3],t[4],t[5],None)

def p_opcion_from_0_0_0_0_0_1_1_0(t):
    'opcion_from :  cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,None,None,t[1],t[2],t[3],t[4],None)

def p_opcion_from_0_0_1_1_1_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],t[2],t[3],t[4],None,t[5],t[6],None)

def p_opcion_from_0_0_0_1_1_1_1_0_ordeno(t):
    'opcion_from : cond_gb cond_having cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,t[1],t[2],t[3],None,t[4],t[5],None)

def p_opcion_from_0_0_1_0_1_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_having cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],None,t[2],t[3],None,t[4],t[5],None)

def p_opcion_from_0_0_0_0_1_1_1_0_ordeno(t):
    'opcion_from :  cond_having cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,None,t[1],t[2],None,t[3],t[4],None)

def p_opcion_from_0_0_1_1_0_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_gb  cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],t[2],None,t[3],None,t[4],t[5],None)

def p_opcion_from_0_0_0_1_0_1_1_0_ordeno(t):
    'opcion_from :  cond_gb cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,t[1],None,t[2],None,t[3],t[4],None)

def p_opcion_from_0_0_1_0_0_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],None,None,t[2],None,t[3],t[4],None)

def p_opcion_from_0_0_0_0_0_1_1_0_ordeno(t):
    'opcion_from :  cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,None,None,t[1],None,t[2],t[3],None)

def p_opcion_from_0_0_1_1_1_0_1_0(t):
    'opcion_from : cond_where cond_gb cond_having cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],t[2],t[3],None,None,t[4],t[5],None)

def p_opcion_from_0_0_0_1_1_0_1_0(t):
    'opcion_from :  cond_gb cond_having cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,t[1],t[2],None,None,t[3],t[4],None)

def p_opcion_from_0_0_1_0_1_0_1_0(t):
    'opcion_from : cond_where cond_having cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],None,t[2],None,None,t[3],t[4],None)

def p_opcion_from_0_0_0_0_1_0_1_0(t):
    'opcion_from :  cond_having cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,None,t[1],None,None,t[2],t[3],None)

def p_opcion_from_0_0_1_1_0_0_1_0(t):
    'opcion_from : cond_where cond_gb cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],t[2],None,None,None,t[3],t[4],None)

def p_opcion_from_0_0_0_1_0_0_1_0(t):
    'opcion_from :  cond_gb cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,t[1],None,None,None,t[2],t[3],None)

def p_opcion_from_0_0_1_0_0_0_1_0(t):
    'opcion_from : cond_where cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],None,None,None,None,t[2],t[3],None)

def p_opcion_from_0_0_0_0_0_0_1_0(t):
    'opcion_from :  cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,None,None,None,None,t[1],t[2],None)

def p_opcion_from_0_0_1_1_1_1_1_0_offno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(t[1],t[2],t[3],t[4],t[5],t[6],None,None)

def p_opcion_from_0_0_0_1_1_1_1_0_offno(t):
    'opcion_from :  cond_gb cond_having cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(None,t[1],t[2],t[3],t[4],t[5],None,None)

def p_opcion_from_0_0_1_0_1_1_1_0_offno(t):
    'opcion_from : cond_where cond_having cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(t[1],None,t[2],t[3],t[4],t[5],None,None)

def p_opcion_from_0_0_0_0_1_1_1_0_offno(t):
    'opcion_from :  cond_having cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(None,None,t[1],t[2],t[3],t[4],None,None)

def p_opcion_from_0_0_1_1_0_1_1_0_offno(t):
    'opcion_from : cond_where cond_gb cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(t[1],t[2],None,t[3],t[4],t[5],None,None)

def p_opcion_from_0_0_0_1_0_1_1_0_offno(t):
    'opcion_from :  cond_gb cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(None,t[1],None,t[2],t[3],t[4],None,None)

def p_opcion_from_0_0_1_0_0_1_1_0_offno(t):
    'opcion_from : cond_where cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(t[1],None,None,t[2],t[3],t[4],None,None)

def p_opcion_from_0_0_0_0_0_1_1_0_offno(t):
    'opcion_from :  cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(None,None,None,t[1],t[2],t[3],None,None)

def p_opcion_from_0_0_1_1_1_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(t[1],t[2],t[3],t[4],None,t[5],None,None)

def p_opcion_from_0_0_0_1_1_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_gb cond_having cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(None,t[1],t[2],t[3],None,t[4],None,None)

def p_opcion_from_0_0_1_0_1_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_having cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(t[1],None,t[2],t[3],None,t[4],None,None)

def p_opcion_from_0_0_0_0_1_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_having cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(None,None,t[1],t[2],None,t[3],None,None)

def p_opcion_from_0_0_1_1_0_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_gb cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(t[1],t[2],None,t[3],None,t[4],None,None)

def p_opcion_from_0_0_0_1_0_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_gb cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(None,t[1],None,t[2],None,t[3],None,None)

def p_opcion_from_0_0_1_0_0_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(t[1],None,None,t[2],None,t[3],None,None)

def p_opcion_from_0_0_0_0_0_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(None,None,None,t[1],None,t[2],None,None)

def p_opcion_from_0_0_1_1_1_0_1_0_offno(t):
    'opcion_from :  cond_where cond_gb cond_having cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_limit>")
    t[0] = Create_padre_select(t[1],t[2],t[3],None,None,t[4],None,None)

def p_opcion_from_0_0_0_1_1_0_1_0_offno(t):
    'opcion_from :  cond_gb cond_having cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_limit>")
    t[0] = Create_padre_select(None,t[1],t[2],None,None,t[3],None,None)

def p_opcion_from_0_0_1_0_1_0_1_0_offno(t):
    'opcion_from :  cond_where cond_having cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_limit>")
    t[0] = Create_padre_select(t[1],None,t[2],None,None,t[3],None,None)

def p_opcion_from_0_0_0_0_1_0_1_0_offno(t):
    'opcion_from :  cond_having cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_limit>")
    t[0] = Create_padre_select(None,None,t[1],None,None,t[2],None,None)

def p_opcion_from_0_0_1_1_0_0_1_0_offno(t):
    'opcion_from :  cond_where cond_gb cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_limit>")
    t[0] = Create_padre_select(t[1],t[2],None,None,None,t[3],None,None)

def p_opcion_from_0_0_0_1_0_0_1_0_offno(t):
    'opcion_from :  cond_gb  cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_limit>")
    t[0] = Create_padre_select(None,t[1],None,None,None,t[2],None,None)

def p_opcion_from_0_0_1_0_0_0_1_0_offno(t):
    'opcion_from :  cond_where cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_limit>")
    t[0] = Create_padre_select(t[1],None,None,None,None,t[2],None,None)

def p_opcion_from_0_0_0_0_0_0_1_0_offno(t):
    'opcion_from :  cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_limit>")
    t[0] = Create_padre_select(None,None,None,None,None,t[1],None,None)

def p_opcion_from_0_0_1_1_1_1_0_0(t):
    'opcion_from :  cond_where cond_gb cond_having cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob> <orden>")
    t[0] = Create_padre_select(t[1],t[2],t[3],t[4],t[5],None,None,None)

def p_opcion_from_0_0_0_1_1_1_0_0(t):
    'opcion_from :  cond_gb cond_having cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <orden>")
    t[0] = Create_padre_select(None,t[1],t[2],t[3],t[4],None,None,None)

def p_opcion_from_0_0_1_0_1_1_0_0(t):
    'opcion_from :  cond_where cond_having cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <orden>")
    t[0] = Create_padre_select(t[1],None,t[2],t[3],t[4],None,None,None)

def p_opcion_from_0_0_0_0_1_1_0_0(t):
    'opcion_from :  cond_having cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob> <orden>")
    t[0] = Create_padre_select(None,None,t[1],t[2],t[3],None,None,None)

def p_opcion_from_0_0_1_1_0_1_0_0(t):
    'opcion_from :  cond_where cond_gb cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob> <orden>")
    t[0] = Create_padre_select(t[1],t[2],None,t[3],t[4],None,None,None)

def p_opcion_from_0_0_0_1_0_1_0_0(t):
    'opcion_from :  cond_gb  cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <orden>")
    t[0] = Create_padre_select(None,t[1],None,t[2],t[3],None,None,None)

def p_opcion_from_0_0_1_0_0_1_0_0(t):
    'opcion_from :  cond_where cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <orden>")
    t[0] = Create_padre_select(t[1],None,None,t[2],t[3],None,None,None)

def p_opcion_from_0_0_0_0_0_1_0_0(t):
    'opcion_from :  cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_ob>")
    t[0] = Create_padre_select(None,None,None,t[1],None,None,None,None)

def p_opcion_from_0_0_1_1_1_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_gb cond_having cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob>")
    t[0] = Create_padre_select(t[1],t[2],t[3],t[4],None,None,None,None)

def p_opcion_from_0_0_0_1_1_1_0_0_ordeno(t):
    'opcion_from :  cond_gb cond_having cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob>")
    t[0] = Create_padre_select(None,t[1],t[2],t[3],None,None,None,None)

def p_opcion_from_0_0_1_0_1_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_having cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob>")
    t[0] = Create_padre_select(t[1],None,t[2],t[3],None,None,None,None)

def p_opcion_from_0_0_0_0_1_1_0_0_ordeno(t):
    'opcion_from :  cond_having cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob>")
    t[0] = Create_padre_select(None,None,t[1],t[2],None,None,None,None)

def p_opcion_from_0_0_1_1_0_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_gb cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob>")
    t[0] = Create_padre_select(t[1],t[2],None,t[4],None,None,None,None)

def p_opcion_from_0_0_0_1_0_1_0_0_ordeno(t):
    'opcion_from :  cond_gb cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob>")
    t[0] = Create_padre_select(None,t[1],None,t[2],None,None,None,None)

def p_opcion_from_0_0_1_0_0_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob>")
    t[0] = Create_padre_select(t[1],None,None,t[2],None,None,None,None)

#def p_opcion_from_0_0_0_0_0_1_0_0_ordeno(t):
 #   'opcion_from :  cond_ob'

def p_opcion_from_0_0_1_1_1_0_0_0(t):
    'opcion_from : cond_where cond_gb cond_having'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having>")
    t[0] = Create_padre_select(t[1],t[2],t[3],None,None,None,None,None)

def p_opcion_from_0_0_0_1_1_0_0_0(t):
    'opcion_from :  cond_gb cond_having'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having>")
    t[0] = Create_padre_select(None,t[1],t[2],None,None,None,None,None)

def p_opcion_from_0_0_1_0_1_0_0_0(t):
    'opcion_from : cond_where cond_having'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having>")
    t[0] = Create_padre_select(t[1],None,t[2],None,None,None,None,None)

def p_opcion_from_0_0_0_0_1_0_0_0(t):
    'opcion_from :  cond_having'
    reporte_bnf.append("<opcion_from> ::= <cond_having>")
    t[0] = Create_padre_select(None,None,t[1],None,None,None,None,None)

def p_opcion_from_0_0_1_1_0_0_0_0(t):
    'opcion_from : cond_where cond_gb '
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb>")
    t[0] = Create_padre_select(t[1],t[2],None,None,None,None,None,None)

def p_opcion_from_0_0_0_1_0_0_0_0(t):
    'opcion_from :  cond_gb '
    reporte_bnf.append("<opcion_from> ::= <cond_gb>")
    t[0] = Create_padre_select(None,t[1],None,None,None,None,None,None)

def p_opcion_from_0_0_1_0_0_0_0_0(t):
    'opcion_from : cond_where'
    reporte_bnf.append("<opcion_from> ::= <cond_where>")
    t[0] = Create_padre_select(t[1],None,None,None,None,None,None,None)


    
#? ####################################################################
# TODO              OPCIONES DE FROM 
#? ####################################################################

def p_opcion_from_2(t):
    'opcion_from :   select_insrt PARC ID '
    reporte_bnf.append("<opcion_from> ::= <select_insrt> PARC ID")
    t[0] = Create_hijo_select(OPCIONES_SELECT.SUBCONSULTA,t[1],t[3])

def p_opcion_from_3(t):
    'opcion_from :   select_insrt PARC'
    reporte_bnf.append("<opcion_from> ::= <select_insrt> PARC")
    t[0] = Create_hijo_select(OPCIONES_SELECT.SUBCONSULTA,t[1],None)

def p_cond_where(t):
    'cond_where : WHERE expresion_where'
    reporte_bnf.append("<cond_where> ::= WHERE <expresion_where>")
    t[0] = Create_hijo_select(OPCIONES_SELECT.WHERE,t[2],None)

def p_cond_GB(t):
    'cond_gb : GROUP BY campos_c '
    reporte_bnf.append("<cond_gb> ::= GROUP BY <campos_c>")
    t[0] = Create_hijo_select(OPCIONES_SELECT.GROUP_BY,t[3],None)

def p_cond_Having(t):
    'cond_having : HAVING expresion_logica'
    reporte_bnf.append("<cond_having> ::= HAVING <expresion_logica>")
    t[0] = Create_hijo_select(OPCIONES_SELECT.HAVING,t[1],None)

def p_cond_OB(t):
    'cond_ob : ORDER BY campos_c'  #######
    reporte_bnf.append("<cond_ob> ::= ORDER BY <campos_c>")
    t[0] = Create_hijo_select(OPCIONES_SELECT.ORDER_BY,t[3],None)

def p_cond_limit(t):
    'cond_limit : LIMIT opc_lim'
    reporte_bnf.append("<cond_limit> ::= LIMIT <opc_lim>")
    t[0] = Create_hijo_select(OPCIONES_SELECT.LIMIT,t[2],None)

def p_cond_offset(t):
    'cond_offset : OFFSET ENTERO'
    reporte_bnf.append("<cond_offset> ::= OFFSET ENTERO")
    t[0] = Create_hijo_select(OPCIONES_SELECT.OFFSET,ExpresionEntero(TIPO_VALOR.NUMERO,t[2]),None)

#? ####################################################################
# TODO              LIM,ORDEN
#? ####################################################################

def p_opc_lim(t):
    '''opc_lim : ENTERO'''
    reporte_bnf.append("<opc_lim> ::= ENTERO")
    t[0] = ExpresionEntero(TIPO_VALOR.NUMERO,t[1])

def p_opc_lim2(t):
    ' opc_lim : POR '
    reporte_bnf.append("<opc_lim> ::= POR")
    t[0] = ExpresionIdentificador(TIPO_VALOR.POR,t[1])

def p_ORDER(t):
    ''' orden : DESC '''
    reporte_bnf.append("<orden> ::= DESC")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

def p_ORDER2(t):
    ''' orden : ASC '''
    reporte_bnf.append("<orden> ::= ASC")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])






 
#? ####################################################################
# TODO          EXPRESION DATOS - FALTA
#? ####################################################################


def p_sin_some_any(t):
    '''sin_some_any : SOME '''
    reporte_bnf.append("<sin_some_any> ::= SOM")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])      

def p_sin_some_any2(t):
    '''sin_some_any : ANY  '''
    reporte_bnf.append("<sin_some_any> ::= ANY")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])   









#? ####################################################################
# TODO              EXPRESION SELECT
#? ####################################################################


def p_opcion_select1(t):
    ' opcion_select :  PARA select_insrt PARC '
    reporte_bnf.append("<opcion_select> ::= PARA <select_insrt> PARC")
    t[0] = t[2]

def p_opcion_select2(t):
    ' opcion_select :   expresion '
    reporte_bnf.append("<opcion_select> ::= <expresion>")
    t[0] = t[1]

def p_opcion_select3(t):
    'opcion_select :  funciones_select '
    reporte_bnf.append("<opcion_select> ::= <funciones_select>")
    t[0] = t[1]

def p_opcion_select4(t):
    'opcion_select :  POR '
    reporte_bnf.append("<opcion_select> ::= POR")
    t[0] = ExpresionIdentificador(TIPO_VALOR.POR,t[1])

def p_opcion_select5(t):
    ' opcion_select : ID PUNTO POR '
    reporte_bnf.append("<opcion_select> ::= ID PUNTO POR")
    t[0] = ExpresionIdentificadorDoble(TIPO_VALOR.ID_ASTERISCO,t[1],t[3])

def p_greatest_insrt(t):
    ''' greatest_insrt : GREATEST PARA greatest_val PARC
                        | LEAST PARA greatest_val PARC'''
    if t[1].upper() == 'GREATEST':
        reporte_bnf.append("<greates_insrt> ::=  GREATEST PARA <greatest_val> PARC")
        t[0] = Create_select_uno(OPCIONES_SELECT.GREATEST,None,None,None,t[3],None,None)
    elif t[1].upper() == 'LEAST':
        reporte_bnf.append("<greates_insrt> ::= LEAST PARA <greatest_val> PARC")
        t[0] = Create_select_uno(OPCIONES_SELECT.LEAST,None,None,None,t[3],None,None)

def p_greatest_insrt1(t):
    ' greatest_val : greatest_val COMA expresion_dato '
    reporte_bnf.append("<greates_val> ::= <greatest_val> COMA <expresion_dato>")
    t[1].append(t[3])
    t[0] = t[1]

def p_greatest_insrt2(t):
    ' greatest_val : expresion_dato'
    reporte_bnf.append("<greatest_val> ::= <expresion_dato>")
    t[0] = [t[1]]

##################################EXPRESIONES#####################################
def p_funciones_select(t):
    ''' funciones_select : ABS PARA expresion PARC
                        | CBRT PARA expresion PARC
                        | CEIL PARA expresion PARC 
                        | CEILING PARA expresion PARC 
                        | DEGREES PARA expresion PARC 
                        | DIV PARA expresion COMA expresion PARC 
                        | EXP PARA expresion PARC 
                        | FACTORIAL PARA expresion PARC 
                        | FLOOR PARA expresion PARC 
                        | GCD PARA expresion COMA expresion PARC
                        | LN PARA expresion PARC 
                        | LOG PARA expresion PARC 
                        | MOD PARA expresion COMA expresion PARC 
                        | PI PARA PARC 
                        | POWER PARA expresion COMA expresion PARC 
                        | RADIANS PARA expresion PARC 
                        | ROUND PARA expresion PARC 
                        | SIGN PARA expresion PARC 
                        | SQRT PARA expresion PARC
                        | WIDTH_BUCKET PARA expresion COMA expresion COMA expresion COMA expresion PARC 
                        | TRUNC PARA expresion COMA ENTERO PARC
                        | TRUNC PARA expresion PARC 
                        | RANDOM PARA PARC 
                        | ACOS PARA expresion PARC
                        | ASIND PARA expresion PARC
                        | ATAN2 PARA expresion COMA expresion PARC
                        | ATAN2D PARA expresion COMA expresion PARC
                        | ATAN PARA expresion PARC
                        | ATAND PARA expresion PARC
                        | COS PARA expresion PARC
                        | COT PARA expresion PARC 
                        | COTD PARA expresion PARC 
                        | SIN PARA expresion PARC 
                        | SIND PARA expresion PARC 
                        | TAN PARA expresion PARC 
                        | TAND PARA expresion PARC 
                        | SINH PARA expresion PARC 
                        | COSH PARA expresion PARC
                        | TANH PARA expresion PARC 
                        | ASINH PARA expresion PARC
                        | ATANH PARA expresion PARC
                        | COSD PARA expresion PARC
                        | ACOSH PARA expresion PARC  
                        | ASIN PARA expresion PARC
                        | ACOSD PARA expresion PARC
                        | LENGTH PARA string_type PARC
                        | SUBSTRING PARA string_type COMA expresion COMA expresion PARC
                        | TRIM PARA string_type PARC
                        | SUBSTR PARA string_type COMA expresion COMA expresion PARC
                        | GET_BYTE PARA string_type D_DOSPTS BYTEA COMA ENTERO PARC
                        | SET_BYTE PARA string_type D_DOSPTS BYTEA COMA ENTERO COMA ENTERO PARC
                        | SHA256 PARA string_type PARC
                        | ENCODE PARA string_type D_DOSPTS BYTEA COMA formato_texto PARC
                        | DECODE PARA string_type D_DOSPTS BYTEA COMA formato_texto PARC
                        | CONVERT PARA string_type AS TIPO_DATO PARC 
                        '''
    
    if t[1].upper() == 'ABS':
        reporte_bnf.append("<funciones_select> ::= ABS PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ABS, t[3],None,None,None)
    elif t[1].upper() == 'CBRT':
        reporte_bnf.append("<funciones_select> ::= CBRT PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CBRT, t[3],None,None,None)
    elif t[1].upper() == 'CEIL':
        reporte_bnf.append("<funciones_select> ::= CEIL PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CEIL, t[3],None,None,None)
    elif t[1].upper() == 'CEILING':
        reporte_bnf.append("<funciones_select> ::= CEILING PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CEILING, t[3],None,None,None)
    elif t[1].upper() == 'DEGREES':
        reporte_bnf.append("<funciones_select> ::= DEGREES PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.DEGREES, t[3],None,None,None)
    elif t[1].upper() == 'DIV':
        reporte_bnf.append("<funciones_select> ::= DIV PARA <expresion> COMA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.E_DIV, t[3],t[5],None,None)
    elif t[1].upper() == 'EXP':
        reporte_bnf.append("<funciones_select> ::= EXP PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.EXP, t[3],None,None,None)
    elif t[1].upper() == 'FACTORIAL':
        reporte_bnf.append("<funciones_select> ::= FACTORIAL PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.FACTORIAL, t[3],None,None,None)
    elif t[1].upper() == 'FLOOR':
        reporte_bnf.append("<funciones_select> ::= FLOOR PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.FLOOR, t[3],None,None,None)
    elif t[1].upper() == 'GCD':
        reporte_bnf.append("<funciones_select> ::= GCD PARA <expresion> COMA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.GCD, t[3],t[5],None,None)
    elif t[1].upper() == 'LN':
        reporte_bnf.append("<funciones_select> ::= LN PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.LN, t[3],None,None,None)
    elif t[1].upper() == 'LOG':
        reporte_bnf.append("<funciones_select> ::= LOG PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.LOG, t[3],None,None,None)
    elif t[1].upper() == 'MOD':
        reporte_bnf.append("<funciones_select> ::= MOD PARA <expresion> COMA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.MOD, t[3],t[5],None,None)
    elif t[1].upper() == 'PI':
        reporte_bnf.append("<funciones_select> ::= PI PARA PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.PI, None,None,None,None)
    elif t[1].upper() == 'POWER':
        reporte_bnf.append("<funciones_select> ::= POWER PARA <expresion> COMA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.POWER, t[3],t[5],None,None)
    elif t[1].upper() == 'RADIANS':
        reporte_bnf.append("<funciones_select> ::= RADIANS PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.RADIANS, t[3],None,None,None)
    elif t[1].upper() == 'ROUND':
        reporte_bnf.append("<funciones_select> ::= ROUND PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ROUND, t[3],None,None,None)
    elif t[1].upper() == 'SIGN':
        reporte_bnf.append("<funciones_select> ::= SIGN PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.SIGN, t[3],None,None,None)
    elif t[1].upper() == 'SQRT':
        reporte_bnf.append("<funciones_select> ::= SQRT PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.SQRT, t[3],None,None,None)
    elif t[1].upper() == 'WIDTH_BUCKET':
        reporte_bnf.append("<funciones_select> ::= WIDTH_BUCKET PARA <expresion> COMA <expresion> COMA <expresion> COMA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.WIDTH_BUCKET, t[3],t[5],t[7],t[9])
    elif t[1].upper() == 'TRUNC' and t[4] == ',':
        reporte_bnf.append("<funciones_select> ::= TRUNC PARA <expresion> COMA ENTERO PARC ")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.TRUNC, t[3],ExpresionEntero(TIPO_VALOR.NUMERO,t[5]),None,None)
    elif t[1].upper() == 'TRUNC':
        reporte_bnf.append("<funciones_select> ::= TRUNC PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.S_TRUNC, t[3],None,None,None) 
    elif t[1].upper() == 'RANDOM':
        reporte_bnf.append("<funciones_select> ::= RANDOM PARA PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.RANDOM, t[3],None,None,None)
    elif t[1].upper() == 'ACOS':
        reporte_bnf.append("<funciones_select> ::= ACOS PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ACOS, t[3],None,None,None)
    elif t[1].upper() == 'ASIND':
        reporte_bnf.append("<funciones_select> ::= ASIND PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ASIND, t[3],None,None,None)
    elif t[1].upper() == 'ATAN2':
        reporte_bnf.append("<funciones_select> ::= ATAN2 PARA <expresion> COMA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ATAN2, t[3],t[5],None,None)
    elif t[1].upper() == 'ATAN2D':
        reporte_bnf.append("<funciones_select> ::= ATAN2D PARA <expresion> COMA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ATAN2D, t[3],t[5],None,None)
    elif t[1].upper() == 'ATAN':
        reporte_bnf.append("<funciones_select> ::= ATAN PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ATAN, t[3],None,None,None)
    elif t[1].upper() == 'ATAND':
        reporte_bnf.append("<funciones_select> ::= ATAND PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ATAND, t[3],None,None,None)
    elif t[1].upper() == 'COS':
        reporte_bnf.append("<funciones_select> ::= COS PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.COS, t[3],None,None,None)
    elif t[1].upper() == 'COT':
        reporte_bnf.append("<funciones_select> ::= COT PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.COT, t[3],None,None,None)
    elif t[1].upper() == 'COTD':
        reporte_bnf.append("<funciones_select> ::= COTD PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.COTD, t[3],None,None,None)
    elif t[1].upper() == 'SIN':
        reporte_bnf.append("<funciones_select> ::= SIN PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.SIN, t[3],None,None,None)
    elif t[1].upper() == 'SIND':
        reporte_bnf.append("<funciones_select> ::= SIND PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.SIND, t[3],None,None,None)
    elif t[1].upper() == 'TAN':
        reporte_bnf.append("<funciones_select> ::= TAN PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.TAN, t[3],None,None,None)
    elif t[1].upper() == 'TAND':
        reporte_bnf.append("<funciones_select> ::= TAND PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.TAND, t[3],None,None,None)
    elif t[1].upper() == 'SINH':
        reporte_bnf.append("<funciones_select> ::= SINH PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.SINH, t[3],None,None,None)
    elif t[1].upper() == 'COSH':
        reporte_bnf.append("<funciones_select> ::= COSH PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.COSH, t[3],None,None,None)
    elif t[1].upper() == 'TANH':
        reporte_bnf.append("<funciones_select> ::= TANH PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.TANH, t[3],None,None,None)
    elif t[1].upper() == 'ASINH':
        reporte_bnf.append("<funciones_select> ::= ASINH PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ASINH, t[3],None,None,None)
    elif t[1].upper() == 'ATANH':
        reporte_bnf.append("<funciones_select> ::= ATANH PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ATANH, t[3],None,None,None)
    elif t[1].upper() == 'COSD':
        reporte_bnf.append("<funciones_select> ::= COSD PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.COSD, t[3],None,None,None)
    elif t[1].upper() == 'ACOSH':
        reporte_bnf.append("<funciones_select> ::= ACOSH PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ACOSH, t[3],None,None,None)
    elif t[1].upper() == 'ASIN':
        reporte_bnf.append("<funciones_select> ::= ASIN PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ASIN, t[3],None,None,None)
    elif t[1].upper() == 'ACOSD':
        reporte_bnf.append("<funciones_select> ::= ACOSD PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ACOSD, t[3],None,None,None)
    elif t[1].upper() == 'LENGTH':
        reporte_bnf.append("<funciones_select> ::= LENGTH PARA <expresion> PARC")
        t[0] = Expresiondatos(CADENA_BINARIA.LENGTH, t[3],None,None,None)
    elif t[1].upper() == 'SUBSTRING':
        reporte_bnf.append("<funciones_select> ::= SUBSTRING PARA <string_type> COMA <expresion> COMA <expresion> PARC")
        t[0] = Expresiondatos(CADENA_BINARIA.SUBSTRING, t[3],t[5],t[7],None)
    elif t[1].upper() == 'TRIM':
        reporte_bnf.append("<funciones_select> :: TRIM PARA <string_type> PARC")
        t[0] = Expresiondatos(CADENA_BINARIA.TRIM, t[3],None,None,None) 
    elif t[1].upper() == 'SUBSTR':
        reporte_bnf.append("<funciones_select> :: SUBSTR PARA <string_type> COMA ENTERO COMA ENTERO PARC")
        t[0] = Expresiondatos(CADENA_BINARIA.SUBSTR, t[3],t[5],t[7],None) 
    elif t[1].upper() == 'GET_BYTE':
        reporte_bnf.append("<funciones_select> :: GET_BYTE PARA <string_type> D_DOSPTS BYTEA COMA ENTERO PARC")
        t[0] = Expresiondatos(CADENA_BINARIA.GET_BYTE, t[3],ExpresionEntero(TIPO_VALOR.NUMERO,t[7]),None,None)
    elif t[1].upper() == 'SET_BYTE':
        reporte_bnf.append("<funciones_select> :: SET_BYTE PARA <string_type> D_DOSPTS BYTEA COMA ENTERO COMA ENTERO PARC")
        t[0] = Expresiondatos(CADENA_BINARIA.SET_BYTE, t[3],ExpresionEntero(TIPO_VALOR.NUMERO,t[7]),ExpresionEntero(TIPO_VALOR,t[9]),None)
    elif t[1].upper() == 'SHA256':
        reporte_bnf.append("<funciones_select> :: SHA256 PARA <string_typ>e PARC")
        t[0] = Expresiondatos(CADENA_BINARIA.SHA256, t[3],None,None,None)
    elif t[1].upper() == 'ENCODE':
        reporte_bnf.append("<funciones_select> :: ENCODE PARA <string_type> D_DOSPTS BYTEA COMA formato_texto PARC")
        t[0] = Expresiondatos(CADENA_BINARIA.ENCODE, t[3],t[7],None,None)
    elif t[1].upper() == 'DECODE':
        reporte_bnf.append("<funciones_select> :: DECODE PARA <string_type> D_DOSPTS BYTEA COMA formato_texto PARC")
        t[0] = Expresiondatos(CADENA_BINARIA.DECODE, t[3],t[7],None,None)
    elif t[1].upper() == 'CONVERT':
        reporte_bnf.append("<funciones_select> :: CONVERT PARA <string_type> AS TIPO_DATO PARC ")
        t[0] = Expresiondatos(CADENA_BINARIA.CONVERT, t[3],t[5],None,None)

def p_formato_texto(t):
    ''' formato_texto : ESCAPE '''
    reporte_bnf.append("<formato_texto> ::= ESCAPE")
    t[0] = t[1]

def p_formato_texto_hex(t):
    'formato_texto : HEX'
    reporte_bnf.append("<formato_texto> ::= HEX")
    t[0] = t[1]

def p_formato_texto_base64(t):
    ' formato_texto : BASE64'
    reporte_bnf.append("<formato_texto> ::= BASE64")
    t[0] = t[1]
                 
                 

#? ###################################################################
# TODO              EXPRESION WHERE
#? ###################################################################
                 
def p_expresion_where2(t):
    'expresion_where : expresion_logica_w'
    reporte_bnf.append("<expresion_where> ::= <expresion_logica_w>")
    t[0] = t[1]

def p_expresion_where(t):
    ''' expresion_where : expresion_dato NOT IN PARA select_insrt PARC
                        | expresion_dato IN PARA select_insrt PARC
                        | NOT EXISTS PARA select_insrt PARC
                        '''

    if t[2].upper() == 'NOT' and t[3].upper() == 'IN':
        reporte_bnf.append("<expresion_where> ::= <expresion_dato> NOT IN PARA <select_insrt> PARC")
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_IN, t[1],t[5],None,None)
    elif t[2].upper() == 'IN':
        reporte_bnf.append("<expresion_where> ::= <expresion_dato> IN PARA <select_insrt> PARC")
        t[0] = Expresiondatos(OPCION_VERIFICAR.INN,t[1],t[4],None,None)
    elif t[1].upper() == 'NOT' and t[2].upper() == 'EXISTS':
        reporte_bnf.append("<expresion_where> ::= NOT EXISTS PARA <select_insrt> PARC")
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_EXISTS,t[4],None,None,None)


def p_expresion_where_3(t):
    ''' expresion_where : expresion_dato NOT BETWEEN SYMMETRIC expresion_dato AND expresion_dato'''
    if t[2].upper() == 'NOT' and t[4].upper() == 'SYMMETRIC':
        reporte_bnf.append("<expresion_where> ::= <expresion_dato> NOT BETWEEN SYMMETRIC <expresion_dato> AND <expresion_dato>")
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_BETWEEN_SYMETRIC,t[1],t[5],t[7],None)


def p_expresion_wherea(t):
    '''expresion_wherea :  ABS PARA expresion PARC
                        | LENGTH PARA string_type PARC
                        | CBRT PARA expresion PARC
                        | CEIL PARA expresion PARC 
                        | CEILING PARA expresion PARC 
                        | SUBSTRING PARA string_type COMA expresion COMA expresion PARC
                        | TRIM PARA string_type D_DOSPTS BYTEA FROM string_type D_DOSPTS BYTEA PARC
                        | SUBSTR PARA string_type COMA expresion COMA expresion PARC
                        | sin_some_any PARA select_insrt PARC
                        | EXTRACT PARA extract_time FROM string_type PARC '''

    if t[1].upper() == 'ABS':
        reporte_bnf.append("<expresion_wherea> ::= ABS PARA expresion PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ABS, t[3],None,None,None)
    elif t[1].upper() == 'LENGTH':
        reporte_bnf.append("<expresion_wherea> ::= LENGTH PARA <string_type> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.LENGTH, t[3],None,None,None)
    elif t[1].upper() == 'CBRT':
        reporte_bnf.append("<expresion_wherea> ::= CBRT PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CBRT, t[3],None,None,None)
    elif t[1].upper() == 'CEIL':
        reporte_bnf.append("<expresion_wherea> ::= CEIL PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CEIL, t[3],None,None,None)
    elif t[1].upper() == 'CEILING':
        reporte_bnf.append("<expresion_wherea> ::= CEILING PARA <expresion> PARC")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CEILING, t[3],None,None,None)
    elif t[1].upper() == 'SUBSTRING':
        reporte_bnf.append("<expresion_wherea> ::= SUBSTRING PARA <string_type> COMA <expresion> COMA <expresion> PARC")
        t[0] = Expresiondatos(OPCIONES_DATOS.SUBSTRING, t[3],t[5],t[7],None)
    elif t[1].upper() == 'TRIM':
        reporte_bnf.append("<expresion_wherea> ::= TRIM PARA <string_type> D_DOSPTS BYTEA FROM <string_type> D_DOSPTS BYTEA PARC")
        t[0] = Expresiondatos(OPCIONES_DATOS.TRIM, t[3],t[7],None,None)
    elif t[1].upper() == 'SUBSTR':
        reporte_bnf.append("<expresion_wherea> ::= SUBSTR PARA <string_type> COMA ENTERO COMA ENTERO PARC")
        t[0] = Expresiondatos(OPCIONES_DATOS.SUBSTR, t[3],t[5],t[7],None)
    elif t[1].upper() == 'EXTRACT':
        reporte_bnf.append("<expresion_wherea> ::= EXTRACT PARA <expresion_time> FROM <string_type> PARC")
        t[0] = Expresiondatos(OPCIONES_DATOS.EXTRACT, t[3],t[5],None,None)
    else:
        reporte_bnf.append("<expresion_wherea> ::= <sin_some_any> PARA <select_insrt> PARC")
        t[0] = Expresiondatos(OPCIONES_DATOS.SOME, t[3],None,None,None)

def p_expresion_wherea2(t):
    ''' expresion_wherea : expresion '''
    reporte_bnf.append("<expresion_wherea> ::= <expresion>")
    t[0] = t[1]

#? #########################################################
#ANCHOR       EXPRESIONES AGREGADAS AL WHERE
#? ##################################################
def p_expresion_wherea3(t):
    ''' expresion_wherea : LOWER PARA string_type PARC '''

def p_expresion_wherea4(t):
    ''' expresion_wherea : ID PARA ID PARC'''



def p_expresion_isnull_(t):
    ''' expresion_whereb : expresion_dato IS NULL '''
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS NULL")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.NULL)
        
def p_experesion_isnull_2(t):
    ' expresion_whereb : expresion_dato ISNULL'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> ISNULL")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.ISNULL)

def p_expresion_notnull(t):
    ' expresion_whereb : expresion_dato NOTNULL'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> NOTNULL")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.NOTNULL)

def p_expresion_true(t):
    ' expresion_whereb : expresion_dato IS TRUE'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS TRUE")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.TRUE)

def p_expresion_not_true(t):
    ' expresion_whereb : expresion_dato IS NOT TRUE'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS NOT TRUE")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.N_TRUE)

def p_expresion_false(t):
    'expresion_whereb : expresion_dato IS FALSE'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS FALSE")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.FALSE)

def p_expresion_UNKNOWN(t):
    ' expresion_whereb : expresion_dato IS UNKNOWN'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS UNKNOWN")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.UNKNOWN)

def p_expresion_UNKNOWN_(t):
    ' expresion_whereb : expresion_dato IS NOT UNKNOWN'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS NOT UNKNOWN")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.UNKNOWN)


def p_expresion_whereb(t):
    '''expresion_whereb :     expresion_wherea MAYOR expresion_wherea
                             | expresion_wherea MENOR expresion_wherea
                             | expresion_wherea MAYORIGUAL expresion_wherea
                             | expresion_wherea MENORIGUAL expresion_wherea
                             | expresion_wherea IGUALIGUAL expresion_wherea
                             | expresion_wherea IGUAL expresion_wherea
                             | expresion_wherea NOIG expresion_wherea
                             | expresion_wherea NOIGUAL expresion_wherea '''

    if t[2] == '>':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> MAYOR <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYOR)
    elif t[2] == '<':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> MENOR <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MENOR)
    elif t[2] == '>=':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> MAYORIGUAL <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYORIGUAL)
    elif t[2] == '<=':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> MENORIGUAL <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MENORIGUAL)
    elif t[2] == '==':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> IGUALIGUAL <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.DOBLEIGUAL)
    elif t[2] == '=':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> IGUAL <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.IGUAL)
    elif t[2] == '<>':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> NOIG <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.NOIG)
    elif t[2] == '!=':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> NOIGUAL <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.DIFERENTE)

def p_expresion_whereb2(t):
    ' expresion_whereb : expresion_wherea '
    reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea>")
    t[0] = t[1]

def p_expresion_logica_w(t):
    ''' expresion_logica_w :  expresion_logica_w AND expresion_whereb
                            | expresion_logica_w OR expresion_whereb ''' 


    if t[2].upper() == 'AND':
        reporte_bnf.append("<expresion_logica_w> ::= <expresion_logica_w> AND <expresion_whereb>")
        t[0] = ExpresionLogica(t[1],t[3],OPERACION_LOGICA.AND)
    elif t[2].upper() == 'OR':
        reporte_bnf.append("<expresion_logica_w> ::= <expresion_logica_w> OR <expresion_whereb>")
        t[0] = ExpresionLogica(t[1],t[3],OPERACION_LOGICA.OR) 

def p_expresion_logica_between(t):
    ' expresion_logica_w :  expresion_logica_w BETWEEN expresion_whereb'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_logica_w> BETWEEN <expresion_whereb>")
    if t[2].upper() == 'BETWEEN' : t[0] = ExpresionLogica(t[1],t[3],OPCION_VERIFICAR.BETWEEN)

def p_expresion_logica_between_1(t):
    ' expresion_logica_w :  expresion_wherea BETWEEN expresion_wherea AND expresion_wherea'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_wherea> BETWEEN <expresion_wherea> AND <expresion_wherea>")
    if t[2].upper() == 'BETWEEN' and t[4].upper() == 'AND' : t[0] = ExpresionLogica(ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYOR),ExpresionRelacional(t[1],t[5],OPERACION_RELACIONAL.MENOR),OPCION_VERIFICAR.BETWEEN_1)


def p_expresion_logica_between_NOT(t):
    ' expresion_logica_w : expresion_dato NOT BETWEEN expresion_dato AND expresion_dato'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> NOT BETWEEN <expresion_dato> AND <expresion_dato>")
    if t[3].upper() == 'BETWEEN' and t[2].upper() == 'NOT' : t[0] = ExpresionLogica(ExpresionRelacional(t[1],t[4],OPERACION_RELACIONAL.MAYOR),ExpresionRelacional(t[1],t[6],OPERACION_RELACIONAL.MENOR),OPCION_VERIFICAR.N_BETWEEN)

def p_expresion_logica_between_distict(t):
    ' expresion_logica_w : expresion_dato IS DISTINCT FROM expresion_dato'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> IS DISTINCT FROM <expresion_dato>")
    if t[3].upper() == 'DISTINCT' : t[0] = ExpresionLogica(ExpresionRelacional(t[1],t[5],OPERACION_RELACIONAL.DIFERENTE), ExpresionRelacional(t[1],t[5],OPERACION_RELACIONAL.DIFERENTE), OPCION_VERIFICAR.ISDISTINCT)


def p_expresion_logica_between_notdistict(t):
    ' expresion_logica_w :  expresion_dato IS NOT DISTINCT FROM expresion_dato'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> IS NOT DISTINCT FROM expresion_dato")
    if t[3].upper() == 'NOT' and t[4].upper() == 'DISTINCT' : t[0] = ExpresionLogica(ExpresionRelacional(t[1],t[6],OPERACION_RELACIONAL.DOBLEIGUAL), ExpresionRelacional(t[1],t[6],OPERACION_RELACIONAL.DOBLEIGUAL), OPCION_VERIFICAR.NOT_DISTINCT)


def p_expresion_logica_between_like(t):
    'expresion_logica_w : expresion_dato LIKE CADENA'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> LIKE CADENA")
    if t[2].upper() == 'LIKE' : t[0] = ExpresionLogica(ExpresionRelacional(t[1],ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[3]),OPERACION_RELACIONAL.DOBLEIGUAL), ExpresionRelacional(t[1],ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[3]),OPERACION_RELACIONAL.DOBLEIGUAL), OPCION_VERIFICAR.LIKE)

def p_expresion_logica_between_NOTLIKE(t):
    'expresion_logica_w : expresion_dato NOT LIKE CADENA'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> NOT LIKE CADENA")
    if t[3].upper() == 'LIKE' and t[2].upper() == 'NOT' : t[0] = ExpresionLogica(ExpresionRelacional(t[1],ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[4]),OPERACION_RELACIONAL.DIFERENTE), ExpresionRelacional(t[1],ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[4]),OPERACION_RELACIONAL.DIFERENTE), OPCION_VERIFICAR.NOT_LIKE)

def p_expresion_logica_w2(t):
    ' expresion_logica_w : NOT expresion_logica_w '
    reporte_bnf.append("<expresion_logica_w> ::= NOT <expresion_logica_w>")
    t[0] = ExpresionLogica(t[2],None,OPERACION_LOGICA.NOT)

def p_expresion_logica_w3(t):
    ' expresion_logica_w : expresion_whereb '
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_whereb>")
    t[0] = t[1]




#? ###################################################################
# SECTION             AGREGADOS CAPITULO 11
#? ###################################################################


#? ###################################################################
# TODO                         INDEX
#? ###################################################################
def p_ins_createIndex(t):
    'instruccion : createIndex'
    t[0] = t[1]

def p_createIndex(t):
    ' createIndex : CREATE INDEX ID ON ID opc_index PTCOMA '
    t[0] = Funcion_Index(INDEX.INDEX,t[3],t[5],t[6],None)
    
def p_createIndex1(t):
    ' createIndex : CREATE INDEX ID ON ID opc_index cond_where PTCOMA '
    t[0] = Funcion_Index(INDEX.INDEX_WHERE,t[3],t[5],t[6],t[7])

def p_createIndex2(t):
    ' createIndex : CREATE INDEX ID ON ID opc_index INCLUDE opc_index PTCOMA '
    t[0] = Funcion_Index(INDEX.INDEX_INCLUDE,t[3],t[5],t[6],t[8])

def p_createIndex3(t):
    ' createIndex : CREATE UNIQUE INDEX ID ON ID opc_index PTCOMA '
    t[0] = Funcion_Index(INDEX.INDEX_UNIQUE_WHERE,t[4],t[6],t[7],None)

def p_createIndex4(t):
    ' createIndex : CREATE UNIQUE INDEX ID ON ID opc_index cond_where PTCOMA '
    t[0] = Funcion_Index(INDEX.INDEX_INCLUDE,t[4],t[6],t[7],t[8])

def p_createIndex5(t):
    ' createIndex : CREATE UNIQUE INDEX ID ON ID opc_index INCLUDE opc_index PTCOMA '
    t[0] = Funcion_Index(INDEX.INDEX_INCLUDE,t[4],t[6],t[7],t[9])

def p_otro_index(t):
    'createIndex : CREATE INDEX ID ON ID PARA ID opclass PARC PTCOMA'
    t[0] = Funcion_Index(INDEX.INDEX_CLASS,t[3],t[5],t[7],t[8])
    
def p_otro_index1(t):
    'createIndex : CREATE INDEX ID ON ID PARA ID opclass sortoptions PARC PTCOMA'
    t[0] = Funcion_Index(t[3],t[5],t[7],t[8],t[9])

def p_createIndex6(t):
    '''opc_index :  USING HASH PARA ID PARC
                  | PARA opc_index_par PARC'''
    if t[1].upper() == 'USING':
        t[0] = index_cuerpo(TIPO_INDEX.USING_HASH,t[4],None)
    else:
        t[0]= t[2]

def p_createIndex2_0(t):
    ' opc_index_par : campos_c '
    t[0] = index_cuerpo(TIPO_INDEX.CAMPOS,t[1],None)

def p_createIndex2_1(t):
    ' opc_index_par : ID NULLS first_last'
    t[0] = index_cuerpo(TIPO_INDEX.NULLS,t[1],t[3])

def p_createIndex2_1_1(t):
    ' opc_index_par : ID orden NULLS first_last '
    t[0] = index_cuerpo(TIPO_INDEX.NULLS,t[1], t[4])

def p_createIndex2_3(t):
    ' opc_index_par : ID COLLATE string_type '   
    t[0] = index_cuerpo(TIPO_INDEX.COLLATE,t[1],t[3])

def p_createIndex2_30(t):
    ' opc_index_par : LOWER PARA ID PARC '
    t[0] = index_cuerpo(TIPO_INDEX.LOWER,t[3],None)

def p_createIndex_5(t):
    ' opc_index_par : ID PARA ID PARC '
    t[0] = index_cuerpo(TIPO_INDEX.WITH_IDS,t[1],t[3])

def p_first_last(t):
    ''' first_last : FIRST
                   | LAST'''
    t[0] = t[1]


def p_sortoptions(t):
    'sortoptions : sortoptions sortoption'
    t[1].append(t[2])
    t[0] = t[1]

def p_sortoptions0(t):
    'sortoptions : sortoption'
    t[0] = t[1]

def p_sortoptions1(t):
    '''sortoption : COLLATE
                    | ASC
                    | DESC '''
    t[0] = t[1]


 
def p_sortoptions2(t):
    '''sortoption :  NULLS FIRST
                    | NULLS LAST '''
    t[0] = t[2]

def p_opclass(t):
    '''opclass : TEXT_PATTERN_OPS
               | VARCHAR_PATTERN_OPS
               | BPCHAR_PATTERN_OPS '''
    t[0] = t[1]
