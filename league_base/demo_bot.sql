CREATE DATABASE league_bot;

USE league_bot;

CREATE TABLE personajes(
    id_personaje int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(100) NOT NULL,
    tipo_habilidad varchar (100)NOT NULL,
    preciot float NOT NULL,
    region varchar(100)  NOT NULL,
    rol varchar(100)     NOT NULL,
    sexo varchar(50) NOT NULL);

)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO personajes (nombre, tipo_habilidad, preciot, region, rol, sexo)
VALUES ('Bardo','mana',6300,'Runaterra','Soporte','Hombre'),
('Azir','mana',6300,'Shurima','Mago','Hombre'),
('Draven','mana',4800,'Noxus','Tirador','Hombre'),
('Janna','mana',1350,'Zaun','Soporte','Mujer'),
('Zed','energia',6800,'Jonia','Asesino','Hombre');






SHOW TABLES;

SELECT * FROM personajes;

DESCRIBE personajes;

CREATE USER 'ahp'@'localhost' IDENTIFIED BY 'ahp.2019';
GRANT ALL PRIVILEGES ON league_bot.* TO 'ahp'@'localhost';
FLUSH PRIVILEGES;

