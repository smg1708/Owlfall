var database = require("../database/config");

// ======================================================
// SALVAR RESULTADO DO QUIZ
// ======================================================
function salvarResultado(idUsuario, idQuiz, pontuacao, personagemEscolhido = null) {

    let instrucao = "";

    if (personagemEscolhido) {
        instrucao = `
            insert into resultadoQuiz (fkUsuario, idQuiz, pontuacao, personagemEscolhido)
            values (${idUsuario}, ${idQuiz}, ${pontuacao}, '${personagemEscolhido}');
        `;
    } else {
        instrucao = `
            insert into resultadoQuiz (fkUsuario, idQuiz, pontuacao)
            values (${idUsuario}, ${idQuiz}, ${pontuacao});
        `;
    }

    return database.executar(instrucao);
}

function obterMedias() {
    var instrucao = `
        select 
            idQuiz,
            avg(pontuacao) as media
        from resultadoQuiz
        where idQuiz = 1
        group by idQuiz;
    `;
    return database.executar(instrucao);
}

function obterTopPersonagem() {
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

function obterTopClasses() {
    var instrucao = `
        select 
            descricao as classe,
            count(*) as quantidade
        from caracteristicas
        where nome = 'classe'
        group by descricao
        order by quantidade desc
    `;
    return database.executar(instrucao);
}

module.exports = {
    salvarResultado,
    obterMedias,
    obterTopPersonagem,
    obterTopClasses
};
