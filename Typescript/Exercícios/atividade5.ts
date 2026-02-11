// Introdução:
// Hora de filtrar os dados! Para sermos flexíveis, filtramos os usuários usando diversos critérios e retornamos apenas aqueles que correspondem a todos os critérios. Ainda não precisamos dos administradores, vamos filtrar apenas Users.

// Exercício:
// Sem duplicar estruturas de tipo, modifique a definição da função filterUsers para que possamos passar apenas os critérios necessários, e não todas as informações do User, como é exigido atualmente pela tipagem.

// Exercício bônus (maior dificuldade):
// Exclua a propriedade type dos critérios de filtragem.

import {Admin, admin1} from "./atividade3";
import { isAdmin, isUser } from "./atividade4";
import {Person, logPerson} from './atividade2'

export type Criterio = {
    criterio: string
    valor: string | number
}

export function filterUsers(
  users: Person[],
  criteria: Partial<Person>
): Person[] {
  return users.filter(user => {
    return Object.entries(criteria).every(([key, value]) => {
      return user[key as keyof Person] === value;
    });
  });
}

const persons: Person[] = [
  { name: "Francisco", age: 28, occupation: "student" },
  { name: "Ana", age: 22, occupation: "teacher" },
  { name: "Carlos", age: 28, occupation: "teacher" },
  { name: "Marina", age: 28, occupation: "student" },
];

const result1 = filterUsers(persons, { age: 28 });
console.log(result1);