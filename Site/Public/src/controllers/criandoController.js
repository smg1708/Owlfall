var criandoModel = require("../models/criandoModel");

function autenticar(req, res) {
    var dadosPersonagem = req.body.dadosPersonagemServer;

    if (dadosPersonagem == undefined) {
        res.status(400).send("Dados indefinido(s)!");
    } else {

        dadosPersonagemModel.autenticar(dadosPersonagem)
            .then(
                function (resultadoAutenticar) {
                    console.log(`\nResultados encontrados: ${resultadoAutenticar.length}`);
                    console.log(`Resultados: ${JSON.stringify(resultadoAutenticar)}`); // transforma JSON em String

                    if (resultadoAutenticar.length == 1) {
                        console.log(resultadoAutenticar);
                        
                        res.json({
                            idCaracteristicas: resultadoAutenticar[0].idCaracteristicas,
                            descricao: resultadoAutenticar[0].descricao,
                            // nome: resultadoAutenticar[0].nome,
                            // senha: resultadoAutenticar[0].senha,
                        });
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

function cadastrar(req, res) {
    // Crie uma variável que vá recuperar os valores do arquivo cadastro.html
    var dadosPersonagem = req.body.dadosPersonagemServer;

    // Faça as validUsuarioações dos valores
    if (nome == undefined) {
        res.status(400).send("Dados não estão definidos");
    } else {

        // Passe os valores como parâmetro e vá para o arquivo usuarioModel.js
        dadosPersonagemModel.cadastrar(dadosPersonagem)
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
    autenticar,
    cadastrar
}