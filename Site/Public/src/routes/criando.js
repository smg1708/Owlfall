var express = require("express");
var router = express.Router();

var criandoController = require("../controllers/criandoController");

//Recebendo os dados do html e direcionando para a função cadastrar de usuarioController.js
router.post("/criarFicha", function (req, res) {
    criandoController.criarFicha(req, res);
})

// router.post("/autenticar", function (req, res) {
//     usuarioController.autenticar(req, res);
// });

module.exports = router;