function mostrarNome() {
    // 1. Seleciona o input e pega o valor
    var nomeDigitado = document.getElementById("nome").value;
    
    // 2. Seleciona o local onde o texto será exibido
    var localExibicao = document.getElementById("resultado");
    
    // 3. Define o texto do elemento com o nome digitado
    localExibicao.innerText = nomeDigitado;
}