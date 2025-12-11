var database = require("../database/config")

function criarFicha(dados, idUsuario) {

    console.log("Dados enviados para criarFicha:", dados);
    var sqlFicha = `
    INSERT INTO ficha (fkUsuario, nome, jogador, nivel, vdAtual, vdMax, sanAtual, sanMax, nenAtual, nenMax ) VALUES 
        (${idUsuario}, '${dados[0].nome}', '${dados[0].jogador}', '1','${dados[0].statusMax.vida}','${dados[0].statusMax.vida}','${dados[0].statusMax.sanidade}','${dados[0].statusMax.sanidade}','${dados[0].statusMax.nen}','${dados[0].statusMax.nen}');
    `;
    
    console.log("Executando a instrução SQL: \n" + sqlFicha);
    return database.executar(sqlFicha)
        .then(resultado => {
            var idFicha = resultado.insertId;

            var sqlCarac = `
                INSERT INTO caracteristicas (fkFicha, nome, tipo, descricao) VALUES 
                ('${idFicha}', 'classe', 'classe', "${dados[0].classe}"),
                ('${idFicha}', 'aparencia', 'texto', "${dados[0].aparencia}"),
                ('${idFicha}', 'personalidade', 'texto', "${dados[0].personalidade}"),
                ('${idFicha}', 'descricao', 'texto', "${dados[0].descricao}"),
                ('${idFicha}', 'objetivo', 'texto', "${dados[0].objetivo}"),
                ('${idFicha}', 'agilidade', 'atributo', "${dados[0].atributos[0]}"),
                ('${idFicha}', 'forca', 'atributo', "${dados[0].atributos[1]}"),
                ('${idFicha}', 'intelecto', 'atributo', "${dados[0].atributos[2]}"),
                ('${idFicha}', 'presenca', 'atributo', "${dados[0].atributos[3]}"),
                ('${idFicha}', 'vigor', 'atributo', "${dados[0].atributos[4]}"),
                ('${idFicha}', 'adestramento', 'pericia', "${dados[0].pericias[0].adestramento}"),
                ('${idFicha}', 'artes', 'pericia', "${dados[0].pericias[0].artes}"),
                ('${idFicha}', 'acrob_atlet', 'pericia', "${dados[0].pericias[0].acrob_atlet}"),
                ('${idFicha}', 'ciencias', 'pericia', "${dados[0].pericias[0].ciencias}"),
                ('${idFicha}', 'diplomacia', 'pericia', "${dados[0].pericias[0].diplomacia}"),
                ('${idFicha}', 'enganacao', 'pericia', "${dados[0].pericias[0].enganacao}"),
                ('${idFicha}', 'fortitude', 'pericia', "${dados[0].pericias[0].fortitude}"),
                ('${idFicha}', 'furtividade', 'pericia', "${dados[0].pericias[0].furtividade}"),
                ('${idFicha}', 'iniciativa', 'pericia', "${dados[0].pericias[0].iniciativa}"),
                ('${idFicha}', 'intimidacao', 'pericia', "${dados[0].pericias[0].intimidacao}"),
                ('${idFicha}', 'investigacao', 'pericia', "${dados[0].pericias[0].investigacao}"),
                ('${idFicha}', 'luta', 'pericia', "${dados[0].pericias[0].luta}"),
                ('${idFicha}', 'medicina', 'pericia', "${dados[0].pericias[0].medicina}"),
                ('${idFicha}', 'percepcao', 'pericia', "${dados[0].pericias[0].percepcao}"),
                ('${idFicha}', 'pilotagem', 'pericia', "${dados[0].pericias[0].pilotagem}"),
                ('${idFicha}', 'pontaria', 'pericia', "${dados[0].pericias[0].pontaria}"),
                ('${idFicha}', 'profissao', 'pericia', "${dados[0].pericias[0].profissao}"),
                ('${idFicha}', 'reflexos', 'pericia', "${dados[0].pericias[0].reflexos}"),
                ('${idFicha}', 'sobrevivencia', 'pericia', "${dados[0].pericias[0].sobrevivencia}"),
                ('${idFicha}', 'espirito', 'pericia', "${dados[0].pericias[0].espirito}");
            `;
            console.log("Executando a instrução SQL: \n" + sqlCarac);
            return database.executar(sqlCarac)
                .then(() => {
                    return {idFicha: idFicha};
                });
        });
}

module.exports = {
    criarFicha
};