"use strict";
// Introdução:
// Os dois usuários gostaram da ideia da comunidade. Devemos seguir em frente e introduzir um pouco de ordem. Afinal, estamos na Alemanha. Vamos adicionar alguns administradores.
// Inicialmente, tínhamos apenas usuários no banco de dados em memória. Após a introdução dos administradores, precisamos corrigir os tipos para que tudo funcione bem em conjunto.
Object.defineProperty(exports, "__esModule", { value: true });
exports.persons = void 0;
exports.logPerson = logPerson;
// Exercício:
// O tipo "Person" está faltando. Por favor, defina-o e utilize-o no array persons e na função logPerson, a fim de corrigir todos os erros de TypeScript.
var atividade3_1 = require("./atividade3");
var atividade4_1 = require("./atividade4");
function logPerson(pessoa) {
    if ((0, atividade4_1.isUser)(pessoa)) {
        console.log("Ol\u00E1 ".concat(pessoa.name, ", voc\u00EA tem ").concat(pessoa.age, " anos e sua ocupa\u00E7\u00E3o \u00E9 ").concat(pessoa.occupation, "."));
    }
    else if ((0, atividade4_1.isAdmin)(pessoa)) {
        console.log("Ol\u00E1 ".concat(pessoa.name, ", voc\u00EA tem ").concat(pessoa.age, " anos e sua role \u00E9 ").concat(pessoa.role, "."));
    }
}
exports.persons = [
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
];
exports.persons.forEach(logPerson);
logPerson(atividade3_1.admin1);
