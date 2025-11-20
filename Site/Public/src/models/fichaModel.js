var database = require("../database/config")

// function autenticar(email, senha) {
//     console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function entrar(): ", email, senha)
//     var instrucaoSql = `
//         SELECT idUsuario, nome, email as Login FROM usuario WHERE email = '${email}' and senha = '${senha}';
//     `;
//     console.log("Executando a instrução SQL: \n" + instrucaoSql);
//     return database.executar(instrucaoSql);
// }

// Coloque os mesmos parâmetros aqui. Vá para a var instrucaoSql
function buscarFicha(idFicha) {
    // console.log("ACESSEI OS DADOS MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function cadastrar():", nome, email, senha);
    
    // Insira exatamente a query do banco aqui, lembrando da nomenclatura exata nos valores
    //  e na ordem de inserção dos dados.
    
    var sql = `
        select 
            f.nome,
            f.jogador,
            f.nivel,
            f.vdAtual AS vida,
            f.sanAtual AS sanidade,
            f.nenAtual AS nen,
            c.descricao AS classe,
            c.descricao AS aparencia,
            c.descricao AS personalidade,
            c.descricao AS historia,
            c.descricao AS objetivo,
            c.descricao AS agilidade,
            c.descricao AS forca,
            c.descricao AS intelecto,
            c.descricao AS presenca,
            c.descricao AS vigor
        from ficha f
        
        join caracteristicas c 
            on c.fkFicha = f.idFicha and 

        join caracteristicas c 
            on c.fkFicha = f.idFicha and c.nome = 'aparencia'

        join caracteristicas c 
            on c.fkFicha = f.idFicha and c.nome = 'personalidade'

        join caracteristicas c 
            on c.fkFicha = f.idFicha and c.nome = 'descricao'

        join caracteristicas c 
            on c.fkFicha = f.idFicha and c.nome = 'objetivo'

        join caracteristicas c 
            on c.fkFicha = f.idFicha and c.nome = 'agilidade'

        join caracteristicas c 
            on c.fkFicha = f.idFicha and c.nome = 'forca'

        join caracteristicas c 
            on c.fkFicha = f.idFicha and c.nome = 'intelecto'

        join caracteristicas c 
            on c.fkFicha = f.idFicha and c.nome = 'presenca'

        join caracteristicas c 
            on c.fkFicha = f.idFicha and c.nome = 'vigor'

        WHERE f.idFicha = ${idFicha}
    `;
    
    console.log("Executando a instrução SQL: \n" + sql);
    return database.executar(sql)

}

module.exports = {
    buscarFicha
};