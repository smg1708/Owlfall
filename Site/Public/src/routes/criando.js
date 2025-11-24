var express = require("express");
var router = express.Router();

var criandoController = require("../controllers/criandoController");

router.post("/criarFicha", function (req, res) {
    criandoController.criarFicha(req, res);
})

module.exports = router;