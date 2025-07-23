// // Laço for (inicialização;condição;incremento);
// for(let i = 0; i<=10; i++){
//     alert(i);
// }

// // Atividade 1:
// let num = Number(prompt("Digite um número: "));
// for (let i=1; i<=10; i++){
//     console.log(`${num} x ${i} = ${num*i}`);
// }

// // Atividade 2:
// for (let i = 1; i<=10; i++){
//     console.log(i);
//     if (i==6){
//         break;
//     }
// }

// //  Atividade 3:
// for(let i=1; i<=10; i++){
//     if(i==5){
//         continue;
//     }
//     console.log(i);
// }

// // Atividade 4:
// let palavra = "Bem vindo a infinity";
// let cont = 0;
// for (let letra of palavra){
//     console.log(letra);
//     if (letra=="a"||letra=="e"||letra=="i"||letra=="o"||letra=="u"){
//         cont++
//     }
// }
// console.log(`Existem ${cont} vogais na frase "${palavra}".`)

// // Atividade 5:
// let cont = 1;
// while (cont<=5){
//     console.log(cont)
//     cont++
// }

// // Atividade 6:
// let num = 1
// let soma = 0
// while (num!=0){
//     num = Number(prompt("Digite um número"))
//     soma += num
// }

// alert(`A soma dos números digitados foi de ${soma}`)

//  Atividade 7:
// // Resolução 1 -
// let cont = 1
// while (cont<=20){
//     if (cont%3!=0){
//         console.log(cont)
//     }
//     cont++
// }

// // Resolução 2 -
// let cont = 0
// while (cont<=20){
//     cont++
//     if (cont%3==0){
//         continue
//     }
//     console.log(cont)
// }

// // Atividade 8:
// // Fórmula da média - soma/qtd_numeros
// let num = 0
// let soma = 0
// let cont = 0
// while (num>=0){
//     num = Number(prompt("Digite um número"))
//     if (num>=0){
//         soma += num
//         cont++
//     }
// }
// media = soma/cont
// alert(`A soma dos números foi ${soma}, foram digitados ${cont} números e a média é de ${media}`)