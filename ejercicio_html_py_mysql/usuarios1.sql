create database usuarios1;
USE usuarios1;

DROP TABLE usuarios;
CREATE TABLE usuarios (
    name VARCHAR(50) NOT NULL,
    mail VARCHAR(50) NOT NULL,
    passwd VARCHAR(500) NOT NULL
    
);