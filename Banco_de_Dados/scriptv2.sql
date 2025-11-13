use owlfall;

create table usuario (
	idUsuario int primary key auto_increment,
	nome varchar(80) not null,
	apelido varchar(45),
	dtNasc date not null,
	email varchar(80) not null unique,
	senha varchar(45) not null
);

create table ficha (
	idFicha int auto_increment,
	fkUsuario int,
	fkAtributo int,
	fkNen int,
	fkClasse int,
	fkArma int,
	fkHabilidade int,
	fkPericia int,
	nome varchar(80),
	nivel int,
	vdAtual int,
	vdMax int,
	sanAtual int,
	sanMax int,
	nenAtual int,
	nenMax int,
	Primary key (idFicha, fkUsuario),
	Constraint fkUsuario
		Foreign key (fkUsuario)
		References usuario(idUsuario)
);

create table caracteristicas (
	idCampanha int,
    idFicha int,
    nome varchar(80),
	tipo varchar(255),
	descricao varchar(255)
);

create table campanha (
	idCampanha int primary key auto_increment,
	nome varchar(80),
	descricao varchar(255)
);

create table fichaCampanha (
	fkFicha int,
	fkCampanha int,
	Primary key (fkFicha, fkCampanha),
	Constraint fkFicha
		Foreign key (fkFicha)
		References ficha (idFicha),
	Constraint fkCampanha
		Foreign key (fkCampanha)
		References campanha(idCampanha)
);

