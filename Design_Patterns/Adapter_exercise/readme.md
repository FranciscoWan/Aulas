# Exercício prático — Adapter Pattern (Python)

## 🎯 Contexto do problema

Você está desenvolvendo um sistema de pagamentos.

O sistema principal espera trabalhar sempre com pagamentos via Cartão, usando esta interface:

```python
class PagamentoCartao:
    def pagar(self, valor: float):
        pass
```

Porém, a empresa decidiu integrar um sistema externo de pagamento via PayPal, cujo código não pode ser alterado, e que funciona assim:

```python
class PayPal:
    def make_payment(self, amount: float):
        print(f"Pagamento de R$ {amount} realizado via PayPal")
```

⚠️ Repare:

- O método se chama `make_payment`
- O parâmetro se chama `amount`
- A interface não é compatível com `PagamentoCartao`

## 🧠 Seu desafio

Você deve implementar o Adapter Pattern para que o sistema consiga usar o PayPal como se fosse um PagamentoCartao, sem alterar a classe `PayPal`.

## 📌 Requisitos do exercício

Você deve:

1️⃣ Criar uma interface base (ou classe abstrata) chamada `Pagamento`

2️⃣ Criar uma classe `PagamentoCartao` que implemente essa interface

3️⃣ Criar um Adapter chamado `PayPalAdapter`

4️⃣ O `PayPalAdapter` deve:

- Receber um objeto `PayPal`
- Traduzir a chamada `pagar(valor)` para `make_payment(amount)`

## 📂 Estrutura esperada (conceitual)

```
Pagamento (interface)
   ↑
PagamentoCartao
PayPalAdapter  ---> PayPal (sistema externo)
```

## 🧪 Exemplo de uso esperado

```python
pagamento_cartao = PagamentoCartao()
pagamento_cartao.pagar(100)

paypal = PayPal()
paypal_adapter = PayPalAdapter(paypal)
paypal_adapter.pagar(250)
```

Saída esperada:

```
Pagamento de R$ 100 realizado com cartão
Pagamento de R$ 250 realizado via PayPal
```

## 🚫 Regras importantes

❌ Não pode modificar a classe `PayPal`

❌ Não pode chamar `make_payment` diretamente fora do Adapter

✔️ O sistema deve tratar Cartão e PayPal da mesma forma

## 🧠 Dica conceitual (sem entregar a solução)

O Adapter "traduz" uma interface incompatível para uma interface que o sistema espera.

Pense nele como um adaptador de tomada 🔌.