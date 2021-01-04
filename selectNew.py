
#?######################################################
# TODO      INSTRUCCION SELECT
#?######################################################


def p_instruccion_select_insrt(t):
    ' select_insrt : SELECT opcion_select_tm'  
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_select_tm3(t):
    'opcion_select_tm : greatest_insrt' #YA ESTA
    t[0] = ' ' + str(t[1]) + ' '

def p_select_lista(t):
    ' opcion_select_lista : DISTINCT campos_c '
    # ES UNA LISTA t[2]
    cadena = ""
    for i in t[2]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(cadena) + ' '

def p_select_lista2(t):
    ' opcion_select_lista : opciones_select_lista'
    #LISTA t[1]
    cadena = ""
    for i in t[1]:
        cadena += str(i)
    t[0] = ' ' + str(cadena) + ' '

def p_opciones_select_lista(t):
    ''' opciones_select_lista : opciones_select_lista COMA opcion_select '''
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_select_lista2(t):
    ' opciones_select_lista : opcion_select'
    t[0] = [t[1]]

def p_opcion_select_tm1(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_sobrenombres '
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '

def p_opcion_select_tm2(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_sobrenombres opcion_from '
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) + ' '

def p_opciones_sobrenombre(t):
    '''opciones_sobrenombres : opciones_sobrenombres COMA opcion_sobrenombre '''
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_sobrenombre2(t):
    ' opciones_sobrenombres : opcion_sobrenombre '
    t[0] = [t[1]]

def p_opcion_select_tm_op1(t):
    'opcion_select_tm : opcion_select_lista seguir_sobrenombre FROM otros_froms '
    # ES UNA LISTA t[4]
    cadena = ""
    for i in t[4]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(cadena) + ' '

def p_otros_from(t):
    'otros_froms : otros_froms COMA otro_from'
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_otros_from2(t):
    'otros_froms : otro_from'
    t[0] = [t[1]]

def p_opcion_select_tm(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_from opcion_from'
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4])

def p_opciones_from(t):
    '''opciones_from : opciones_from COMA from_s'''
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_from2(t):
    'opciones_from : from_s'
    t[0] = [t[1]]

def p_ins_1(t):
    'opcion_select_tm : varias_funciones'
    # ES UNA LISTA t[1]
    cadena = ""
    for i in t[1]:
        cadena+= str(i)
    t[0] = ' ' + str(cadena) + ' '

def p_varias_funciones(t):
    'varias_funciones : varias_funciones COMA funcion'
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_varias_funciones1(t):
    'varias_funciones : funcion'
    t[0] = [t[1]]

def p_funcion(t):
    'funcion : funciones_select seguir_sobrenombre'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_funcion1(t):
    'funcion : funciones_select'
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select_tm_op2(t):
    '''otro_from : from_s '''
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select_tm_op3(t):
    'otro_from : from_s opcion_from'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_s(t):
    ''' from_s : ID'''
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_s2(t):
    ' from_s : PARA'
    t[0] = ' ' + str(t[1]) + ' '


def p_sobre_Nombre(t):
    ''' opcion_sobrenombre : ID seguir_sobrenombre'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '
    
    
def p_sobre_Nombre2(t):
    ' opcion_sobrenombre : ID '
    t[0] = ' ' + str(t[1]) + ' '

def p_as_ID(t):
    ''' as_ID : ID '''
    t[0] = ' ' + str(t[1]) + ' '

def p_as_ID2(t):
    'as_ID : CADENA'
    cadena = '\\\''+t[1]+'\\\''
    t[0] = ' ' + str(cadena) + ' '
#---------------------------------------------------------

def p_alias(t):
    ''' seguir_sobrenombre : AS as_ID'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '
def p_alias2(t):
    'seguir_sobrenombre : ID'
    t[0] = t[1]
    t[0] = ' ' + str(t[1]) + ' '

def p_alias3(t):
    'seguir_sobrenombre : PUNTO ID'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_select_tm_extract(t):
    'opcion_select_tm : EXTRACT PARA extract_time FROM TIMESTAMP CADENA  PARC '
    cadena = '\\\''+t[6]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(cadena) + ' '+ str(t[7]) + ' '

