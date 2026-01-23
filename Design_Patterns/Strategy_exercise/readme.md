# Exercício Prático — Strategy Pattern (Python)

## 🎯 Objetivo

Implementar o Strategy Pattern para permitir trocar algoritmos em tempo de execução, sem usar `if/else` espalhado no código.

## 📌 Cenário

Você está desenvolvendo um sistema de frete para um e-commerce.

O valor do frete muda conforme a estratégia escolhida:

- Frete Normal
- Frete Expresso
- Frete Retirada na Loja

O sistema deve:

- Calcular o frete
- Poder trocar o tipo de frete sem alterar o código principal

## 🧩 Estrutura esperada

### 1️⃣ Interface da Strategy

- Classe abstrata `FreteStrategy`
- Método:
  - `calcular(valor_compra)`

### 2️⃣ Estratégias concretas

Implemente 3 estratégias:

- `FreteNormal`
  - 10% do valor da compra
- `FreteExpresso`
  - 20% do valor da compra
- `FreteRetirada`
  - Frete grátis (0)

### 3️⃣ Contexto

- Classe `Carrinho`
- Deve receber uma estratégia de frete
- Deve permitir:
  - Trocar a estratégia em runtime
  - Calcular o valor final da compra

## ✅ Requisitos obrigatórios

✔ Use `ABC` e `@abstractmethod`

✔ Nenhum `if` ou `elif` no cálculo do frete

✔ Estratégias intercambiáveis

✔ Carrinho não pode conhecer implementações concretas

✔ Strategy deve focar no comportamento, não na criação

## 🧪 Exemplo de uso esperado

```python
carrinho = Carrinho(FreteNormal())
print(carrinho.total(100))  # 110

carrinho.set_strategy(FreteExpresso())
print(carrinho.total(100))  # 120

carrinho.set_strategy(FreteRetirada())
print(carrinho.total(100))  # 100
```

## 🚫 Restrições

❌ Não usar `if/else` para escolher frete

❌ Não usar herança no `Carrinho`

❌ Não usar bibliotecas externas

## 💡 Dica de ouro

Strategy resolve "como fazer", não "qual objeto criar".

Se você sentir vontade de usar `if`, está no caminho errado.