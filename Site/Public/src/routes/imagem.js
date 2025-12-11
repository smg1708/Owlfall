const express = require('express');
const router = express.Router();
const upload = require('../config/configUpload');
const imagemController = require('../controllers/imagemController');

router.get("", (req, res) => {
  res.render("index")
});

router.post('/cadastro', upload.single('foto'), (req, res) => {
  imagemController.salvar(req, res);
});

router.get('/:id', upload.single('foto'), (req, res) => {
  imagemController.buscarUsuarioPeloId(req, res);
});

module.exports = router;