def p_opcion_select_tm_date(t):
    'opcion_select_tm : DATE_PART PARA CADENA COMA INTERVAL CADENA PARC  '
    cadena = '\\\''+t[3]+'\\\''
    cadena1 = '\\\''+t[6]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(cadena1) + ' '+ str(t[7]) + ' '

def p_opcion_select_tm_now(t):
    'opcion_select_tm : NOW PARA PARC '
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_select_tm_current(t):
    'opcion_select_tm : CURRENT_DATE '
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select_tm_crtm(t):
    'opcion_select_tm : CURRENT_TIME '
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select_tm_timestamp(t):
    'opcion_select_tm : TIMESTAMP CADENA '
    cadena = '\\\''+t[2]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(cadena) + ' '



#?######################################################
# TODO      OFFSET
#?######################################################

def p_opcion_from_0_0_1_1_1_1_1_0(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '

def p_opcion_from_0_0_0_1_1_1_1_0(t):
    'opcion_from :  cond_gb cond_having cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '
    
def p_opcion_from_0_0_1_0_1_1_1_0(t):
    'opcion_from : cond_where cond_having cond_ob orden cond_limit OFFSET ENTERO'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '

def p_opcion_from_0_0_0_0_1_1_1_0(t):
    'opcion_from :  cond_having cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_1_1_0_1_1_0(t):
    'opcion_from : cond_where cond_gb cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_opcion_from_0_0_0_1_0_1_1_0(t):
    'opcion_from :  cond_gb cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_1_0_0_1_1_0(t):
    'opcion_from : cond_where cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_0_0_1_1_0(t):
    'opcion_from :  cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_1_1_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_opcion_from_0_0_0_1_1_1_1_0_ordeno(t):
    'opcion_from : cond_gb cond_having cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_1_0_1_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_having cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_0_1_1_1_0_ordeno(t):
    'opcion_from :  cond_having cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_1_0_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_gb  cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_0_1_1_0_ordeno(t):
    'opcion_from :  cond_gb cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_0_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_0_1_1_0_ordeno(t):
    'opcion_from :  cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_1_0_1_0(t):
    'opcion_from : cond_where cond_gb cond_having cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_1_0_1_0(t):
    'opcion_from :  cond_gb cond_having cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_1_0_1_0(t):
    'opcion_from : cond_where cond_having cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_1_0_1_0(t):
    'opcion_from :  cond_having cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_0_0_1_0(t):
    'opcion_from : cond_where cond_gb cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_0_0_1_0(t):
    'opcion_from :  cond_gb cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_0_0_1_0(t):
    'opcion_from : cond_where cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_0_0_1_0(t):
    'opcion_from :  cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_1_1_1_0_offno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_opcion_from_0_0_0_1_1_1_1_0_offno(t):
    'opcion_from :  cond_gb cond_having cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_1_0_1_1_1_0_offno(t):
    'opcion_from : cond_where cond_having cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_0_1_1_1_0_offno(t):
    'opcion_from :  cond_having cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_1_0_1_1_0_offno(t):
    'opcion_from : cond_where cond_gb cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_0_1_1_0_offno(t):
    'opcion_from :  cond_gb cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_0_1_1_0_offno(t):
    'opcion_from : cond_where cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_0_1_1_0_offno(t):
    'opcion_from :  cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_1_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_1_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_gb cond_having cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_1_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_having cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_1_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_having cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_0_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_gb cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_0_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_gb cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_0_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_0_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_1_0_1_0_offno(t):
    'opcion_from :  cond_where cond_gb cond_having cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_1_0_1_0_offno(t):
    'opcion_from :  cond_gb cond_having cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_1_0_1_0_offno(t):
    'opcion_from :  cond_where cond_having cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_1_0_1_0_offno(t):
    'opcion_from :  cond_having cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_0_0_1_0_offno(t):
    'opcion_from :  cond_where cond_gb cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_1_0_0_1_0_offno(t):
    'opcion_from :  cond_gb  cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_0_0_0_1_0_offno(t):
    'opcion_from :  cond_where cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_0_0_0_0_1_0_offno(t):
    'opcion_from :  cond_limit'
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_from_0_0_1_1_1_1_0_0(t):
    'opcion_from :  cond_where cond_gb cond_having cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_1_1_0_0(t):
    'opcion_from :  cond_gb cond_having cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_1_1_0_0(t):
    'opcion_from :  cond_where cond_having cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_1_1_0_0(t):
    'opcion_from :  cond_having cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_0_1_0_0(t):
    'opcion_from :  cond_where cond_gb cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_0_1_0_0(t):
    'opcion_from :  cond_gb  cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_0_1_0_0(t):
    'opcion_from :  cond_where cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_0_1_0_0(t):
    'opcion_from :  cond_ob'
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_from_0_0_1_1_1_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_gb cond_having cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_1_1_0_0_ordeno(t):
    'opcion_from :  cond_gb cond_having cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_1_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_having cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_1_1_0_0_ordeno(t):
    'opcion_from :  cond_having cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_0_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_gb cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_1_0_1_0_0_ordeno(t):
    'opcion_from :  cond_gb cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_0_0_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_1_0_0_0(t):
    'opcion_from : cond_where cond_gb cond_having'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_1_1_0_0_0(t):
    'opcion_from :  cond_gb cond_having'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_0_1_0_0_0(t):
    'opcion_from : cond_where cond_having'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_0_0_1_0_0_0(t):
    'opcion_from :  cond_having'
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_from_0_0_1_1_0_0_0_0(t):
    'opcion_from : cond_where cond_gb '
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_0_1_0_0_0_0(t):
    'opcion_from :  cond_gb '
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_from_0_0_1_0_0_0_0_0(t):
    'opcion_from : cond_where'
    t[0] = ' ' + str(t[1]) + ' '


    
#? ####################################################################
# TODO              OPCIONES DE FROM 
#? ####################################################################

def p_opcion_from_2(t):
    'opcion_from :   select_insrt PARC ID '
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_3(t):
    'opcion_from :   select_insrt PARC'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_cond_where(t):
    'cond_where : WHERE expresion_where'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_cond_GB(t):
    'cond_gb : GROUP BY campos_c '
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena+= str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '


def p_cond_Having(t):
    'cond_having : HAVING expresion_logica'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_cond_OB(t):
    'cond_ob : ORDER BY campos_c'  #######
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena+=str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '

def p_cond_limit(t):
    'cond_limit : LIMIT opc_lim'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_cond_offset(t):
    'cond_offset : OFFSET ENTERO'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

#? ####################################################################
# TODO              LIM,ORDEN
#? ####################################################################

def p_opc_lim(t):
    '''opc_lim : ENTERO'''
    t[0] = ' ' + str(t[1]) + ' '

def p_opc_lim2(t):
    ' opc_lim : POR '
    t[0] = ' ' + str(t[1]) + ' '

def p_ORDER(t):
    ''' orden : DESC '''
    t[0] = ' ' + str(t[1]) + ' '

def p_ORDER2(t):
    ''' orden : ASC '''
    t[0] = ' ' + str(t[1]) + ' '






 
#? ####################################################################
# TODO          EXPRESION DATOS - FALTA
#? ####################################################################


def p_sin_some_any(t):
    '''sin_some_any : SOME '''
    t[0] = ' ' + str(t[1]) + ' '

def p_sin_some_any2(t):
    '''sin_some_any : ANY  '''
    t[0] = ' ' + str(t[1]) + ' '









#? ####################################################################
# TODO              EXPRESION SELECT
#? ####################################################################


def p_opcion_select1(t):
    ' opcion_select :  PARA select_insrt PARC '
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_select2(t):
    ' opcion_select :   expresion '
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select3(t):
    'opcion_select :  funciones_select '
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select4(t):
    'opcion_select :  POR '
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select5(t):
    ' opcion_select : ID PUNTO POR '
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_greatest_insrt(t):
    ''' greatest_insrt : GREATEST PARA greatest_val PARC
                        | LEAST PARA greatest_val PARC'''
    cadena = ""
    for i in t[3]:
        cadena+=str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) + ' '

