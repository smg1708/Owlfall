var express = require("express");
var router = express.Router();

var personagensController = require("../controllers/personagensController");

router.get("/mostrar/:idUsuario", function (req, res) {
    personagensController.mostrar(req, res);
})

module.exports = router;