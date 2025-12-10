# 🎅 Exercícios de Natal em Python 🎄

Este repositório contém uma série de exercícios de programação em Python com o tema natalino, abrangendo conceitos básicos como **inputs**, **cálculos aritméticos**, **estruturas condicionais** e **loops/menus interativos**.

## 🎁 Descrição dos Exercícios

### 🎄 Exercício 1 – Mensagem para o Papai Noel (Inputs)

Este exercício foca na obtenção de dados do usuário (`input()`) e na formatação de strings.

**Objetivo:**
Criar um programa que solicite e armazene três informações do usuário:

1.  Seu nome
2.  Sua idade
3.  O que gostaria de ganhar de Natal

Ao final, o programa deve exibir uma **mensagem personalizada** como se fosse uma carta enviada ao Papai Noel.

**Saída Esperada (Exemplo):**

> Olá, Papai Noel\! Meu nome é Ana, tenho 10 anos e neste Natal eu gostaria muito de ganhar uma bicicleta\!

-----

### 🎅 Exercício 2 – Soma de Presentes para o Trenó (Cálculos)

Este exercício introduz a realização de cálculos aritméticos básicos.

**Objetivo:**
Criar um programa que:

1.  Peça ao usuário o **número de presentes** que serão entregues na **Cidade A**.
2.  Peça o **número de presentes** que serão entregues na **Cidade B**.
3.  Calcule o **total de presentes** que o Papai Noel precisará carregar no trenó.
4.  Exiba uma mensagem informando o total.

**Saída Esperada (Exemplo):**

> Papai Noel irá carregar 350 presentes em seu trenó\!

-----

### 🎁 Exercício 3 – Capacidade do Trenó (Condições)

Este exercício utiliza o total de presentes (idealmente calculado no Exercício 2) para aplicar **estruturas condicionais** (`if/elif/else`).

**Objetivo:**
Verificar a capacidade máxima do trenó (que é de **1000 presentes**) e exibir mensagens diferentes com base no total de presentes:

  * **Se o total ultrapassar 1000:** Exibir mensagem de sobrecarga e informar quantos presentes ficarão para a próxima viagem.
  * **Se o total estiver entre 500 e 1000 (inclusive 500):** Informar que a entrega é possível normalmente.
  * **Se o total for menor que 500:** Avisar que o Papai Noel precisa reabastecer e mostrar quantos presentes faltam para atingir 1000.

**Saída Esperada (Exemplo - Sobrecarga):**

> Há presentes demais\! O trenó só aguenta 1000. Ficarão 150 presentes para a próxima viagem.

-----

### ⭐ Exercício 4 – Menu de Opções Natalino (Loops e Funções)

Este exercício visa combinar os três exercícios anteriores dentro de uma **estrutura de repetição** (`while` loop) e talvez o uso de **funções**, criando um programa principal interativo.

**Objetivo:**
Criar um programa que exibe um menu de opções e continua rodando até que o usuário escolha "Sair".

**Opções do Menu:**

1.  Enviar mensagem para o Papai Noel (Executa lógica do **Exercício 1**)
2.  Calcular total de presentes (Executa lógica do **Exercício 2**)
3.  Verificar capacidade do trenó (Executa lógica do **Exercício 3**)
4.  Sair do programa

**Exibição do Menu:**

```
===== MENU DE NATAL =====
1 - Mensagem para o Papai Noel
2 - Soma de presentes
3 - Capacidade do trenó
4 - Sair
=========================
```
