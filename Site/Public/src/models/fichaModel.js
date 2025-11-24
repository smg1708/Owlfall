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
        UPDATE caracteristicas SET descricao = CASE nome
            WHEN 'classe' THEN '${dados.classe}'

            WHEN 'aparencia' THEN '${dados.aparencia}'
            WHEN 'personalidade' THEN '${dados.personalidade}'
            WHEN 'descricao' THEN '${dados.descricao}'
            WHEN 'objetivo' THEN '${dados.objetivo}'

            WHEN 'agilidade' THEN '${dados.agilidade}'
            WHEN 'forca' THEN '${dados.forca}'
            WHEN 'intelecto' THEN '${dados.intelecto}'
            WHEN 'presenca' THEN '${dados.presenca}'
            WHEN 'vigor' THEN '${dados.vigor}'

            WHEN 'adestramento' THEN '${dados.adestramento}'
            WHEN 'artes' THEN '${dados.artes}'
            WHEN 'acrob_atletismo' THEN '${dados.acrob_atlet}'
            WHEN 'ciencias' THEN '${dados.ciencias}'
            WHEN 'diplomacia' THEN '${dados.diplomacia}'

            WHEN 'enganacao' THEN '${dados.enganacao}'
            WHEN 'fortitude' THEN '${dados.fortitude}'
            WHEN 'furtividade' THEN '${dados.furtividade}'
            WHEN 'iniciativa' THEN '${dados.iniciativa}'
            WHEN 'intimidacao' THEN '${dados.intimidacao}'

            WHEN 'investigacao' THEN '${dados.investigacao}'
            WHEN 'luta' THEN '${dados.luta}'
            WHEN 'medicina' THEN '${dados.medicina}'
            WHEN 'percepcao' THEN '${dados.percepcao}'
            WHEN 'pilotagem' THEN '${dados.pilotagem}'

            WHEN 'pontaria' THEN '${dados.pontaria}'
            WHEN 'profissao' THEN '${dados.profissao}'
            WHEN 'reflexos' THEN '${dados.reflexos}'
            WHEN 'sobrevivencia' THEN '${dados.sobrevivencia}'
            WHEN 'espirito' THEN '${dados.espirito}'

            else descricao
        END
        WHERE fkFicha = ${dados.idFicha};
        `;

    var sql = sqlCaracs + sqlFicha

  return database.executar(sql);
}

function buscarFicha(idFicha) {
    
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