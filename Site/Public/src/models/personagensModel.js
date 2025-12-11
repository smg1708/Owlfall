var database = require("../database/config")

function mostrar(idUsuario) {
    
    var sql = `
        select * from vw_selectFicha
            where fkUsuario = ${idUsuario};
    `;
    
    console.log("Executando a instrução SQL: \n" + sql);
    return database.executar(sql)

}

module.exports = {
    mostrar
};