var database = require("../database/config");

function buscarMediasQuizzes() {
    var instrucao = `
        select 
            idQuiz,
            Round(avg(pontuacao)) as media
        from resultadoQuiz
        where idQuiz = 1
        group by idQuiz;
    `;
    return database.executar(instrucao);
}

function buscarResultadosPersonagem() {
    var instrucao = `
        select 
            personagemEscolhido as personagem,
            count(*) as quantidade
        from resultadoQuiz
        where idQuiz = 2
        group by personagemEscolhido
        order by quantidade desc;
    `;
    return database.executar(instrucao);
}

function buscarResultadosClasse() {
    var instrucao = `
        select 
            descricao as classe,
            count(*) as quantidade
        from caracteristicas
        where nome = 'classe'
        group by descricao
        order by quantidade desc
        limit 1;
    `;
    return database.executar(instrucao);
}

module.exports = {
    buscarMediasQuizzes,
    buscarResultadosPersonagem,
    buscarResultadosClasse
};

