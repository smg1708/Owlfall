const imagemModel = require('../models/imagemModel');


function salvar(req, res) {
  const imagem = req.file.filename;

  const usuario = { imagem }
  
  imagemModel.salvar(usuario)
  .then(resultado => {
    res.status(201).send("Usuario criado com sucesso");
  }).catch(err => {
    res.status(500).send(err);
  });
}

function buscarUsuarioPeloId(req, res) {
  console.log(req.params.id);
  imagemModel.buscarUsuarioPeloId(req.params.id)
  .then(resultado => {
    res.json(resultado);
  }).catch(err => {
    res.status(500).send(err);
  });
}

module.exports = { salvar, buscarUsuarioPeloId }