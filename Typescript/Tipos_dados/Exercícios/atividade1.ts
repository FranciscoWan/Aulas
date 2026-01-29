// Estamos iniciando uma pequena comunidade de usuários. Por motivos de desempenho, decidimos armazenar todos os usuários diretamente no código. Dessa forma, podemos oferecer aos nossos desenvolvedores mais oportunidades de interação com usuários — pelo menos no que diz respeito aos dados relacionados a usuários. Todas as questões relacionadas à GDPR serão resolvidas em outro momento.
// Isso servirá como base para nossos experimentos futuros durante estes exercícios.

// Exercício:
// Dado os dados, defina a interface "User" e utilize-a adequadamente.

export type User = {
    name: string;
    age: number;
    occupation: string;
};

export const users: User[] =[
    {
        name: "Verstapen",
        age: 22,
        occupation: "racer"
    },
    {
        name: "Pedro",
        age: 30,
        occupation: "worker"
    }
]

export interface User1 {
    name: string;
    age: number;
    occupation: string
}

export const users1: User1[] =[
    {
        name: "Verstapen",
        age: 22,
        occupation: "racer"
    },
    {
        name: "Pedro",
        age: 30,
        occupation: "worker"
    }
]
