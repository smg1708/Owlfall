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
    nome varchar(80) not null,
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

INSERT INTO quiz (nome, tipo, descricao) VALUES 
	('Quiz de Pontos', 'conhecimento', 'Você sabe sobre HXH'),
	('Quiz de Personagem', 'personalidade', 'Quem voce seria em hxh');

INSERT INTO questao (fkQuiz, pergunta, alternativaA, alternativaB, alternativaC, alternativaD, alternativaCorreta) VALUES
	(1, "Quem é o pai de Killua?", "Ging", "Silva", "Kite", "Leorio", "alternativaB"),
	(1, "Quem lidera a Trupe Fantasma (Phantom Troupe)?", "Hisoka", "Chrollo Lucilfer", "Feitan", "Machi", "alternativaB"),
	(1, "Qual das seguintes habilidades é usada por Hisoka?", "Godspeed", "Jajanken", "Chain Jail", "Bungee Gum", "alternativaD"),
	(1, "Quem derrota Pitou durante o arco das Formigas Quimera?", "Gon", "Netero", "Killua", "Pouf", "alternativaA"),
	(1, "Quem é o mestre de batalha de Gon e Killua em Heaven’s Arena?", "Biscuit", "Kite", "Wing", "Knuckle", "alternativaC"),
	(1, "Quem é o único membro da Trupe Fantasma que não usa Nen ofensivamente?", "Chrollo", "Shalnark", "Pakunoda", "Machi", "alternativaC"),
	(1, "Qual é o maior ponto fraco de Meruem após o arco da Chimera Ant?", "Ele se torna vulnerável emocionalmente por Komugi", "Sua aura diminui drasticamente após absorver inimigos", "Perde a habilidade de voar", "Não consegue usar Nen ofensivo", "alternativaA"),
	(1, "Quem tentou envenenar Leorio e seus amigos no exame dos caçadores?", "Ponzu", "Wing", "Ging", "Tompa", "alternativaD"),
	(1, "Qual membro da aranha é da família Zoldyck?", "Illumi", "Kalluto", "Killua", "Milluki", "alternativaD"),
	(1, "Em que ano foi lançado o ultimo episodio do anime atualmente de hxh?", "2025", "2014", "2009", "2019", "alternativaB");
    
INSERT INTO questao (fkQuiz, pergunta, alternativaA, alternativaB, alternativaC, alternativaD, valorA, valorB, valorC, valorD) VALUES
	(2, "Qual rota você segue?", "A Floresta das Feras", "O Vale das Sombras", "O Caminho das Luzes", "A Estrada da Ruína", "Gon_Freecss", "Killua_Zoldyck", "Leorio", "Kurapika"),
	(2, "Você veio aqui atrás de que?", "Quero desafiar meus limites.", "Quero liberdade. Coisas que só a força pode oferecer", "Quero um futuro melhor para mim e para os outros.", "Quero respostas. Quero justiça.", "Gon_Freecss", "Killua_Zoldyck", "Leorio", "Kurapika"),
	(2, "Como você reage?", "Parte pra cima com impulsividade e coragem.", "Analisa o movimento, se esquiva e procura um contra-ataque certeiro", "Tenta dialogar primeiro, e luta apenas se necessário.", "Assume uma postura defensiva e espera o momento perfeito.", "Gon_Freecss", "Killua_Zoldyck", "Leorio", "Kurapika"),
	(2, "O que torna uma pessoa verdadeiramente forte?", "A vontade de seguir em frente, não importa o quê.", "A capacidade de tomar decisões difíceis.", "O desejo de proteger os outros.", "A determinação de nunca trair seu ideal.", "Gon_Freecss", "Killua_Zoldyck", "Leorio", "Kurapika"),
	(2, "Quem você escolhe?", "Salva o inocente sem hesitar", "Salva o ladrão todos merecem uma chance.", "Ignora os dois e segue em frente foco é tudo.", "Salva quem vai te dar mais respostas.", "Leorio", "Gon_Freecss", "Killua_Zoldyck", "Kurapika"),
	(2, "Se você dominasse o Nen hoje… Qual seria o motivo?", "Buscar aventuras e novos horizontes.", "Ser forte o suficiente para nunca depender de ninguém", "Ajudar pessoas e mudar o mundo.", "Fazer justiça mesmo que custe caro.", "Gon_Freecss", "Killua_Zoldyck", "Leorio", "Kurapika");
    
select * from caracteristicas;


