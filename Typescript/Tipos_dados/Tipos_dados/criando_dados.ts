// Criação de tipos de dados específicos

// Existem duas formas para criação de dados no typescript

// interface -> Recomendado para contratos, APIs e modelos de objetos, HIERARQUIA:

interface compra {
    preco: number;
    quantia: number;
    produto: string;
}

// Vantagens:
// . Pensada para descrever a forma de objetos.
// . Pode ser estendida (extends).
// . Suporta declaration merging (muito importante em libs).
// . Cria hierarquia de dados.
// . Pode crescer no futuro
// . É mais legível como "contrato"

interface lista_mercado extends compra {
    validade: string;
}

// lista_mercado é uma classe que herda os atributos de compra e ADICIONA (extende) com validade.

const comprar_mercado: lista_mercado = {
    preco: 20,
    quantia: 10,
    produto: "Macarrão",
    validade: "10/10/26",
}

console.log(comprar_mercado)


// type -> COMPOSIÇÃO, unions, utilitários e tipos mais complexos:

type User = {
    name: string;
    age: number;
    occupation: string;
}

//  Vantagens:
// . Podem representar qualquer coisa, não só objetos.
// . Permite union types.
// . Permite interseções.
// . Funciona melhor com tipos utilitários.

// union types:
type Status = "active"|"inactive"

// intersection type:
type UserWithStatus = User & {status: Status}

