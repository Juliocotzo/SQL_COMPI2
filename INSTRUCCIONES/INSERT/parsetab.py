
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMAYQUEMENQUEMAYIGQUEMENIGQUEleftIGUALNOIGNOIGUALleftANDORleftSUMARESTAleftMULTIDIVISIONABS ACOS ACOSD ACOSH ADD ALL ALTER AND ANY AS ASC ASIN ASIND ASINH ASTERISCO ATAN ATAN2 ATAN2D ATAND ATANH AVG BETWEEN BIGINT BY CADENA CASE CBRT CEIL CEILING CEJILLA CHAR CHARACTER CHECK COLUMN COMA CONSTRAINT CONVERT COS COSD COSH COT COTD COUNT CREATE CURRENT_DATE CURRENT_TIME CURRENT_USER DATABASE DATE DATE_PART DAY DECIMAL DECODE DEGREES DELETE DESC DISTINCT DIV DIVISION DOBLEIG DOUBLE DROP D_OR ELSE ENCODE END ENTERO ENUM EXCEPT EXISTS EXP EXTRACT FACTORIAL FALSE FLOAT FLOOR FLOTANTE FOREIGN FOREING FROM FULL GCD GET_BYTE GROUP HASHTAG HAVING HOUR ID IGUAL IN INHERITS INNER INSERT INTEGER INTERSECT INTERVAL INTO IS ISNULL JOIN KEY LCM LEFT LENGTH LIKE LIMIT LN LOG LOG10 MAX MAYIGQUE MAYMAY MAYQUE MD5 MENIGQUE MENMEN MENQUE MIN MINUTE MIN_SCALE MOD MODULO MONEY MONTH MULTI NATURAL NOIG NOIGUAL NOT NOTNULL NOW NULL NUMERIC OFFSET ON ONLY OR ORDER OUTER OWNER PAR_A PAR_C PI POWER PRECISION PRIMARY PTCOMA PUNTO RADIANS RANDOM REAL REFERENCES RENAME RESTA RETURNING RIGHT ROUND SCALE SECOND SELECT SESSION_USER SET SETSEED SET_BYTE SHA256 SIGN SIN SIND SINH SMALLINT SOME SQRT SUBSTR SUBSTRING SUM SUMA SYMMETRIC S_OR TABLE TAN TAND TANH TEXT THEN TIME TIMESTAMP TO TRIM TRIM_SCALE TRUC TRUE TYPE UNION UNIQUE UNKNOWN UPDATE USE USING VALUES VARCHAR VARYING WHEN WHERE WIDTH_BUCKET Y YEARinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion : insert_insrt insert_insrt : INSERT INTO ID PAR_A lista_parametros_lista PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA  insert_insrt : INSERT INTO ID PAR_A  PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA  insert_insrt : INSERT INTO ID VALUES PAR_A lista_datos PAR_C PTCOMA  lista_parametros_lista : lista_parametros_lista COMA ID lista_parametros_lista : ID lista_datos : lista_datos COMA expresion lista_datos : expresion agrupacion_expresion : PAR_A expresion PAR_Cexpresion : CADENAexpresion : ENTERO \n                   | FLOTANTEexpresion : ID expresion : ID PUNTO ID expresion : expresion SUMA expresion \n                 | expresion RESTA expresion\n                 | expresion DIVISION expresion\n                 | expresion ASTERISCO expresion  expresion_relacional : expresion MAYQUE expresion\n                             | expresion MENQUE expresion\n                             | expresion MAYIGQUE expresion\n                             | expresion MENIGQUE expresion\n                             | expresion DOBLEIG expresion\n                             | expresion IGUAL expresion\n                             | expresion NOIG expresion\n                             | expresion NOIGUAL expresion'
    
