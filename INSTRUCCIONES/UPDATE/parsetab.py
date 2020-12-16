
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMAYQUEMENQUEMAYIGQUEMENIGQUEleftIGUALNOIGNOIGUALleftANDORleftSUMARESTAleftMULTIDIVISIONABS ACOS ACOSD ACOSH ADD ALL ALTER AND ANY AS ASC ASIN ASIND ASINH ASTERISCO ATAN ATAN2 ATAN2D ATAND ATANH AVG BETWEEN BIGINT BY CADENA CASE CBRT CEIL CEILING CEJILLA CHAR CHARACTER CHECK COLUMN COMA CONSTRAINT CONVERT COS COSD COSH COT COTD COUNT CREATE CURRENT_DATE CURRENT_TIME CURRENT_USER DATABASE DATE DATE_PART DAY DECIMAL DECODE DEGREES DELETE DESC DISTINCT DIV DIVISION DOBLEIG DOUBLE DROP D_OR ELSE ENCODE END ENTERO ENUM EXCEPT EXISTS EXP EXTRACT FACTORIAL FALSE FLOAT FLOOR FLOTANTE FOREIGN FOREING FROM FULL GCD GET_BYTE GROUP HASHTAG HAVING HOUR ID IGUAL IN INHERITS INNER INSERT INTEGER INTERSECT INTERVAL INTO IS ISNULL JOIN KEY LCM LEFT LENGTH LIKE LIMIT LN LOG LOG10 MAX MAYIGQUE MAYMAY MAYQUE MD5 MENIGQUE MENMEN MENQUE MIN MINUTE MIN_SCALE MOD MODULO MONEY MONTH MULTI NATURAL NOIG NOIGUAL NOT NOTNULL NOW NULL NUMERIC OFFSET ON ONLY OR ORDER OUTER OWNER PAR_A PAR_C PI POWER PRECISION PRIMARY PTCOMA PUNTO RADIANS RANDOM REAL REFERENCES RENAME RESTA RETURNING RIGHT ROUND SCALE SECOND SELECT SESSION_USER SET SETSEED SET_BYTE SHA256 SIGN SIN SIND SINH SMALLINT SOME SQRT SUBSTR SUBSTRING SUM SUMA SYMMETRIC S_OR TABLE TAN TAND TANH TEXT THEN TIME TIMESTAMP TO TRIM TRIM_SCALE TRUC TRUE TYPE UNION UNIQUE UNKNOWN UPDATE USE USING VALUES VARCHAR VARYING WHEN WHERE WIDTH_BUCKET Y YEARinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccion instruccion : insert_insrtinstruccion : update_insrt insert_insrt : INSERT INTO ID PAR_A lista_parametros_lista PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA  insert_insrt : INSERT INTO ID PAR_A  PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA  insert_insrt : INSERT INTO ID VALUES PAR_A lista_datos PAR_C PTCOMA  lista_parametros_lista : lista_parametros_lista COMA ID lista_parametros_lista : ID lista_datos : lista_datos COMA expresion lista_datos : expresion agrupacion_expresion : PAR_A expresion PAR_Cexpresion : CADENAexpresion : ENTERO \n                   | FLOTANTEexpresion : ID expresion : ID PUNTO ID expresion : expresion SUMA expresion \n                 | expresion RESTA expresion\n                 | expresion DIVISION expresion\n                 | expresion ASTERISCO expresion  expresion_relacional : expresion MAYQUE expresion\n                             | expresion MENQUE expresion\n                             | expresion MAYIGQUE expresion\n                             | expresion MENIGQUE expresion\n                             | expresion DOBLEIG expresion\n                             | expresion IGUAL expresion\n                             | expresion NOIG expresion\n                             | expresion NOIGUAL expresion update_insrt : UPDATE ID SET lista_update WHERE expresion_relacional PTCOMA lista_update :  lista_update COMA parametro_update lista_update : parametro_update parametro_update : ID IGUAL expresion'
    
