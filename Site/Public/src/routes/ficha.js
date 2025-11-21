var express = require("express");
var router = express.Router();
const upload = require('../config/configUpload'); // ARQUIVO COM A CONFIGURAÇÃO DO UPLOAD
const fichaController = require('../controllers/fichaController');

//Recebendo os dados do html e direcionando para a função cadastrar de usuarioController.js

router.put('/imagem', upload.single('foto_personagem'), (req, res) => {
    fichaController.salvarImagem(req, res);
});

router.get("/buscar", function (req, res) {
    fichaController.buscarFicha(req, res);
})

module.exports = router;
