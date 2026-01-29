// Introdução:
// Como já temos algumas informações adicionais sobre nossos usuários, é uma boa ideia exibi-las de uma forma agradável.

// Exercício:
// Corrija os erros de tipagem na função logPerson.
// A função logPerson deve aceitar tanto User quanto Admin e deve exibir as informações relevantes de acordo com a entrada: occupation para User e role para Admin.



export type Admin = {
    name: string;
    age: number;
    role: "GUEST" | "ADMIN";
}

export const admin1: Admin = {
    name: "João",
    age: 30,
    role: "GUEST",
}