_lr_action_items = {'INSERT':([0,2,3,4,5,8,48,60,77,78,],[6,6,-3,-4,-5,-2,-31,-8,-7,-6,]),'UPDATE':([0,2,3,4,5,8,48,60,77,78,],[7,7,-3,-4,-5,-2,-31,-8,-7,-6,]),'$end':([1,2,3,4,5,8,48,60,77,78,],[0,-1,-3,-4,-5,-2,-31,-8,-7,-6,]),'INTO':([6,],[9,]),'ID':([7,9,12,13,21,22,23,24,26,40,41,43,44,45,46,47,49,50,51,52,53,54,55,56,57,],[10,11,15,18,28,28,28,15,39,28,59,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'SET':([10,],[12,]),'PAR_A':([11,14,27,38,],[13,21,40,57,]),'VALUES':([11,20,25,],[14,27,38,]),'PAR_C':([13,18,19,28,29,30,31,32,33,39,58,59,61,62,63,64,65,74,],[20,-10,25,-17,42,-12,-14,-15,-16,-9,75,-18,-11,-19,-20,-21,-22,76,]),'IGUAL':([15,28,31,32,33,36,59,62,63,64,65,],[22,-17,-14,-15,-16,54,-18,-19,-20,-21,-22,]),'WHERE':([16,17,28,31,32,33,34,37,59,62,63,64,65,],[23,-33,-17,-14,-15,-16,-34,-32,-18,-19,-20,-21,-22,]),'COMA':([16,17,18,19,28,29,30,31,32,33,34,37,39,58,59,61,62,63,64,65,74,],[24,-33,-10,26,-17,43,-12,-14,-15,-16,-34,-32,-9,43,-18,-11,-19,-20,-21,-22,43,]),'CADENA':([21,22,23,40,43,44,45,46,47,49,50,51,52,53,54,55,56,57,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'ENTERO':([21,22,23,40,43,44,45,46,47,49,50,51,52,53,54,55,56,57,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'FLOTANTE':([21,22,23,40,43,44,45,46,47,49,50,51,52,53,54,55,56,57,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'SUMA':([28,30,31,32,33,34,36,59,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-17,44,-14,-15,-16,44,44,-18,44,-19,-20,-21,44,44,44,44,44,44,44,44,44,]),'RESTA':([28,30,31,32,33,34,36,59,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-17,45,-14,-15,-16,45,45,-18,45,-19,-20,-21,45,45,45,45,45,45,45,45,45,]),'DIVISION':([28,30,31,32,33,34,36,59,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-17,46,-14,-15,-16,46,46,-18,46,46,46,-21,46,46,46,46,46,46,46,46,46,]),'ASTERISCO':([28,30,31,32,33,34,36,59,61,62,63,64,65,66,67,68,69,70,71,72,73,],[-17,47,-14,-15,-16,47,47,-18,47,-19,-20,-21,47,47,47,47,47,47,47,47,47,]),'MAYQUE':([28,31,32,33,36,59,62,63,64,65,],[-17,-14,-15,-16,49,-18,-19,-20,-21,-22,]),'MENQUE':([28,31,32,33,36,59,62,63,64,65,],[-17,-14,-15,-16,50,-18,-19,-20,-21,-22,]),'MAYIGQUE':([28,31,32,33,36,59,62,63,64,65,],[-17,-14,-15,-16,51,-18,-19,-20,-21,-22,]),'MENIGQUE':([28,31,32,33,36,59,62,63,64,65,],[-17,-14,-15,-16,52,-18,-19,-20,-21,-22,]),'DOBLEIG':([28,31,32,33,36,59,62,63,64,65,],[-17,-14,-15,-16,53,-18,-19,-20,-21,-22,]),'NOIG':([28,31,32,33,36,59,62,63,64,65,],[-17,-14,-15,-16,55,-18,-19,-20,-21,-22,]),'NOIGUAL':([28,31,32,33,36,59,62,63,64,65,],[-17,-14,-15,-16,56,-18,-19,-20,-21,-22,]),'PTCOMA':([28,31,32,33,35,42,59,62,63,64,65,66,67,68,69,70,71,72,73,75,76,],[-17,-14,-15,-16,48,60,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,77,78,]),'PUNTO':([28,],[41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,8,]),'insert_insrt':([0,2,],[4,4,]),'update_insrt':([0,2,],[5,5,]),'lista_update':([12,],[16,]),'parametro_update':([12,24,],[17,37,]),'lista_parametros_lista':([13,],[19,]),'lista_datos':([21,40,57,],[29,58,74,]),'expresion':([21,22,23,40,43,44,45,46,47,49,50,51,52,53,54,55,56,57,],[30,34,36,30,61,62,63,64,65,66,67,68,69,70,71,72,73,30,]),'expresion_relacional':([23,],[35,]),}

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
  ('instruccion -> update_insrt','instruccion',1,'p_instruccion_f_update','gramatica_insert.py',378),
  ('insert_insrt -> INSERT INTO ID PAR_A lista_parametros_lista PAR_C VALUES PAR_A lista_datos PAR_C PTCOMA','insert_insrt',11,'p_insert_insrt','gramatica_insert.py',384),
  ('insert_insrt -> INSERT INTO ID PAR_A PAR_C VALUES PAR_A lista_datos PAR_C PTCOMA','insert_insrt',10,'p_opcion_lista_parametros_','gramatica_insert.py',389),
  ('insert_insrt -> INSERT INTO ID VALUES PAR_A lista_datos PAR_C PTCOMA','insert_insrt',8,'p_opcion_lista_parametros_vacios','gramatica_insert.py',393),
  ('lista_parametros_lista -> lista_parametros_lista COMA ID','lista_parametros_lista',3,'p_lista_parametros_lista','gramatica_insert.py',399),
  ('lista_parametros_lista -> ID','lista_parametros_lista',1,'p_lista_parametros','gramatica_insert.py',404),
  ('lista_datos -> lista_datos COMA expresion','lista_datos',3,'p_parametros_lista_datos','gramatica_insert.py',413),
  ('lista_datos -> expresion','lista_datos',1,'p_expresion_lista','gramatica_insert.py',418),
  ('agrupacion_expresion -> PAR_A expresion PAR_C','agrupacion_expresion',3,'p_agrupacion_expresion','gramatica_insert.py',422),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','gramatica_insert.py',427),
  ('expresion -> ENTERO','expresion',1,'p_expresion1','gramatica_insert.py',432),
  ('expresion -> FLOTANTE','expresion',1,'p_expresion1','gramatica_insert.py',433),
  ('expresion -> ID','expresion',1,'p_expresion3','gramatica_insert.py',438),
  ('expresion -> ID PUNTO ID','expresion',3,'p_expresion4','gramatica_insert.py',442),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion','gramatica_insert.py',446),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion','gramatica_insert.py',447),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresion','gramatica_insert.py',448),
  ('expresion -> expresion ASTERISCO expresion','expresion',3,'p_expresion','gramatica_insert.py',449),
  ('expresion_relacional -> expresion MAYQUE expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',457),
  ('expresion_relacional -> expresion MENQUE expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',458),
  ('expresion_relacional -> expresion MAYIGQUE expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',459),
  ('expresion_relacional -> expresion MENIGQUE expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',460),
  ('expresion_relacional -> expresion DOBLEIG expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',461),
  ('expresion_relacional -> expresion IGUAL expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',462),
  ('expresion_relacional -> expresion NOIG expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',463),
  ('expresion_relacional -> expresion NOIGUAL expresion','expresion_relacional',3,'p_expresion_relacional','gramatica_insert.py',464),
  ('update_insrt -> UPDATE ID SET lista_update WHERE expresion_relacional PTCOMA','update_insrt',7,'p_update_insrt','gramatica_insert.py',479),
  ('lista_update -> lista_update COMA parametro_update','lista_update',3,'p_lista_update','gramatica_insert.py',483),
  ('lista_update -> parametro_update','lista_update',1,'p_lista_update_lista','gramatica_insert.py',488),
  ('parametro_update -> ID IGUAL expresion','parametro_update',3,'p_parametro_update','gramatica_insert.py',492),
]