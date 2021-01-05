CREATE DATABASE DBFase2;

USE DBFase2;

CREATE FUNCTION myFuncion(texto text) RETURNS text AS $$
BEGIN
	RAISE texto;
END;
$$ LANGUAGE plpgsql;

select myFuncion('INICIO CALIFICACION FASE 2');

CREATE TABLE tbProducto (idproducto integer not null primary key,
  						 producto varchar(150) not null,
  						 fechacreacion date not null,
						 estado integer);

CREATE UNIQUE INDEX idx_producto ON tbProducto (idproducto);

CREATE TABLE tbCalificacion (idcalifica integer not null primary key,
							 item varchar(100) not null,
							 punteo integer not null);

CREATE UNIQUE INDEX idx_califica ON tbCalificacion (idcalifica);
						 
INSERT INTO tbProducto values(1,'Laptop Lenovo',now(),1);
INSERT INTO tbProducto values(2,'Bateria para Laptop Lenovo T420',now(),1);
INSERT INTO tbProducto values(3,'Teclado Inalambrico',now(),1);
INSERT INTO tbProducto values(4,'Mouse Inalambrico',now(),1);
INSERT INTO tbProducto values(5,'WIFI USB',now(),1);
INSERT INTO tbProducto values(6,'Laptop HP',now(),1);
INSERT INTO tbProducto values(7,'Teclado Flexible USB',now(),1);
INSERT INTO tbProducto values(8,'Laptop Samsung','2021-01-02',1);

	 

CREATE FUNCTION ValidaRegistros(tabla varchar(50),cantidad integer) RETURNS integer AS $$
DECLARE resultado INTEGER; 
		retorna   INTEGER;
BEGIN
	if tabla == 'tbProducto' then
	    resultado := 2;
    	if cantidad == resultado then
			retorna := 1;
		else 
			retorna := 0;
		end if;
	end if;
	if tabla == 'tbProductoUp' then
	    resultado := 2;
    	if cantidad == resultado then
			retorna := 1;
		else 
			retorna := 0;
		end if;
	end if;
	if tabla == 'tbbodega' then
	    resultado := 2;
    	if cantidad == resultado then
			retorna := 1;
		else 
			retorna := 0;
		end if;
	end if;
RAISE retorna;
END;
$$ LANGUAGE plpgsql;

SELECT ValidaRegistros('tbProducto',8);
insert into tbCalificacion values(1,'Create Table and Insert',2);

--update tbProducto set estado = 2 where estado = 1;
SELECT ValidaRegistros('tbProductoUp',8);
insert into tbCalificacion values(2,'Update',2);

CREATE FUNCTION CALCULOS() RETURNS integer AS $$
DECLARE hora integer;
DECLARE SENO DECIMAL;
DECLARE VALOR INTEGER;
DECLARE ABSOLUTO DECIMAL;
BEGIN
	hora := 2;	
	SENO := 3;
	VALOR := 4;	
	VALOR := VALOR + 2;					
	ABSOLUTO := 3;	
	ABSOLUTO := 4;
	VALOR := (VALOR + ABSOLUTO)/2;
	IF VALOR > 1 THEN
		VALOR := 20;
	ELSE
		VALOR := 10;
	END IF;
RAISE VALOR;
END;
$$ LANGUAGE plpgsql;

SELECT CALCULOS();
insert into tbCalificacion values(3,' Valida Funciones',2);

create table tbbodega (idbodega integer not null primary key,
					   bodega varchar(100) not null,
					   estado integer);
								  
CREATE INDEX tbbodegaIndex ON tbbodega (lower(bodega));

create procedure sp_validainsert()
language plpgsql
as $$
begin
	insert into tbbodega values(1,'BODEGA CENTRAL',1);
	insert into tbbodega (idbodega,bodega) values(2,'BODEGA ZONA 12');
	insert into tbbodega (idbodega,bodega,estado) values(3,'BODEGA ZONA 11',1);
	insert into tbbodega (idbodega,bodega,estado) values(4,'BODEGA ZONA 1',1);
	insert into tbbodega (idbodega,bodega,estado) values(5,'BODEGA ZONA 10',1);
	RAISE 'INSERT';
end; $$
								 
EXECUTE sp_validainsert();

SELECT ValidaRegistros('tbbodega',5);		 
insert into tbCalificacion values(4,'Valida Store Procedure',5);
																			  

create procedure sp_validaupdate()
language plpgsql
as $$
begin
	RAISE 'UPDATE';
	--update tbbodega set bodega = 'bodega zona 9' where idbodega = 4; 
end; $$

EXECUTE sp_validaupdate();

--delete from tbbodega where idbodega = 4;
SELECT ValidaRegistros('tbbodega',4);
insert into tbCalificacion values(5,'Valida Delete',2);
select * from tbbodega;
