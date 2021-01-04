CREATE DATABASE prueba1;
USE prueba1;
CREATE TABLE usuario(
    id_usuario INTEGER,
    nombre VARCHAR(50),
    apellido VARCHAR(50)
);

CREATE TABLE usuario1(
    id_usuario INTEGER,
    nombre VARCHAR(50),
    apellido VARCHAR(50)
);

CREATE INDEX test1_id_index ON tbUSUARIO (id_usuario);
CREATE INDEX name ON tbUSUARIO USING HASH (id_usuario);
CREATE INDEX test2_mm_idx ON tbUSUARIO (id_usuario, id_usuario);
CREATE INDEX test2_info_nulls_low ON tbUSUARIO (id_usuario NULLS FIRST);
CREATE INDEX test3_desc_index ON tbUSUARIO (id_usuario DESC NULLS LAST);
CREATE UNIQUE INDEX name ON tbUSUARIO (id_usuario , id_usuario, id_usuario);
CREATE INDEX test1_lower_col1_idx ON tbUSUARIO (lower(id_usuario));
CREATE INDEX access_log_client_ip_ix ON tbUSUARIO (id_usuario)
     WHERE NOT (id_usuario > inet  AND
     id_usuario < inet );

CREATE INDEX mytable_cat_1 ON tbUSUARIO (id_usuario) WHERE category = 1;
CREATE INDEX mytable_cat_2 ON tbUSUARIO (id_usuario) WHERE category = 2;
CREATE INDEX mytable_cat_3 ON tbUSUARIO (id_usuario) WHERE category = 3;





CREATE OR REPLACE FUNCTION suma(a integer) RETURNS integer  AS $$
DECLARE
    b integer := 10;
BEGIN
    IF a<20 AND b > 5 THEN
        RAISE a;
        a := a +1;
        SELECT suma(a);
    ELSE 
        RAISE 'ES MAYOR A 20';
    END IF; 
END;
$$ LANGUAGE plpgsql;

SELECT suma(17);

1371

'''def p_expresion31_g(t):
    expresion : select_insrt '''
    #t[0] = ' '+ str(t[1]) + ' '

1308
''' def p_expresion2(t):
     expresion :   AVG PARA expresion PARC 
                     | MAX PARA expresion PARC
                     | MIN PARA expresion PARC             
                     | ALL PARA select_insrt PARC
                     | SOME PARA select_insrt PARCn'''
                     
    #t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

ALTER TABLE usuario ADD COLUMN columna1 BOOLEAN,columna2 INTEGER,columna3 SMALLINT; 
ALTER TABLE usuario ADD COLUMN columna4 MONEY,columna5 DECIMAL (5,2),columna6 NUMERIC (10,2); 
ALTER TABLE usuario ADD COLUMN columna9 BIGINT,columna8 REAL,columna7 DOUBLE PRECISION; 
ALTER TABLE usuario ADD COLUMN columna10 INTERVAL YEAR TO YEAR,columna11 INTERVAL,columna12 TIME; 
ALTER TABLE usuario ADD COLUMN columna15 TIMESTAMP,columna14 DATE,columna13 CHARACTER VARYING (10); 
ALTER TABLE usuario ADD COLUMN columna16 VARCHAR(50),columna18 CHAR(10),columns20 CHARACTER(9); 
ALTER TABLE usuario ADD COLUMN columna17 CHAR(),columna19 CHARACTER(),columna21 SMALLINT; 