var express = require("express");
var router = express.Router();

var personagensController = require("../controllers/personagensController");

//Recebendo os dados do html e direcionando para a função cadastrar de usuarioController.js
router.get("/mostrar/:idUsuario", function (req, res) {
    personagensController.mostrar(req, res);
})

module.exports = router;