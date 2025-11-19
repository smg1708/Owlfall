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
function buscarFicha(idFicha) {
    // console.log("ACESSEI OS DADOS MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function cadastrar():", nome, email, senha);
    
    // Insira exatamente a query do banco aqui, lembrando da nomenclatura exata nos valores
    //  e na ordem de inserção dos dados.
    
    var sql = `
        SELECT 
            f.nome,
            f.jogador,
            f.nivel,
            f.vdAtual AS vida,
            f.sanAtual AS sanidade,
            f.nenAtual AS nen,
            c_classe.descricao AS classe,
            c_aparencia.descricao AS aparencia,
            c_personalidade.descricao AS personalidade,
            c_descricao.descricao AS historia,
            c_objetivo.descricao AS objetivo,
            c_agilidade.descricao AS agilidade,
            c_forca.descricao AS forca,
            c_intelecto.descricao AS intelecto,
            c_presenca.descricao AS presenca,
            c_vigor.descricao AS vigor
        FROM ficha f
        
        JOIN caracteristicas c_classe 
            ON c_classe.fkFicha = f.idFicha AND c_classe.nome = 'classe'

        JOIN caracteristicas c_aparencia 
            ON c_aparencia.fkFicha = f.idFicha AND c_aparencia.nome = 'aparencia'

        JOIN caracteristicas c_personalidade 
            ON c_personalidade.fkFicha = f.idFicha AND c_personalidade.nome = 'personalidade'

        JOIN caracteristicas c_descricao 
            ON c_descricao.fkFicha = f.idFicha AND c_descricao.nome = 'descricao'

        JOIN caracteristicas c_objetivo 
            ON c_objetivo.fkFicha = f.idFicha AND c_objetivo.nome = 'objetivo'

        JOIN caracteristicas c_agilidade 
            ON c_agilidade.fkFicha = f.idFicha AND c_agilidade.nome = 'agilidade'

        JOIN caracteristicas c_forca 
            ON c_forca.fkFicha = f.idFicha AND c_forca.nome = 'forca'

        JOIN caracteristicas c_intelecto 
            ON c_intelecto.fkFicha = f.idFicha AND c_intelecto.nome = 'intelecto'

        JOIN caracteristicas c_presenca 
            ON c_presenca.fkFicha = f.idFicha AND c_presenca.nome = 'presenca'

        JOIN caracteristicas c_vigor 
            ON c_vigor.fkFicha = f.idFicha AND c_vigor.nome = 'vigor'

        WHERE f.idFicha = ${idFicha};
    `;
    
    console.log("Executando a instrução SQL: \n" + sql);
    return database.executar(sql)

}

module.exports = {
    buscarFicha
};