def p_greatest_insrt1(t):
    ' greatest_val : greatest_val COMA expresion_dato '
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_greatest_insrt2(t):
    ' greatest_val : expresion_dato'
    t[0] = [t[1]]

##################################EXPRESIONES#####################################
def p_funciones_select(t):
    ''' funciones_select : ABS PARA expresion PARC
                        | CBRT PARA expresion PARC
                        | CEIL PARA expresion PARC 
                        | CEILING PARA expresion PARC 
                        | DEGREES PARA expresion PARC 
                        | EXP PARA expresion PARC 
                        | FACTORIAL PARA expresion PARC 
                        | FLOOR PARA expresion PARC 
                        | LN PARA expresion PARC 
                        | LOG PARA expresion PARC 
                        | RADIANS PARA expresion PARC 
                        | ROUND PARA expresion PARC 
                        | SIGN PARA expresion PARC 
                        | SQRT PARA expresion PARC
                        | TRUNC PARA expresion PARC 
                        | ACOS PARA expresion PARC
                        | ASIND PARA expresion PARC
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
                        | TRIM PARA string_type PARC
                        | SHA256 PARA string_type PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_funciones_select__15(t):
    ''' funciones_select : DIV PARA expresion COMA expresion PARC '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_funciones_select__16(t):
    ''' funciones_select : GCD PARA expresion COMA expresion PARC
                        | MOD PARA expresion COMA expresion PARC 
                        | POWER PARA expresion COMA expresion PARC 
                        | TRUNC PARA expresion COMA ENTERO PARC
                        | ATAN2 PARA expresion COMA expresion PARC
                        | ATAN2D PARA expresion COMA expresion PARC
                        | CONVERT PARA string_type AS TIPO_DATO PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_funciones_select__18(t):
    ''' funciones_select : SUBSTRING PARA string_type COMA expresion COMA expresion PARC
                        | SUBSTR PARA string_type COMA expresion COMA expresion PARC
                        | GET_BYTE PARA string_type D_DOSPTS BYTEA COMA ENTERO PARC
                        | ENCODE PARA string_type D_DOSPTS BYTEA COMA formato_texto PARC
                        | DECODE PARA string_type D_DOSPTS BYTEA COMA formato_texto PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '

