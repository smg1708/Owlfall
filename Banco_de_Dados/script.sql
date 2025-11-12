use owlfall;

create table usuario (
	idUsuario int primary key auto_increment,
	nome varchar(80) not null,
	apelido varchar(45),
	dtNasc date not null,
	email varchar(80) not null unique,
	senha varchar(45) not null
);

create table arma (
	idArma int primary key auto_increment,
	nome varchar(80) not null,
	alcance varchar(45) not null,
	dano int not null,
	descricao varchar(255)
);

create table habilidade (
	idHabilidade int primary key auto_increment,
	nome varchar(80) not null,
	tipo varchar(45) not null,
	tempo varchar(45) not null,
	alcance varchar(45)not null,
	custo int not null,
	restricao varchar(255)not null,
	descricao varchar(255)
);

create table classe (
	idClasse int primary key auto_increment,
	fortificador tinyint,
	emissor tinyint,
	transmutador tinyint,
	conjurador tinyint,
	manipulador tinyint,
	especialista tinyint
);
create table Nen (
	Nen int primary key auto_increment,
	fortificador int,
	emissor int,
	transmutador int,
	conjurador int,
	manipulador int,
	especialista int
);

Create table atributo (
	idAtributo int primary key auto_increment,
	forca int,
	agilidade int,
	vigor int,
	intelecto int,
	presenca int
);


create table pericia (
	idPericia int primary key auto_increment,
	adestramento int,
	artes int,
	atletismoAcrobacia int,
	ciencias int,
	diplomacia int,
	enganacao int,
	fortitude int,
	furtividade int,
	iniciativa int,
	intimidacao int,
	investigacao int,
	luta int,
	medicina int,
	percepcao int,
	pilotagem int,
	pontaria int,
	profissao int,
	reflexos int,
	sobrevivencia int,
	espirito int
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
	Primary key (idFicha, fkUsuario, fkAtributo, fkNen, fkClasse, fkArma, fkHabilidade, fkPericia),
	Constraint fkUsuario
		Foreign key (fkUsuario)
		References usuario(idUsuario),
	Constraint fkAtributo
		Foreign key (fkAtributo)
		References atributo(idAtributo),
	Constraint fkNen
		Foreign key (fkNen)
		References Nen(Nen),
	Constraint fkClasse
		Foreign key (fkClasse)
		References classe(idClasse),
	Constraint fkArma
		Foreign key (fkArma)
		References arma (idArma),
	Constraint fkHabilidade
		Foreign key (fkHabilidade)
		References habilidade (idHabilidade),
	Constraint fkPericia
		Foreign key (fkPericia)
		References pericia (idPericia)
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

