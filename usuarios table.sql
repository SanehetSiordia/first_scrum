DROP DATABASE usuarioscrud;
CREATE DATABASE usuarioscrud;
USE usuariosCRUD;

CREATE TABLE persona(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(50) NOT NULL,
	primer_apellido VARCHAR(50) NOT NULL,
	segundo_apellido VARCHAR(50) NOT NULL,
    fecha date NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE domicilio(
	persona_id INT NOT NULL,
	ciudad VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL,
	FOREIGN KEY(persona_id) REFERENCES persona(id)
);

CREATE TABLE telefono(
	persona_id INT NOT NULL,
	numero BIGINT,
	FOREIGN KEY(persona_id) REFERENCES persona(id)
);

INSERT INTO persona (nombre, primer_apellido,segundo_apellido,fecha) VALUES ('Sinhue', 'Siordia','Millan',(STR_TO_DATE("25/04/92","%d/%m/%y"))), ('Sinhue', 'siordia','millan',(STR_TO_DATE("25/04/92","%d/%m/%y"))); 
INSERT INTO domicilio (persona_id,ciudad, estado) VALUES (1,'Culiacan', 'Sinaloa'),(2,'Mazatlan','Sinaloa'); 
INSERT INTO telefono (persona_id,numero) VALUES (1,6671302628),(2,6677170047); 