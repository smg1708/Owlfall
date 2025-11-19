var express = require("express");
var router = express.Router();

var fichaController = require("../controllers/fichaController");

//Recebendo os dados do html e direcionando para a função cadastrar de usuarioController.js
router.post("/buscar", function (req, res) {
    fichaController.buscarFicha(req, res);
})

// router.post("/autenticar", function (req, res) {
//     usuarioController.autenticar(req, res);
// });

module.exports = router;