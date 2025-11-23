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
	Constraint fkUsuario
		Foreign key (fkUsuario)
		References usuario(idUsuario)
);

create table caracteristicas (
	idCaracteristicas int primary key auto_increment not null,
    fkFicha int not null,
    nome varchar(80),
	tipo varchar(255),
	descricao varchar(255),
	Constraint fkFicha
		Foreign key (fkFicha)
		References ficha(idFicha)
);

create table campanha (
	idCampanha int primary key auto_increment,
	nome varchar(80) not null,
	descricao varchar(255)
);

create table fichaCampanha (
	fkFichaCampanha int not null,
	fkCampanha int not null,
	Primary key (fkFichaCampanha, fkCampanha),
	Constraint fkFichaCampanha
		Foreign key (fkFichaCampanha)
		References ficha(idFicha),
	Constraint fkCampanha
		Foreign key (fkCampanha)
		References campanha(idCampanha)
);

create table quiz (
    idQuiz int primary key auto_increment,
    nome varchar(100) not null,
    tipo varchar(45) not null
        constraint ckTipo check(tipo in ('conhecimento','personalidade')),
    descricao varchar(255)
);

create table resultadoQuiz (
    idResultado int primary key auto_increment,
    fkUsuario int not null,
    idQuiz int not null,
    pontuacao int,
    personagemEscolhido varchar(80),
    dataHora datetime default current_timestamp,
    constraint fkResultadoUsuario foreign key (fkUsuario) references usuario(idUsuario),
    constraint fkResultadoQuiz foreign key (idQuiz) references quiz(idQuiz)
);

create table questao (
    idQuestao int primary key auto_increment,
    fkQuiz int not null,
    pergunta varchar(255),
    alternativaA varchar(255),
    alternativaB varchar(255),
    alternativaC varchar(255),
    alternativaD varchar(255),
    alternativaCorreta varchar(45),
    valorA varchar(50),
    valorB varchar(50),
    valorC varchar(50),
    valorD varchar(50),
    constraint fkQuestaoQuiz foreign key (fkQuiz) references quiz(idQuiz)
);


