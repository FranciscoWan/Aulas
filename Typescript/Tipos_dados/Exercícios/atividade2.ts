// Introdução:
// Os dois usuários gostaram da ideia da comunidade. Devemos seguir em frente e introduzir um pouco de ordem. Afinal, estamos na Alemanha. Vamos adicionar alguns administradores.
// Inicialmente, tínhamos apenas usuários no banco de dados em memória. Após a introdução dos administradores, precisamos corrigir os tipos para que tudo funcione bem em conjunto.

// Exercício:
// O tipo "Person" está faltando. Por favor, defina-o e utilize-o no array persons e na função logPerson, a fim de corrigir todos os erros de TypeScript.

import {Admin, admin1} from "./atividade3";
import { isAdmin, isUser } from "./atividade4";

export type Person = {
    name: string;
    age: number;
    occupation: string;
}

export function logPerson(pessoa: Person|Admin){
    if (isUser(pessoa)){
            console.log(`Olá ${pessoa.name}, você tem ${pessoa.age} anos e sua ocupação é ${pessoa.occupation}.`)
    } else if (isAdmin(pessoa)){
        console.log(`Olá ${pessoa.name}, você tem ${pessoa.age} anos e sua role é ${pessoa.role}.`)
    }
}


export const persons: Person[] = [
    {
        name: "Francisco",
        age: 28,
        occupation: "student",
    },
    {
        name: "ana",
        age: 22,
        occupation: "teacher"
    }
]

persons.forEach(logPerson)
logPerson(admin1)