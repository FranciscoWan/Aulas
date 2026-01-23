# Exercício — Padrão Facade

## 🎯 Objetivo

Aplicar o padrão Facade para simplificar o uso de vários subsistemas complexos por meio de uma única interface.

## 📌 Contexto

Você está desenvolvendo um sistema de compra online. Internamente, o sistema possui vários subsistemas, cada um com sua própria responsabilidade:

- 💳 Pagamento
- 📦 Estoque
- 🚚 Entrega
- 📧 Notificação

Cada subsistema já funciona, mas o código cliente fica confuso e acoplado, pois precisa chamar tudo manualmente.

## 🧠 Problema

Sem o Facade, o cliente teria que fazer algo assim:

```python
estoque = Estoque()
pagamento = Pagamento()
entrega = Entrega()
notificacao = Notificacao()

if estoque.verificar(produto):
    pagamento.pagar(produto)
    entrega.agendar(produto)
    notificacao.enviar()
```

👉 Seu objetivo é esconder essa complexidade usando o padrão Facade.

## 🛠️ Sua Tarefa

### 1️⃣ Crie os subsistemas abaixo

```python
class Estoque:
    def verificar(self, produto):
        return True


class Pagamento:
    def pagar(self, produto):
        print("Pagamento realizado.")


class Entrega:
    def agendar(self, produto):
        print("Entrega agendada.")


class Notificacao:
    def enviar(self):
        print("Notificação enviada ao cliente.")
```

### 2️⃣ Crie a Facade

Crie uma classe chamada `CompraFacade` que:

- Cria e controla os subsistemas internamente
- Exponha apenas um método público:

```python
realizar_compra(produto)
```

Esse método deve:

1. Verificar o estoque
2. Processar o pagamento
3. Agendar a entrega
4. Enviar a notificação

### 3️⃣ Código cliente

O cliente NÃO pode acessar diretamente os subsistemas.

Exemplo esperado:

```python
facade = CompraFacade()
facade.realizar_compra("Notebook")
```

## ✅ Resultado Esperado (saída)

```
Pagamento realizado.
Entrega agendada.
Notificação enviada ao cliente.
```

## 🧠 Perguntas para refletir (importante)

Responda mentalmente ou por escrito:

1. Qual problema o Facade resolve nesse código?
2. O Facade substitui os subsistemas?
3. O cliente sabe que existem várias classes por trás?
4. O Facade viola o princípio da responsabilidade única?