// Criando objetos em typescript

// Em TypeScript conseguimos criar diferentes tipos de objetos de acordo com a necessidade de um script

type Person = {
    name: string;
    age: number;
};

function greet(person:Person){
    return "Hello " + person.name;
}

// Podemos tambem, criar objetos utilizando interface

interface Pessoa{
    name: string;
    age: number;
};

function saudacao(pessoa:Pessoa){
    return "Olá " + pessoa.name;
}




