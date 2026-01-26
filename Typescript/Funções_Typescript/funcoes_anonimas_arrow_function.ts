//  Funções anônimas 

const mult = function (num1: number,num2: number): number{
    return num1*num2
}

console.log(mult(5,2))

// Arrow function - não necessita da palavra function para ser criada, porém não é possível criá-la sem salvar em uma variável.

const dividir = (num1: number, num2: number): number => {
    return num1/num2
}


