"use strict";
// Introdução:
// Hora de filtrar os dados! Para sermos flexíveis, filtramos os usuários usando diversos critérios e retornamos apenas aqueles que correspondem a todos os critérios. Ainda não precisamos dos administradores, vamos filtrar apenas Users.
Object.defineProperty(exports, "__esModule", { value: true });
exports.filterUsers = filterUsers;
function filterUsers(users, criteria) {
    return users.filter(function (user) {
        return Object.entries(criteria).every(function (_a) {
            var key = _a[0], value = _a[1];
            return user[key] === value;
        });
    });
}
var persons = [
    { name: "Francisco", age: 28, occupation: "student" },
    { name: "Ana", age: 22, occupation: "teacher" },
    { name: "Carlos", age: 28, occupation: "teacher" },
    { name: "Marina", age: 28, occupation: "student" },
];
var result1 = filterUsers(persons, { age: 28 });
console.log(result1);
