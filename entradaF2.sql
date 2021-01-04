CREATE DATABASE prueba1;
USE prueba1;
CREATE TABLE usuario(
    id_usuario INTEGER,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha VARCHAR(50) 
);

INSERT INTO usuario VALUES (1,SUBSTR('julio',0,2),SUBSTRING('cotzo',0,2),NOW());
INSERT INTO usuario (id_usuario,nombre,apellido) VALUES (2,MD5('julio1'),TRIM('             cotzo2'));
INSERT INTO usuario (id_usuario,nombre,apellido) VALUES (3,MD5('julio2'),'             cotzo2');
SELECT id_usuario,nombre FROM usuario;


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