_lr_action_items = {'INSERT':([0,2,3,4,6,37,46,47,],[5,5,-3,-4,-2,-7,-6,-5,]),'$end':([1,2,3,4,6,37,46,47,],[0,-1,-3,-4,-2,-7,-6,-5,]),'INTO':([5,],[7,]),'ID':([7,9,14,16,26,27,29,30,31,32,33,34,],[8,11,18,25,18,36,18,18,18,18,18,18,]),'PAR_A':([8,10,17,24,],[9,14,26,34,]),'VALUES':([8,13,15,],[10,17,24,]),'PAR_C':([9,11,12,18,19,20,21,22,23,25,35,36,38,39,40,41,42,43,],[13,-9,15,-16,28,-11,-13,-14,-15,-8,44,-17,-10,-18,-19,-20,-21,45,]),'COMA':([11,12,18,19,20,21,22,23,25,35,36,38,39,40,41,42,43,],[-9,16,-16,29,-11,-13,-14,-15,-8,29,-17,-10,-18,-19,-20,-21,29,]),'CADENA':([14,26,29,30,31,32,33,34,],[21,21,21,21,21,21,21,21,]),'ENTERO':([14,26,29,30,31,32,33,34,],[22,22,22,22,22,22,22,22,]),'FLOTANTE':([14,26,29,30,31,32,33,34,],[23,23,23,23,23,23,23,23,]),'SUMA':([18,20,21,22,23,36,38,39,40,41,42,],[-16,30,-13,-14,-15,-17,30,-18,-19,-20,30,]),'RESTA':([18,20,21,22,23,36,38,39,40,41,42,],[-16,31,-13,-14,-15,-17,31,-18,-19,-20,31,]),'DIVISION':([18,20,21,22,23,36,38,39,40,41,42,],[-16,32,-13,-14,-15,-17,32,32,32,-20,32,]),'ASTERISCO':([18,20,21,22,23,36,38,39,40,41,42,],[-16,33,-13,-14,-15,-17,33,-18,-19,-20,33,]),'PUNTO':([18,],[27,]),'PTCOMA':([28,44,45,],[37,46,47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,6,]),'insert_insrt':([0,2,],[4,4,]),'lista_parametros_lista':([9,],[12,]),'lista_datos':([14,26,34,],[19,35,43,]),'expresion':([14,26,29,30,31,32,33,34,],[20,20,38,39,40,41,42,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica_insert.py',348),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica_insert.py',352),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica_insert.py',357),
  ('instruccion -> insert_insrt','instruccion',1,'p_instruccion_f_select','gramatica_insert.py',374),
  ('insert_insrt -> INSERT INTO ID PAR_A lista_parametros_lista PAR_C VALUES PAR_A lista_datos PAR_C PTCOMA','insert_insrt',11,'p_insert_insrt','gramatica_insert.py',381),
  ('insert_insrt -> INSERT INTO ID PAR_A PAR_C VALUES PAR_A lista_datos PAR_C PTCOMA','insert_insrt',10,'p_opcion_lista_parametros_','gramatica_insert.py',386),
  ('insert_insrt -> INSERT INTO ID VALUES PAR_A lista_datos PAR_C PTCOMA','insert_insrt',8,'p_opcion_lista_parametros_vacios','gramatica_insert.py',390),
  ('lista_parametros_lista -> lista_parametros_lista COMA ID','lista_parametros_lista',3,'p_lista_parametros_lista','gramatica_insert.py',396),
  ('lista_parametros_lista -> ID','lista_parametros_lista',1,'p_lista_parametros','gramatica_insert.py',401),
  ('lista_datos -> lista_datos COMA expresion','lista_datos',3,'p_parametros_lista_datos','gramatica_insert.py',410),
  ('lista_datos -> expresion','lista_datos',1,'p_expresion_lista','gramatica_insert.py',415),
  ('agrupacion_expresion -> PAR_A expresion PAR_C','agrupacion_expresion',3,'p_agrupacion_expresion','gramatica_insert.py',419),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','gramatica_insert.py',424),
  ('expresion -> ENTERO','expresion',1,'p_expresion1','gramatica_insert.py',429),
  ('expresion -> FLOTANTE','expresion',1,'p_expresion1','gramatica_insert.py',430),
  ('expresion -> ID','expresion',1,'p_expresion3','gramatica_insert.py',435),
  ('expresion -> ID PUNTO ID','expresion',3,'p_expresion4','gramatica_insert.py',439),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion','gramatica_insert.py',443),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion','gramatica_insert.py',444),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresion','gramatica_insert.py',445),
  ('expresion -> expresion ASTERISCO expresion','expresion',3,'p_expresion','gramatica_insert.py',446),
  ('expresion_relacional -> expresion MAYQUE expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',454),
  ('expresion_relacional -> expresion MENQUE expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',455),
  ('expresion_relacional -> expresion MAYIGQUE expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',456),
  ('expresion_relacional -> expresion MENIGQUE expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',457),
  ('expresion_relacional -> expresion DOBLEIG expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',458),
  ('expresion_relacional -> expresion IGUAL expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',459),
  ('expresion_relacional -> expresion NOIG expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',460),
  ('expresion_relacional -> expresion NOIGUAL expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',461),
]
