# Aula: Promise, then, async e await no JavaScript

## Objetivo da aula

Ao final da aula, o aluno deve:

* Entender por que Promise existe
* Saber usar `.then()` e `.catch()`
* Compreender `async` / `await`
* Saber quando usar cada abordagem
* Evitar erros comuns

## Estrutura da aula

* Problema do código assíncrono
* Promise e `.then()`
* `async` / `await`
* Comparação + exercícios rápidos

## 1. O problema do código assíncrono

JavaScript não espera tarefas demoradas.

```javascript
console.log("Início");

setTimeout(() => {
  console.log("Processando");
}, 2000);

console.log("Fim");
```

Saída:

```
Início
Fim
Processando
```

Precisamos de uma forma de esperar o resultado sem travar o programa.

## 2. Promise – o contrato do futuro

### O que é uma Promise?

O Promise() construtor cria Promise objetos. Ele é usado principalmente para encapsular APIs baseadas em callbacks que ainda não suportam promises.
Promise() só pode ser construído com new. Tentar chamá-lo sem new lança uma exceção TypeError.
Uma Promise representa um valor que:

* vai existir no futuro
* pode dar certo ou errado

### Estados:

* `pending`
* `fulfilled`
* `rejected`

### Criando uma Promise

```javascript
const promessa = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Concluído");
  }, 2000);
});
```

## 3. `.then()` e `.catch()`

### Consumindo uma Promise

```javascript
promessa
  .then(resultado => {
    console.log(resultado);
  })
  .catch(erro => {
    console.log("Erro:", erro);
  });
```

`.then()` executa quando `resolve` é chamado

`.catch()` executa quando `reject` é chamado

### Encadeamento com `then`

```javascript
buscarUsuario()
  .then(usuario => buscarPedidos(usuario.id))
  .then(pedidos => console.log(pedidos))
  .catch(erro => console.log(erro));
```

Aqui começa o problema de legibilidade…

## 4. `async` e `await` – forma moderna

### Função async

```javascript
async function buscarDados() {
  return "Dados";
}
```
A declaração async function define uma função assíncrona, que retorna um objeto AsyncFunction.
Toda função `async` retorna uma Promise.
Quando a função assíncrona retorna um valor, a Promise será resolvida com o valor retornado. Quando a função assíncrona lança uma exceção ou algum valor, a Promise será rejeitada com o valor lançado.
Uma função assíncrona pode conter uma expressão await, que pausa a execução da função assíncrona e espera pela resolução da Promise passa, e depois retoma a execução da função assíncrona e retorna o valor resolvido.

A proposta das funções async/await é de simplificar o uso de forma síncrona das Promises e executar alguns procedimentos em um grupo de Promises.

### await

```javascript
async function executar() {
  const resultado = await promessa;
  console.log(resultado);
}
```

`await`:

* pausa a função
* não trava o programa
* só funciona dentro de `async`

## 5. Tratamento de erro com try/catch

```javascript
async function executar() {
  try {
    const resultado = await promessa;
    console.log(resultado);
  } catch (erro) {
    console.log("Erro:", erro);
  }
}
```

`reject()` vira exceção no `await`.

## 6. Comparação direta

### Com `.then()`

```javascript
buscarDados()
  .then(dados => console.log(dados))
  .catch(err => console.log(err));
```

### Com `async/await`

```javascript
try {
  const dados = await buscarDados();
  console.log(dados);
} catch (err) {
  console.log(err);
}
```

Mesmo comportamento

`async/await` é mais legível

## 7. Erros comuns

### Esquecer o `await`

```javascript
const resultado = buscarDados(); // Promise
```

### Usar `await` fora de `async`

### Achar que `try/catch` funciona sem `await`

## 8. Exercícios rápidos

1. Crie uma Promise que resolve após 1 segundo
2. Consuma usando `.then()`
3. Refatore usando `async/await`
4. Simule um erro e trate com `catch` / `try-catch`

## Resumo final

* Promise é o contrato
* `then` lê o sucesso
* `catch` lê o erro
* `async/await` é açúcar sintático
* `reject` ≈ `throw`
