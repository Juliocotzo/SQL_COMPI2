CREATE DATABASE compiladores2;

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
    id_curso        INTEGER NOT NULL,
    CONSTRAINT userr FOREIGN KEY (id_ususario) REFERENCES tbUSUARIO(id_ususario),
    CONSTRAINT cursoo FOREIGN KEY (id_curso) REFERENCES tbCURSO(id_curso)
);

SHOW TABLES;

ALTER TABLE tbUSUARIO ADD COLUMN telefono VARCHAR(50);

SHOW TABLES;
