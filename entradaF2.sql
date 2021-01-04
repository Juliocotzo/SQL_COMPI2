CREATE DATABASE prueba1;
CREATE DATABASE prueba2;
CREATE DATABASE prueba3;
CREATE DATABASE prueba4;
USE prueba1;
SHOW DATABASES;
ALTER DATABASE prueba1 RENAME TO prueba5;
SHOW DATABASES;
ALTER DATABASE prueba4 OWNER TO julio1;
SHOW DATABASES;
ALTER DATABASE prueba4 OWNER TO CURRENT_USER;
SHOW DATABASES;
ALTER DATABASE prueba4 OWNER TO SESSION_USER;
SHOW DATABASES;
ALTER DATABASE prueba4 OWNER TO 'Julio2';
SHOW DATABASES;



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