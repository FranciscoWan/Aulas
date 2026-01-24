# Middleware no NestJS - Material de Aula

## 1. Introdução

### O problema que o middleware resolve

Imagine uma API com várias rotas:

- /login
- /users
- /orders
- /health

Agora imagine que você precisa:

- Logar todas as requisições
- Medir tempo de resposta
- Capturar IP e User-Agent
- Fazer isso em todas as rotas

**Fazer isso manualmente em cada controller seria:**

- Repetitivo
- Difícil de manter
- Propenso a erro

**É aqui que entra o middleware.**

---

## 2. O que é Middleware?

### Definição simples

Middleware é uma função que intercepta uma requisição HTTP antes (e/ou depois) que ela chegue ao controller.

Ele fica no meio do caminho entre:

- O cliente (request)
- A lógica da aplicação (controller)

### Ciclo de vida de uma requisição

```
Request
   ↓
Middleware
   ↓
Guard
   ↓
Interceptor
   ↓
Controller
   ↓
Response
```

**Observação:** Hoje vamos focar somente no middleware.

### O que um middleware pode fazer

- Ler dados da requisição
- Modificar a requisição
- Executar código antes da rota
- Executar código depois da resposta
- Encerrar a requisição (em casos específicos)

### O que NÃO é papel do middleware

- Regras de negócio
- Validações complexas
- Acesso a banco de dados (em regra geral)

---

## 3. Quando usar Middleware

### Casos ideais para middleware

- Logging
- Métricas
- Autenticação simples
- Rate limiting
- Headers customizados
- Auditoria

### Quando NÃO usar middleware

- Lógica de negócio
- Validação de DTOs
- Transformação de resposta
- Controle de acesso avançado

**Observação:** No NestJS, essas responsabilidades ficam melhor em:

- Guards
- Pipes
- Interceptors

---

## 4. Middleware no NestJS — Conceito

### O que é um middleware no NestJS?

No NestJS, um middleware é:

- Uma classe
- Que implementa a interface `NestMiddleware`
- Possui um método `use()`

### Assinatura do middleware

```typescript
use(req: Request, res: Response, next: NextFunction)
```

| Parâmetro | Função |
|-----------|--------|
| req | Dados da requisição |
| res | Dados da resposta |
| next() | Continua o fluxo |

**Importante:** Se `next()` não for chamado, a requisição não continua.

---

## 5. Exemplo prático — Middleware de Logging

### Objetivo do exemplo

Capturar:

- Método HTTP
- URL
- Status code
- Tempo de resposta
- Preparar base para central de logs

### Estrutura

```
src/
 ├── middleware/
 │    └── logging.middleware.ts
 ├── app.module.ts
```

### Implementação do middleware

```typescript
import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';

@Injectable()
export class LoggingMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    const start = Date.now();

    res.on('finish', () => {
      const duration = Date.now() - start;

      const log = {
        method: req.method,
        url: req.originalUrl,
        statusCode: res.statusCode,
        duration,
        userAgent: req.headers['user-agent'],
        ip: req.ip,
      };

      console.log(log);
    });

    next();
  }
}
```

### Observações importantes

- O log é criado após a resposta
- O tempo de execução é calculado
- Nenhuma regra de negócio aqui

---

## 6. Registrando o Middleware no NestJS

### Middleware não é automático

No NestJS, você registra middleware explicitamente.

### Registro no AppModule

```typescript
import { Module, MiddlewareConsumer } from '@nestjs/common';
import { LoggingMiddleware } from './middleware/logging.middleware';

@Module({})
export class AppModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(LoggingMiddleware)
      .forRoutes('*');
  }
}
```

### Possibilidades de escopo

Você pode aplicar middleware:

- Para todas as rotas
- Para rotas específicas
- Para métodos HTTP específicos

**Exemplo:**

```typescript
.forRoutes('users')
```

---

## 7. Conexão com a Central de Logs

### Papel do middleware no projeto

No projeto da central de logs, o middleware será responsável por:

- Captar dados da requisição
- Criar o log base
- Enviar esse log para:
  - Service layer
  - ORM
  - Banco de dados

### Evolução natural do middleware

**Hoje:**

```typescript
console.log(log);
```

**Amanhã:**

```typescript
this.logService.create(log);
```

**Depois:**

- Fila
- Batch insert
- Observabilidade completa

---

## Resumo

O middleware no NestJS é uma ferramenta poderosa para interceptar requisições HTTP e executar código transversal à aplicação. Ele deve ser usado para tarefas como logging, métricas e autenticação simples, mantendo a separação de responsabilidades clara e evitando misturar lógica de negócio com infraestrutura.

---

**Material preparado para fins educacionais**