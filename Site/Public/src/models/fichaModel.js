var database = require("../database/config")

function salvarImagem(idFicha ,imagem) {
  const instrucao = `
    update ficha SET imagem = '${imagem}'
        where idFicha = ${idFicha};
        `;

  return database.executar(instrucao);
}

function atualizarFicha(dados) {

    var sqlFicha = `
        UPDATE ficha SET
            nome = '${dados.nome}',
            jogador = '${dados.jogador}',
            nivel = ${dados.nivel},
            vdAtual = ${dados.vida},
            sanAtual = ${dados.sanidade},
            nenAtual = ${dados.nen}
        WHERE idFicha = ${dados.idFicha};
    `;

    var sqlCaracs = `
        UPDATE caracteristicas SET descricao = '${dados.aparencia}' WHERE fkFicha = ${dados.idFicha} AND nome = 'aparencia';
        UPDATE caracteristicas SET descricao = '${dados.personalidade}' WHERE fkFicha = ${dados.idFicha} AND nome = 'personalidade';
        UPDATE caracteristicas SET descricao = '${dados.historia}' WHERE fkFicha = ${dados.idFicha} AND nome = 'descricao';
        UPDATE caracteristicas SET descricao = '${dados.objetivo}' WHERE fkFicha = ${dados.idFicha} AND nome = 'objetivo';

        UPDATE caracteristicas SET descricao = '${dados.agilidade}' WHERE fkFicha = ${dados.idFicha} AND nome = 'agilidade';
        UPDATE caracteristicas SET descricao = '${dados.forca}' WHERE fkFicha = ${dados.idFicha} AND nome = 'forca';
        UPDATE caracteristicas SET descricao = '${dados.intelecto}' WHERE fkFicha = ${dados.idFicha} AND nome = 'intelecto';
        UPDATE caracteristicas SET descricao = '${dados.presenca}' WHERE fkFicha = ${dados.idFicha} AND nome = 'presenca';
        UPDATE caracteristicas SET descricao = '${dados.vigor}' WHERE fkFicha = ${dados.idFicha} AND nome = 'vigor';

        UPDATE caracteristicas SET descricao = '${dados.adestramento}' WHERE fkFicha = ${dados.idFicha} AND nome = 'adestramento';
        UPDATE caracteristicas SET descricao = '${dados.artes}' WHERE fkFicha = ${dados.idFicha} AND nome = 'artes';
        UPDATE caracteristicas SET descricao = '${dados.acrob_atlet}' WHERE fkFicha = ${dados.idFicha} AND nome = 'acrob_atlet';
        UPDATE caracteristicas SET descricao = '${dados.ciencias}' WHERE fkFicha = ${dados.idFicha} AND nome = 'ciencias';
        UPDATE caracteristicas SET descricao = '${dados.diplomacia}' WHERE fkFicha = ${dados.idFicha} AND nome = 'diplomacia';
        UPDATE caracteristicas SET descricao = '${dados.enganacao}' WHERE fkFicha = ${dados.idFicha} AND nome = 'enganacao';
        UPDATE caracteristicas SET descricao = '${dados.fortitude}' WHERE fkFicha = ${dados.idFicha} AND nome = 'fortitude';
        UPDATE caracteristicas SET descricao = '${dados.furtividade}' WHERE fkFicha = ${dados.idFicha} AND nome = 'furtividade';
        UPDATE caracteristicas SET descricao = '${dados.iniciativa}' WHERE fkFicha = ${dados.idFicha} AND nome = 'iniciativa';
        UPDATE caracteristicas SET descricao = '${dados.intimidacao}' WHERE fkFicha = ${dados.idFicha} AND nome = 'intimidacao';
        UPDATE caracteristicas SET descricao = '${dados.investigacao}' WHERE fkFicha = ${dados.idFicha} AND nome = 'investigacao';
        UPDATE caracteristicas SET descricao = '${dados.luta}' WHERE fkFicha = ${dados.idFicha} AND nome = 'luta';
        UPDATE caracteristicas SET descricao = '${dados.medicina}' WHERE fkFicha = ${dados.idFicha} AND nome = 'medicina';
        UPDATE caracteristicas SET descricao = '${dados.percepcao}' WHERE fkFicha = ${dados.idFicha} AND nome = 'percepcao';
        UPDATE caracteristicas SET descricao = '${dados.pilotagem}' WHERE fkFicha = ${dados.idFicha} AND nome = 'pilotagem';
        UPDATE caracteristicas SET descricao = '${dados.pontaria}' WHERE fkFicha = ${dados.idFicha} AND nome = 'pontaria';
        UPDATE caracteristicas SET descricao = '${dados.profissao}' WHERE fkFicha = ${dados.idFicha} AND nome = 'profissao';
        UPDATE caracteristicas SET descricao = '${dados.reflexos}' WHERE fkFicha = ${dados.idFicha} AND nome = 'reflexos';
        UPDATE caracteristicas SET descricao = '${dados.sobrevivencia}' WHERE fkFicha = ${dados.idFicha} AND nome = 'sobrevivencia';
        UPDATE caracteristicas SET descricao = '${dados.espirito}' WHERE fkFicha = ${dados.idFicha} AND nome = 'espirito';
    `;

    var sql = sqlCaracs + sqlFicha

  return database.executar(sql);
}

// Coloque os mesmos parâmetros aqui. Vá para a var instrucaoSql
function buscarFicha(idFicha) {
    // console.log("ACESSEI OS DADOS MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function cadastrar():", nome, email, senha);
    
    // Insira exatamente a query do banco aqui, lembrando da nomenclatura exata nos valores
    //  e na ordem de inserção dos dados.
    
    var sql = `
        select * from vw_carregarFicha
            where idFicha = ${idFicha};
    `;
    
    console.log("Executando a instrução SQL: \n" + sql);
    return database.executar(sql)

}

module.exports = {
    buscarFicha,
    salvarImagem,
    atualizarFicha
};