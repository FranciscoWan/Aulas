# Revisão Geral – Listas, Tuplas, Sets e Dicionários

Este documento complementa o conteúdo visto em aula e serve como guia de estudo e consulta.  
Aqui você encontrará explicações adicionais, exemplos práticos e exercícios extras para reforçar o aprendizado.

---

## 1. Por que usar coleções?

As coleções são fundamentais em Python para **armazenar, organizar e manipular dados**.  
Elas permitem lidar com grandes quantidades de informações de forma eficiente.

- **Listas** → Quando você precisa de uma sequência **mutável** (que pode mudar).
- **Tuplas** → Quando você precisa de uma sequência **imutável** (não pode mudar).
- **Sets** → Quando você precisa de uma coleção de itens **únicos** (sem duplicatas).
- **Dicionários** → Quando você precisa mapear **chaves para valores**.

---

## 2. Exemplos práticos além da sala de aula

### Listas
```python
# Controle de estoque de uma loja
estoque = ["camisa", "calça", "tênis"]
estoque.append("boné")   # adiciona novo item
print(estoque)
```

### Tuplas
```python
# Coordenadas geográficas (imutáveis)
coordenadas = (23.5, 46.6)
print(f"Latitude: {coordenadas[0]}, Longitude: {coordenadas[1]}")
```

### Sets
```python
# Cadastro de emails (sem duplicatas)
emails = {"ana@gmail.com", "joao@gmail.com", "ana@gmail.com"}
print(emails)  # saída terá apenas um "ana@gmail.com"
```

### Dicionários
```python
# Cadastro de alunos com nota
alunos = {"Ana": 9.0, "João": 7.5}
alunos["Maria"] = 8.0  # adiciona nova aluna
print(alunos)
```

---

## 3. Boas práticas

- Use **listas** quando a ordem dos elementos importa e os dados podem mudar.
- Use **tuplas** quando os dados não devem ser alterados (ex.: coordenadas, configurações fixas).
- Use **sets** para eliminar duplicatas ou checar rapidamente a existência de um item.
- Use **dicionários** para representar dados que possuem **pares de chave-valor** (ex.: nome → telefone).

---

## 4. Exercícios Extras

### 1. Listas
Peça ao usuário que insira 5 números e armazene-os em uma lista. Depois, exiba:
- O maior número
- O menor número
- A soma de todos os números

---

### 2. Tuplas
Crie uma tupla com os dias da semana. Peça ao usuário que digite um número de 1 a 7 e mostre o dia correspondente.

---

### 3. Sets
Peça ao usuário para digitar 5 nomes, permitindo repetições. Armazene-os em um set e mostre apenas os nomes únicos.

---

### 4. Dicionários
Crie um dicionário que armazena o nome e a idade de 3 pessoas. Depois, exiba:
- O nome da pessoa mais velha
- O nome da pessoa mais nova

---

### 5. Desafio Final
Monte um **mini-sistema de contatos** usando dicionários:
- Adicione contatos com nome e telefone
- Permita remover contatos
- Exiba todos os contatos cadastrados
