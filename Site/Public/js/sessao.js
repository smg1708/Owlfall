function validarSessao() {
    var email = sessionStorage.EMAIL_USUARIO;
    var nome = sessionStorage.NOME_USUARIO;

    var b_usuario = document.getElementById("b_usuario");

    if (email != null && nome != null) {
        b_usuario.innerHTML = nome;
    } else {
        window.location = "../login.html";
    }
}

function limparSessao() {
    sessionStorage.clear();
    window.location = "../login.html";
}

function aguardar() {
    var divAguardar = document.getElementById("div_aguardar");
    divAguardar.style.display = "flex";
}

function verificarLoginAntes() {
    var email = sessionStorage.EMAIL_USUARIO;
    var nome  = sessionStorage.NOME_USUARIO;

    if (!email || !nome) {
        alert("Você precisa estar logado para acessar essa pagina!");
        window.location = "../login.html";
        return false;
    }
    return true;
}

function finalizarAguardar(texto) {

    var divErrosLogin = document.getElementById("div_erros_login");
    if (texto) {
        divErrosLogin.style.display = "flex";
        divErrosLogin.innerHTML = texto;
    }
}

