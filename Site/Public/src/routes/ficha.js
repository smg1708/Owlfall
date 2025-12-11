var express = require("express");
var router = express.Router();
const upload = require('../config/configUpload'); // ARQUIVO COM A CONFIGURAÇÃO DO UPLOAD
const fichaController = require('../controllers/fichaController');


router.put('/imagem', upload.single('foto_personagem'), (req, res) => {
    fichaController.salvarImagem(req, res);
});

router.get("/buscar", function (req, res) {
    fichaController.buscarFicha(req, res);
})

router.put("/atualizar", function (req, res) {
    fichaController.atualizarFicha(req, res);
})

module.exports = router;
