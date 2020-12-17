CREATE DATABASE compiladores2;

CREATE DATABASE lenguajes;

USE compiladores2;

CREATE TABLE tbUSUARIO(
	id_ususario		INTEGER PRIMARY KEY,
	usuario		INTEGER,
	password		INTEGER
);

CREATE TABLE tbCURSO(
	id_curso		INTEGER PRIMARY KEY,
	descripcion		VARCHAR(50)
);

CREATE TABLE tbASIGNACION(
    id_asignacion   INTEGER PRIMARY KEY,
    id_ususario     INTEGER NOT NULL,
    id_curso        INTEGER NOT NULL
);

ALTER DATABASE compiladores2 RENAME TO compi2;

USE compi2;


SHOW TABLES;

DROP DATABASE compi2;