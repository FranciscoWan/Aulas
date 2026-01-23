# Exercício Prático — Observer Pattern (Python)

## 🎯 Objetivo

Implementar o Observer Pattern, onde vários objetos reagem automaticamente a uma mudança de estado em outro objeto.

## 📌 Cenário

Você está criando um sistema de notificações de uma loja online.

Quando o status de um pedido muda, vários sistemas precisam ser avisados:

- Email
- SMS
- Log do sistema

O pedido não pode saber detalhes de como cada notificação funciona.

## 🧩 Estrutura esperada

### 1️⃣ Sujeito (Subject)

- Classe `Pedido`
- Responsável por:
  - Registrar observadores
  - Remover observadores
  - Notificar observadores
- Deve ter um atributo:
  - `status`

### 2️⃣ Observador (Observer)

- Interface/classe abstrata `Observer`
- Deve definir o método:
  - `update(status)`

### 3️⃣ Observadores concretos

Implemente pelo menos 3 observadores:

- `EmailNotifier`
- `SMSNotifier`
- `LogNotifier`

Cada um deve:

- Implementar `update`
- Reagir ao novo status do pedido

## ✅ Requisitos obrigatórios

- Use `abc.ABC` e `@abstractmethod`
- O `Pedido` não pode conhecer as classes concretas dos observadores
- A notificação deve acontecer automaticamente ao mudar o status
- O mesmo pedido pode ter vários observadores ao mesmo tempo

## 🧪 Teste esperado (exemplo)

Algo parecido com:

```
Status alterado para: ENVIADO
📧 Email enviado: Pedido ENVIADO
📱 SMS enviado: Pedido ENVIADO
📝 Log registrado: Pedido ENVIADO
```

## 🚫 Restrições

- Não use eventos prontos
- Não use frameworks
- Não use bibliotecas externas
- Apenas Python puro

## 💡 Dica importante

Pense no `Pedido` como um canal de notícias.

Os observadores são assinantes.

O pedido só publica, não se importa quem está ouvindo.