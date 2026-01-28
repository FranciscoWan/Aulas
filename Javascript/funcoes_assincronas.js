// Funções assíncronas

// Promise simples
// Crie uma função que retorne uma Promise que resolve após 2 segundos com a mensagem "Concluído".

// const promessa_concluido = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve("Concluido")
//         reject("Falhou")
//     }, 2000);
// })

// promessa_concluido
//     .then(resultado => {
//         console.log(resultado)
//     })
//     .catch(resultado => {
//         console.log(resultado)
//     });


// // Usando async/await
// // Crie uma função async que chame a Promise do exercício anterior e exiba o resultado no console.

// async function promessa_anterior(promessa_function) {
//     try{
//         const resultado = await promessa_function;
//         console.log(resultado);
//     } catch (erro) {
//         console.log(erro);
//     }
// }

// promessa_anterior(promessa_concluido)

// Simulação de erro
// Crie uma Promise que:
// resolva se um número for maior que 10 rejeite caso contrário


// Tratando erro com try/catch
// Crie uma função async que chame a Promise do exercício 3 e trate o erro corretamente.



// Sequência assíncrona
// Crie duas funções assíncronas que retornem mensagens diferentes após tempos diferentes e execute elas em sequência.

// function delay(ms) {
//     return new Promise(resolve=>setTimeout(resolve,ms));
// };

// async function tempo1(temporizador){
//     await delay(temporizador);
//     console.log(`Tempo 1 finalizado após ${temporizador}ms`);
// };

// async function tempo2(temporizador){
//     await delay(temporizador);
//     console.log(`Tempo 2 finalizado após ${temporizador}ms`);
// }

// async function executarSequencia() {
//     await tempo1(2000)
//     await tempo2(1000)
// }

// executarSequencia()

// tempo1(2000)
// tempo2(1000)

// Execução paralela
// Crie duas Promises e execute ambas ao mesmo tempo usando Promise.all.

const promessa1 = new Promise((resolve, reject)=> resolve("Sucesso"));

const promessa2 = new Promise((resolve, reject)=> reject("Error"));

Promise.all([promessa1,promessa2])
    .then((resultados) => {
        console.log(resultados)
    })
    .catch((erro) => {
        console.error("Uma promise falhou " + erro)
    });

//  Retorna apenas o Error porque a lógica do Promise.all é semelhante ao && (and, lógica booleana)

Promise.allSettled([promessa1,promessa2])
    .then(resultados=>{
        console.log(resultados)
    })
    .catch(resultados=>{
        console.log(resultados)
    })

// Retorna o status e valores de todas as Promises

// Simulando requisição
// Crie uma função buscarProduto(id) que retorna uma Promise simulando uma busca após 1 segundo.



// Função com await dentro de loop
// Crie uma função async que percorra um array e aguarde 1 segundo entre cada item exibido.

// Retorno assíncrono
// Crie uma função async que retorne um número e mostre como acessar esse valor.

// Refatoração
// Pegue um código com setTimeout encadeado e reescreva usando async/await.