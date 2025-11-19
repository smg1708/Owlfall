var database = require("../database/config")

// function autenticar(email, senha) {
//     console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function entrar(): ", email, senha)
//     var instrucaoSql = `
//         SELECT idUsuario, nome, email as Login FROM usuario WHERE email = '${email}' AND senha = '${senha}';
//     `;
//     console.log("Executando a instrução SQL: \n" + instrucaoSql);
//     return database.executar(instrucaoSql);
// }

// Coloque os mesmos parâmetros aqui. Vá para a var instrucaoSql
function criarFicha(dados) {
    // console.log("ACESSEI OS DADOS MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function cadastrar():", nome, email, senha);
    
    // Insira exatamente a query do banco aqui, lembrando da nomenclatura exata nos valores
    //  e na ordem de inserção dos dados.
    
    var sqlFicha = `
    INSERT INTO ficha (fkUsuario, nome, jogador, nivel, vdAtual, vdMax, sanAtual, sanMax, nenAtual, nenMax ) VALUES 
        ('1', '${dados[0].nome}', '${dados[0].jogador}', '1','${dados[0].statusMax.vida}','${dados[0].statusMax.vida}','${dados[0].statusMax.sanidade}','${dados[0].statusMax.sanidade}','${dados[0].statusMax.nen}','${dados[0].statusMax.nen}');
    `;
    
    console.log("Executando a instrução SQL: \n" + sqlFicha);
    return database.executar(sqlFicha)
        .then(resultado => {
            var idFicha = resultado.insertId;
            // console.log("ACESSEI OS DADOS MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function cadastrar():", nome, email, senha);


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
                ('${idFicha}', 'vigor', 'atributo', "${dados[0].atributos[4]}");
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