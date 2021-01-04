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