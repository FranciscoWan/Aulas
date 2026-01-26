// string

let color: string = "blue";

// number

let idade: number = 10;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
let big: bigint = 100n;

// booleano 

let isTrue: boolean = true;


// array - Determina o tipo do valor mas não a quantidade de valor

let list: number[] = [1,2,3];

let list1: Array<number> = [1,2,3]


// tuple - Determina o tipo do valor e a posição deles.

let tupla: [number, string] = [8, "Olá"];

// Tupla com número indeterminado de elementos

let tuplaIndetrminada: [string, ...number[]] = ["Oi", 5,7,8,9,10]

// Tupla com elementos opcionais

let tuplaOpcional: [string,number,boolean?] = ["Oi",5];
let tuplaOpcional1: [string,number,boolean?] = ["Oi",5,true];

// any - Aceita qualquer tipo de dado

let qualquer: any = "olá";
let qualquer1: any = 55;

// unknown - Quando precisamos receber um tipo de dado que desconhecemos.

let notSure: unknown = 4;
let notSure1: unknown = "olá";

// void - É a ausência total de qualquer tipo, utilizada comumente como tipo de funções que não retornam um valor

function warnUser(): void {
    console.log("Essa função não retorna nenhum valor.")
}

// object - O tipo objeto, representa um tipo não primitivo, ou seja, qualquer valor que não seja, number, string, boolean, bigint, null ou undefined.

function criarObjeto(lista:object){
    for (let item in lista){
        console.log(item)
    }
}


