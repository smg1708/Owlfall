-- Arquivo de apoio, caso você queira criar tabelas como as aqui criadas para a API funcionar.
-- Você precisa executar os comandos no banco de dados para criar as tabelas,
-- ter este arquivo aqui não significa que a tabela em seu BD estará como abaixo!

/*
comandos para mysql server
*/

CREATE DATABASE owlfall;

use owlfall;

create table usuario (
	idUsuario int primary key auto_increment,
	nome varchar(80) not null,
	email varchar(80) not null unique,
	senha varchar(45) not null,
	imagem varchar(255)
);

create table ficha (
	idFicha int primary key auto_increment,
	fkUsuario int not null,
	nome varchar(80) not null,
    jogador varchar(80),
	nivel int not null,
	imagem varchar(255),
	vdAtual int,
	vdMax int,
	sanAtual int,
	sanMax int,
	nenAtual int,
	nenMax int,
	constraint fkUsuario
		foreign key (fkUsuario)
		references usuario(idUsuario)
);

create table caracteristicas (
	idCaracteristicas int primary key auto_increment not null,
    fkFicha int not null,
    nome varchar(80),
	tipo varchar(255),
	descricao varchar(255),
	constraint fkFicha
		foreign key (fkFicha)
		references ficha(idFicha)
);

create table campanha (
	idCampanha int primary key auto_increment,
	nome varchar(80) not null,
	descricao varchar(255)
);

create table fichaCampanha (
	fkFichaCampanha int not null,
	fkCampanha int not null,
	primary key (fkFichaCampanha, fkCampanha),
	constraint fkFichaCampanha
		foreign key (fkFichaCampanha)
		references ficha(idFicha),
	constraint fkCampanha
		foreign key (fkCampanha)
		references campanha(idCampanha)
);