create view vw_carregarFicha as
	select 
		f.idFicha,
		f.nome,
		f.jogador,
		f.imagem, 
		f.nivel,
		f.vdAtual as vida,
		f.sanAtual as sanidade,
		f.nenAtual as nen,

		cClasse.descricao as classe,
		cAparencia.descricao as aparencia,
		cPersonalidade.descricao as personalidade,
		cHistoria.descricao as historia,
		cObjetivo.descricao as objetivo,

		cAgi.descricao as agilidade,
		cFor.descricao as forca,
		cInt.descricao as intelecto,
		cPre.descricao as presenca,
		cVig.descricao as vigor,

		cAdestramento.descricao as adestramento,
		cArtes.descricao as artes,
		cAcrobAtlet.descricao as acrob_atletismo,
		cCiencias.descricao as ciencias,
		cDiplomacia.descricao as diplomacia,
		cEnganacao.descricao as enganacao,
		cFortitude.descricao as fortitude,
		cFurtividade.descricao as furtividade,
		cIniciativa.descricao as iniciativa,
		cIntimidacao.descricao as intimidacao,
		cInvestigacao.descricao as investigacao,
		cLuta.descricao as luta,
		cMedicina.descricao as medicina,
		cPercepcao.descricao as percepcao,
		cPilotagem.descricao as pilotagem,
		cPontaria.descricao as pontaria,
		cProfissao.descricao as profissao,
		cReflexos.descricao as reflexos,
		cSobrevivencia.descricao as sobrevivencia,
		cEspirito.descricao as espirito

	from ficha f

		left join caracteristicas cClasse on cClasse.fkFicha = f.idFicha and cClasse.nome = 'classe'
		left join caracteristicas cAparencia on cAparencia.fkFicha = f.idFicha and cAparencia.nome = 'aparencia'
		left join caracteristicas cPersonalidade on cPersonalidade.fkFicha = f.idFicha and cPersonalidade.nome = 'personalidade'
		left join caracteristicas cHistoria on cHistoria.fkFicha = f.idFicha and cHistoria.nome = 'descricao'
		left join caracteristicas cObjetivo on cObjetivo.fkFicha = f.idFicha and cObjetivo.nome = 'objetivo'

		left join caracteristicas cAgi on cAgi.fkFicha = f.idFicha and cAgi.nome = 'agilidade'
		left join caracteristicas cFor on cFor.fkFicha = f.idFicha and cFor.nome = 'forca'
		left join caracteristicas cInt on cInt.fkFicha = f.idFicha and cInt.nome = 'intelecto'
		left join caracteristicas cPre on cPre.fkFicha = f.idFicha and cPre.nome = 'presenca'
		left join caracteristicas cVig on cVig.fkFicha = f.idFicha and cVig.nome = 'vigor'

		left join caracteristicas cAdestramento on cAdestramento.fkFicha = f.idFicha and cAdestramento.nome = 'adestramento'
		left join caracteristicas cArtes on cArtes.fkFicha = f.idFicha and cArtes.nome = 'artes'
		left join caracteristicas cAcrobAtlet on cAcrobAtlet.fkFicha = f.idFicha and cAcrobAtlet.nome = 'acrob_atletismo'
		left join caracteristicas cCiencias on cCiencias.fkFicha = f.idFicha and cCiencias.nome = 'ciencias'
		left join caracteristicas cDiplomacia on cDiplomacia.fkFicha = f.idFicha and cDiplomacia.nome = 'diplomacia'
		left join caracteristicas cEnganacao on cEnganacao.fkFicha = f.idFicha and cEnganacao.nome = 'enganacao'
		left join caracteristicas cFortitude on cFortitude.fkFicha = f.idFicha and cFortitude.nome = 'fortitude'
		left join caracteristicas cFurtividade on cFurtividade.fkFicha = f.idFicha and cFurtividade.nome = 'furtividade'
		left join caracteristicas cIniciativa on cIniciativa.fkFicha = f.idFicha and cIniciativa.nome = 'iniciativa'
		left join caracteristicas cIntimidacao on cIntimidacao.fkFicha = f.idFicha and cIntimidacao.nome = 'intimidacao'
		left join caracteristicas cInvestigacao on cInvestigacao.fkFicha = f.idFicha and cInvestigacao.nome = 'investigacao'
		left join caracteristicas cLuta on cLuta.fkFicha = f.idFicha and cLuta.nome = 'luta'
		left join caracteristicas cMedicina on cMedicina.fkFicha = f.idFicha and cMedicina.nome = 'medicina'
		left join caracteristicas cPercepcao on cPercepcao.fkFicha = f.idFicha and cPercepcao.nome = 'percepcao'
		left join caracteristicas cPilotagem on cPilotagem.fkFicha = f.idFicha and cPilotagem.nome = 'pilotagem'
		left join caracteristicas cPontaria on cPontaria.fkFicha = f.idFicha and cPontaria.nome = 'pontaria'
		left join caracteristicas cProfissao on cProfissao.fkFicha = f.idFicha and cProfissao.nome = 'profissao'
		left join caracteristicas cReflexos on cReflexos.fkFicha = f.idFicha and cReflexos.nome = 'reflexos'
		left join caracteristicas cSobrevivencia on cSobrevivencia.fkFicha = f.idFicha and cSobrevivencia.nome = 'sobrevivencia'
		left join caracteristicas cEspirito on cEspirito.fkFicha = f.idFicha and cEspirito.nome = 'espirito';
        
create view vw_selectFicha as
	select 
		f.idFicha,
		f.nome,
		f.imagem,
		f.fkUsuario,
		cClasse.descricao as classe

	from ficha f join caracteristicas cClasse
		   on cClasse.fkFicha = f.idFicha
		  and cClasse.nome = 'classe';
        
select * from vw_carregarFicha
	where idFicha = 1;

select * from vw_selectFicha;

select * from caracteristicas;

select * from resultadoQuiz;

select * from questao