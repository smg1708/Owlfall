var fichaModel = require("../models/fichaModel");

function buscarFicha(req, res) {
    var idFicha = req.query.idFicha;

    if (idFicha == undefined) {
        res.status(400).send("Id indefinido(s)!");
    } else {

        fichaModel.buscarFicha(idFicha)
            .then(
                function (resultado) {
                    console.log(`\nResultados encontrados: ${resultado.length}`);
                    console.log(`Resultados: ${JSON.stringify(resultado)}`); // transforma JSON em String

                    if (resultado.length > 0) {
                        console.log(resultado);
                        res.json(resultado);
                    }   else {
                        res.status(403).send("Ficha nao encontrada");
                    }
                }
            ).catch(
                function (erro) {
                    console.log(erro);
                    console.log("\nHouve um erro ao carregar a ficha! Erro: ", erro.sqlMessage);
                    res.status(500).json(erro.sqlMessage);
                }
            );
    }

}

function salvarImagem(req, res) {
  var idFicha = req.body.idFicha;
  const imagem = req.file.filename;
  
  fichaModel.salvarImagem(idFicha, imagem)
  .then(resultado => {
    res.status(201).send("imagem enviada com sucesso");
  }).catch(err => {
    res.status(500).send(err);
  });
}

function atualizarFicha(req, res) {
  
  fichaModel.atualizarFicha(req.body)
  .then(resultado => {
    res.status(201).send("Ficha atualizada com sucesso!");
  }).catch(err => {
    res.status(500).send(err);
  });
}

module.exports = {
    buscarFicha,
    salvarImagem,
    atualizarFicha
}