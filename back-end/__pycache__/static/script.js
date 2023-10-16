let inputAdultos = document.getElementById('adultos');
let inputDuracao = document.getElementById('duracao');
let resultado = document.getElementById("resultado");

function calcular() {
    console.log("Calculando...");

    let adultos = inputAdultos.value;
    let duracao = inputDuracao.value;

    let qtc = carnePP(duracao) * adultos;
    let qtba = cervejaPP(duracao) * adultos;
    let qtb = bebidaPP(duracao) * adultos;

    resultado.innerHTML = `<p>${qtc / 1000} Kg de petiscos <p>`;

    resultado.innerHTML += `<p>${Math.ceil(qtb / 2000)} Garrafas de bebida 2L<p>`;
}

function carnePP(duracao) {
    if (duracao >= 6) {
        return 650;
    } else {
        return 400;
    }
}

function cervejaPP(duracao) {
    if (duracao >= 6) {
        return 2000;
    } else {
        return 1200;
    }
}

function bebidaPP(duracao) {
    if (duracao >= 6) {
        return 1500;
    } else {
        return 1000;
    }
}



