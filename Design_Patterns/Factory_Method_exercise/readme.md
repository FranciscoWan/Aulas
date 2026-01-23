# Exercício Prático — Factory Method (Python)

## 🎯 Objetivo

Criar um sistema que delegue a criação de objetos para uma fábrica, sem que o código cliente conheça as classes concretas.

## 📌 Cenário

Você está desenvolvendo um sistema de notificações.

O sistema pode enviar notificações por diferentes canais:

- 📧 Email
- 📱 SMS
- 🔔 Push Notification

O sistema principal não deve saber qual classe concreta está sendo criada.

## ✅ Requisitos obrigatórios

### 1️⃣ Interface base

Crie uma classe abstrata `Notification` com:

- Um método abstrato `send(message)`
- Use `ABC` e `@abstractmethod`

### 2️⃣ Classes concretas

Crie as classes:

- `EmailNotification`
- `SMSNotification`
- `PushNotification`

Cada uma deve:

- Implementar o método `send`
- Apenas dar um `print`, por exemplo:
  - `"Enviando EMAIL: {message}"`

### 3️⃣ Factory Method

Crie uma classe `NotificationFactory` com:

- Um método `create_notification(type)`

Esse método deve:

- Receber uma string (`"email"`, `"sms"`, `"push"`)
- Retornar o objeto correto
- Não expor as classes concretas para quem usa

### 4️⃣ Código cliente

Crie um pequeno trecho de código que:

- Peça um tipo de notificação
- Use a factory para criar o objeto
- Chame `send()`

## 🚫 Restrições (importante)

- Não use `if/else` no código cliente
- O `if/else` só pode existir dentro da factory
- Não instancie diretamente `EmailNotification()` fora da factory

## 💡 Dica (sem entregar a solução)

Pense na Factory como um porteiro: você pede o que quer, não como aquilo é criado.