def p_funciones_select__10(t):
    ''' funciones_select : WIDTH_BUCKET PARA expresion COMA expresion COMA expresion COMA expresion PARC 
                        | SET_BYTE PARA string_type D_DOSPTS BYTEA COMA ENTERO COMA ENTERO PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ' '+ str(t[10]) + ' '

def p_funciones_select__11(t):
    ''' funciones_select : PI PARA PARC 
                        | RANDOM PARA PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_formato_texto(t):
    ''' formato_texto : ESCAPE '''
    t[0] = ' ' + str(t[1]) + ' '

def p_formato_texto_hex(t):
    'formato_texto : HEX'
    t[0] = ' ' + str(t[1]) + ' '

def p_formato_texto_base64(t):
    ' formato_texto : BASE64'
    t[0] = ' ' + str(t[1]) + ' '

                 

#? ###################################################################
# TODO              EXPRESION WHERE
#? ###################################################################
                 
def p_expresion_where2(t):
    'expresion_where : expresion_logica_w'
    t[0] = ' ' + str(t[1]) + ' '

def p_expresion_where(t):
    ''' expresion_where : expresion_dato NOT IN PARA select_insrt PARC '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_expresion_where_11(t):
    ''' expresion_where : expresion_dato IN PARA select_insrt PARC
                        | NOT EXISTS PARA select_insrt PARC '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_expresion_where_3(t):
    ''' expresion_where : expresion_dato NOT BETWEEN SYMMETRIC expresion_dato AND expresion_dato'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '


def p_expresion_wherea(t):
    '''expresion_wherea :  ABS PARA expresion PARC
                        | LENGTH PARA string_type PARC
                        | CBRT PARA expresion PARC
                        | CEIL PARA expresion PARC 
                        | CEILING PARA expresion PARC 
                        | sin_some_any PARA select_insrt PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_expresion_wherea_1(t):
    '''expresion_wherea :  SUBSTRING PARA string_type COMA expresion COMA expresion PARC
                        | SUBSTR PARA string_type COMA expresion COMA expresion PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '

def p_expresion_wherea_2(t):
    '''expresion_wherea :  TRIM PARA string_type D_DOSPTS BYTEA FROM string_type D_DOSPTS BYTEA PARC '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ' '+ str(t[10]) + ' '

