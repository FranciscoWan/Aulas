# Aula 2 – Laços de Repetição em Python

Nesta segunda aula do **Super Reforço de Python**, vamos explorar os laços de repetição: estruturas que permitem executar um bloco de código várias vezes de forma controlada.

---

## 📌 Conteúdo da Aula

### 1. Estrutura do laço `for`
O laço `for` é muito usado quando sabemos **quantas vezes queremos repetir** algo, ele **itera (percorre) sobre uma sequência**.

#### Exemplo 1: laço `for` apenas com fim:
```python
for i in range(5):  
    print(i)
```
🔎 O código acima gera os números de 0 até 4.

#### Exemplo 2: laço `for` com início e fim:
```python
for i in range(3, 7): 
    print(i)  
```
🔎 O código acima gera os números de 3 até 6.

#### Exemplo 3: laço `for` com início e fim e passo:
```python
for i in range(2, 11, 2):  
    print(i)
```
🔎 O código acima gera os números de 2 até 10, "pulando" de 2 em 2.

#### Exemplo 4: iterando em listas:
```python
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)
```
🔎 O código acima mostrará as frutas dentro da lista, uma a uma.

---

### 2. Estrutura do laço `while`
O laço `while` é usado quando **não sabemos exatamente quantas repetições serão necessárias**, mas temos uma **condição para continuar**.

#### Exemplo 1:
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```
🔎 O código acima gera os números de 0 até 4.

#### Exemplo 2:
```python
contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break
```
🔎 O código acima gera os números de 0 até 4.

---

### 3. Comando `break`
O `break` encerra o laço **antes que a condição termine**.

#### Exemplo com `for`:
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

#### Exemplo com `while`:
```python
contador = 0
while True:
    print(contador)
    if contador == 3:
        break
    contador += 1
```

---

### 4. Comando `continue`
O `continue` **pula a iteração atual** e continua o laço.

#### Exemplo com `for`:
```python
for i in range(6):
    if i == 3:
        continue
    print(i)
```

#### Exemplo com `while`:
```python
contador = 0
while contador < 6:
    contador += 1
    if contador == 3:
        continue
    print(contador)
```

---

## 📝 Exercícios

1. **Contador de Números:**  
   Peça ao usuário um número e faça um programa que conte de 0 até esse número.  
   ➡ Resolva usando `for` e depois usando `while`.

2. **Tabuada:**  
   Peça ao usuário um número e exiba a tabuada desse número de 1 a 10.  
   ➡ Resolva usando `for` e depois usando `while`.

3. **Somatório:**  
   Solicite ao usuário um número e calcule a soma de todos os números de 1 até esse número.  
   ➡ Resolva usando `for` e depois usando `while`.

4. **Contagem Regressiva:**  
   Peça um número inicial ao usuário e faça uma contagem regressiva até 0.

5. **Números Ímpares:**  
   Exiba todos os números ímpares de 1 até 20.

---

### Lista de exercícios extras

[Lista Exercícios for](https://github.com/FranciscoWan/aulas/tree/main/Python/L%C3%B3gica%20programa%C3%A7%C3%A3o%20python/Aula%204%20-%20FLEX)  
[Lista Exercícios while](https://github.com/FranciscoWan/aulas/tree/main/Python/L%C3%B3gica%20programa%C3%A7%C3%A3o%20python/Aula%203%20-%20FLEX)
