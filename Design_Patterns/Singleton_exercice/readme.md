# Exercício Prático — Design Pattern Singleton (Python)

## 🎯 Objetivo

Criar uma classe que garanta a existência de apenas uma única instância durante toda a execução do programa.

## 📌 Cenário

Você está desenvolvendo um sistema que precisa de uma única configuração global da aplicação.

Essa configuração:

- Guarda informações como:
  - nome da aplicação
  - ambiente (dev, prod)
- Não pode ser recriada
- Todas as partes do sistema devem usar a mesma instância

## ✅ Requisitos obrigatórios

Crie uma classe chamada `AppConfig`

A classe deve:

- Garantir que apenas uma instância exista
- Retornar sempre a mesma instância, mesmo quando chamada várias vezes

Deve possuir:

- Um método para definir o ambiente
- Um método para obter o ambiente

Crie um pequeno teste no final:

- Crie duas variáveis diferentes apontando para `AppConfig`
- Mostre (via `print`) que ambas referenciam o mesmo objeto
- Altere o ambiente em uma e mostre que a outra também reflete essa mudança

## 🚫 Restrições (importante)

- Não use variáveis globais soltas
- Não use bibliotecas externas
- Faça tudo apenas com Python puro
- Pode usar `__new__`, se quiser (não é obrigatório, mas é comum)

## 💡 Dica (sem entregar a solução)

Pense em onde o Python cria objetos e como você pode interceptar esse momento para devolver sempre a mesma instância.