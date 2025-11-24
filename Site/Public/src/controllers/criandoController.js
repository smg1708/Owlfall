var criandoModel = require("../models/criandoModel");

function criarFicha(req, res) {
    // Crie uma variável que vá recuperar os valores do arquivo cadastro.html
    var dados = req.body.dadosPersonagemServer;
    var idUsuario = req.body.idUsuarioServer;

    // Faça as validUsuarioações dos valores
    if (!dados || dados.length == 0) {
        res.status(400).send("Nenhum dado enviado!");
    } else {

        // Passe os valores como parâmetro e vá para o arquivo usuarioModel.js
        criandoModel.criarFicha(dados, idUsuario)
            .then(
                function (resultado) {
                    res.json(resultado);
                }
            ).catch(
                function (erro) {
                    console.log(erro);
                    console.log(
                        "\nHouve um erro ao realizar o cadastro! Erro: ",
                        erro.sqlMessage
                    );
                    res.status(500).json(erro.sqlMessage);
                }
            );
    }
}

module.exports = {
    criarFicha
}