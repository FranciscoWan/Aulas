// Exercícios de função para fixação

// 1 - Crie uma função que receba dois números e retorne o maior

function maiorNum(num1, num2){
    if (num1 > num2){
        return num1
    }
    return num2
}

// 2- Crie uma arrow function que verifique se um número é par

const par = (numVerificar) => {
    if (numVerificar%2==0){
        return `O número ${numVerificar} é par`
    }
    return `O número ${numVerificar} é impar`
}

// 3- Crie uma função que receba um nome e uma idade e retorne uma frase

function frasePersonalizada(nome, idade){
    return `Olá ${nome}, você tem ${idade} anos.`
}

console.log(maiorNum(4, 8))

console.log(par(11))

console.log(frasePersonalizada("Francisco", 28))


