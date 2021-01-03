CREATE DATABASE prueba1;
USE prueba1;
CREATE TABLE usuario(
    id_usuario INTEGER NULL NOT NULL PRIMARY KEY,
    apellido VARCHAR(50) DEFAULT 2.5
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

def p_Ccheck(t):
    ''' C_check : CONSTRAINT ID CHECK PARA expresion_logica PARC '''
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '+ t[5] + ' '+ t[6] + ' '


def p_Ccheck1(t):
    ''' C_check : CHECK PARA expresion_logica PARC'''
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '

def p_cT_options2(t):
    ' cT_options : C_check'
    t[0] = ' '+ t[1] + ' '