def p_expresion_wherea_3(t):
    '''expresion_wherea :  EXTRACT PARA extract_time FROM string_type PARC '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_expresion_wherea2(t):
    ''' expresion_wherea : expresion '''
    t[0] = ' ' + str(t[1]) + ' '

#? #########################################################
#ANCHOR       EXPRESIONES AGREGADAS AL WHERE
#? ##################################################
def p_expresion_wherea3(t):
    ''' expresion_wherea : LOWER PARA string_type PARC '''
    #NADA

def p_expresion_wherea4(t):
    ''' expresion_wherea : ID PARA ID PARC'''
    #NADA


def p_expresion_isnull_(t):
    ''' expresion_whereb : expresion_dato IS NULL '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '
        
def p_experesion_isnull_2(t):
    ' expresion_whereb : expresion_dato ISNULL'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_expresion_notnull(t):
    ' expresion_whereb : expresion_dato NOTNULL'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_expresion_true(t):
    ' expresion_whereb : expresion_dato IS TRUE'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_not_true(t):
    ' expresion_whereb : expresion_dato IS NOT TRUE'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_expresion_false(t):
    'expresion_whereb : expresion_dato IS FALSE'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_UNKNOWN(t):
    ' expresion_whereb : expresion_dato IS UNKNOWN'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_UNKNOWN_(t):
    ' expresion_whereb : expresion_dato IS NOT UNKNOWN'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '


def p_expresion_whereb(t):
    '''expresion_whereb :     expresion_wherea MAYOR expresion_wherea
                             | expresion_wherea MENOR expresion_wherea
                             | expresion_wherea MAYORIGUAL expresion_wherea
                             | expresion_wherea MENORIGUAL expresion_wherea
                             | expresion_wherea IGUALIGUAL expresion_wherea
                             | expresion_wherea IGUAL expresion_wherea
                             | expresion_wherea NOIG expresion_wherea
                             | expresion_wherea NOIGUAL expresion_wherea '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_whereb2(t):
    ' expresion_whereb : expresion_wherea '
    t[0] = ' ' + str(t[1]) + ' '

def p_expresion_logica_w(t):
    ''' expresion_logica_w :  expresion_logica_w AND expresion_whereb
                            | expresion_logica_w OR expresion_whereb ''' 
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_logica_between(t):
    ' expresion_logica_w :  expresion_logica_w BETWEEN expresion_whereb'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_logica_between_1(t):
    ' expresion_logica_w :  expresion_wherea BETWEEN expresion_wherea AND expresion_wherea'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '


def p_expresion_logica_between_NOT(t):
    ' expresion_logica_w : expresion_dato NOT BETWEEN expresion_dato AND expresion_dato'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '


def p_expresion_logica_between_distict(t):
    ' expresion_logica_w : expresion_dato IS DISTINCT FROM expresion_dato'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '


def p_expresion_logica_between_notdistict(t):
    ' expresion_logica_w :  expresion_dato IS NOT DISTINCT FROM expresion_dato'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '


def p_expresion_logica_between_like(t):
    'expresion_logica_w : expresion_dato LIKE CADENA'
    cadena = '\\\''+t[3]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '

def p_expresion_logica_between_NOTLIKE(t):
    'expresion_logica_w : expresion_dato NOT LIKE CADENA'
    cadena = '\\\''+t[4]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(cadena) + ' '

def p_expresion_logica_w2(t):
    ' expresion_logica_w : NOT expresion_logica_w '
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '


def p_expresion_logica_w3(t):
    ' expresion_logica_w : expresion_whereb '
    t[0] = ' ' + str(t[1]) + ' '

