# Funções em TypeScript

## O que são funções?

**Conceito**

Uma função é um bloco de código reutilizável que executa uma tarefa específica. Em vez de repetir código várias vezes, você cria uma função e chama sempre que precisar.

**Analogia**

Pense em uma função como uma receita:
* Ingredientes → parâmetros
* Modo de preparo → código
* Prato pronto → retorno

**Sem função (repetição de código)**

```typescript
console.log("Olá, João");
console.log("Olá, Maria");
console.log("Olá, Ana");
```

**Com função**

```typescript
function cumprimentar(nome: string) {
  console.log(`Olá, ${nome}`);
}

cumprimentar("João");
cumprimentar("Maria");
cumprimentar("Ana");
```

---

## Criando funções em TypeScript

**Estrutura básica**

```typescript
function nomeDaFuncao() {
  // código
}
```

**Exemplo simples**

```typescript
function mostrarMensagem() {
  console.log("Bem-vindo ao sistema!");
}

mostrarMensagem();
```

---

## Parâmetros, retorno e tipagem

**Parâmetros**

São valores que a função recebe para trabalhar.

```typescript
function somar(a: number, b: number) {
  console.log(a + b);
}

somar(5, 3);
```

**Retorno (`return`)**

Quando queremos que a função devolva um valor.

```typescript
function somar(a: number, b: number): number {
  return a + b;
}

const resultado = somar(10, 5);
console.log(resultado);
```

**Importante:**
* Após o `return`, a função para de executar
* O tipo do retorno pode (e deve) ser definido

**Função sem retorno**

```typescript
function exibirAlerta(mensagem: string): void {
  console.log(mensagem);
}
```

`void` significa: não retorna nada

---

## Funções anônimas e Arrow Functions

**Função anônima**

```typescript
const multiplicar = function (a: number, b: number): number {
  return a * b;
};
```

**Arrow Function (muito usada em projetos reais)**

```typescript
const dividir = (a: number, b: number): number => {
  return a / b;
};
```

**Versão reduzida:**

```typescript
const dobrar = (valor: number): number => valor * 2;
```

---

## Escopo e boas práticas

**Escopo**

Variáveis criadas dentro da função só existem ali.

```typescript
function exemplo() {
  let mensagem = "Olá";
  console.log(mensagem);
}

// console.log(mensagem); ❌ erro
```

**Boas práticas**
* Nome claro e descritivo
* Uma função → uma responsabilidade
* Evitar funções muito longas
* Tipar parâmetros e retorno

---

## Funções assíncronas

**O que é uma função assíncrona?**

É uma função que não retorna o resultado imediatamente, pois depende de algo externo:
* API
* Banco de dados
* Arquivo
* Tempo (delay)

**Exemplo de algo demorado**

```typescript
setTimeout(() => {
  console.log("Demorou 2 segundos");
}, 2000);
```

**Função assíncrona com `async`**

```typescript
async function buscarDados() {
  return "Dados carregados";
}
```

Toda função `async` retorna uma Promise

**Usando `await`**

```typescript
async function buscarUsuario() {
  const usuario = await buscarDados();
  console.log(usuario);
}

buscarUsuario();
```

**`await`:**
* Pausa a execução dentro da função
* Só funciona dentro de funções `async`

**Exemplo prático com delay**

```typescript
function esperar(ms: number): Promise<string> {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve("Processo finalizado");
    }, ms);
  });
}

async function executar() {
  const resposta = await esperar(2000);
  console.log(resposta);
}

executar();
```

---

## Exercícios práticos

**Exercício 1**

Crie uma função que receba dois números e retorne o maior.

```typescript
// Seu código aqui
```

**Exercício 2**

Crie uma arrow function que receba um nome e retorne:

```typescript
"Bem-vindo, NOME!"
```

```typescript
// Seu código aqui
```

**Exercício 3 (assíncrono)**

Crie uma função assíncrona que:
* Espere 3 segundos
* Retorne a mensagem: `"Download concluído"`

```typescript
// Seu código aqui
```

---

## Respostas dos Exercícios

<details>
<summary>Clique para ver as respostas</summary>

**Exercício 1**

```typescript
function maiorNumero(a: number, b: number): number {
  return a > b ? a : b;
}

console.log(maiorNumero(10, 5)); // 10
```

**Exercício 2**

```typescript
const bemVindo = (nome: string): string => `Bem-vindo, ${nome}!`;

console.log(bemVindo("João")); // Bem-vindo, João!
```

**Exercício 3**

```typescript
function aguardar(ms: number): Promise<string> {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve("Download concluído");
    }, ms);
  });
}

async function fazerDownload() {
  console.log("Iniciando download...");
  const resultado = await aguardar(3000);
  console.log(resultado);
}

fazerDownload();
```

</details>

---

## Recursos adicionais

* [TypeScript Handbook - Functions](https://www.typescriptlang.org/docs/handbook/2/functions.html)
* [MDN - Functions](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide/Functions)
* [TypeScript Playground](https://www.typescriptlang.org/play) - Para testar código online

---

**Desenvolvido para fins educacionais**