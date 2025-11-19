var fichaModel = require("../models/fichaModel");

function buscarFicha(req, res) {
    var idFicha = req.body.idFicha;

    if (idFicha == undefined) {
        res.status(400).send("Dados indefinido(s)!");
    } else {

        fichaModel.buscarFicha(idFicha)
            .then(
                function (resultado) {
                    console.log(`\nResultados encontrados: ${resultado.length}`);
                    console.log(`Resultados: ${JSON.stringify(resultado)}`); // transforma JSON em String

                    if (resultado.length > 0) {
                        console.log(resultado);
                        res.json(resultado[0]);
                    }   else {
                        res.status(403).send("Dados inválido(s)");
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
    buscarFicha
}