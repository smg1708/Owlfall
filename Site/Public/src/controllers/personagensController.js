var personagensModel = require("../models/personagensModel");

function mostrar(req, res) {
    var idUsuario = req.body.idUsuario;

    if (idUsuario == undefined) {
        res.status(400).send("Fichas não foram carregadas!");
    } else {

        personagensModel.mostrar(idUsuario)
            .then(
                function (resultado) {
                    console.log(`\nResultados encontrados: ${resultado.length}`);
                    console.log(`Resultados: ${JSON.stringify(resultado)}`); // transforma JSON em String

                    if (resultado.length > 0) {
                        console.log(resultado);
                        res.json(resultado[0]);
                    }   else {
                        res.status(403).send("Fichas não foram carregadas!");
                    }
                }
            ).catch(
                function (erro) {
                    console.log(erro);
                    console.log("\nHouve um erro ao realizar o login! Erro: ", erro.sqlMessage);
                    res.status(500).json(erro.sqlMessage);
                }
            );
    }

}

module.exports = {
    mostrar
}