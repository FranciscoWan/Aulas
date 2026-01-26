# Interceptors e Exception Filters no NestJS - Material de Aula

## 1. Introdução – O problema real

Imagine uma API onde:

- Várias rotas podem falhar
- Erros são lançados em services
- Você quer:
  - Padronizar respostas de erro
  - Capturar exceções
  - Registrar erros no log com contexto

**Problemas comuns:**

- Se cada controller tratar erro manualmente → caos
- Se o middleware tentar capturar erro → não funciona

**Solução:** Interceptors e Exception Filters resolvem isso.

---

## 2. Visão geral do pipeline do NestJS

```
Request
   ↓
Middleware
   ↓
Guard
   ↓
Interceptor (before)
   ↓
Controller
   ↓
Service
   ↓
Interceptor (after)
   ↓
Exception Filter (se erro)
   ↓
Response
```

**Observação:** Entender essa ordem é fundamental.

---

## 3. Interceptors — o "envolvedor" da execução

### O que é um Interceptor?

Um Interceptor envolve a execução do controller/service, podendo:

- Executar código antes
- Executar código depois
- Medir tempo
- Transformar respostas
- Reagir a erros

**Observação:** Muito parecido com AOP (Aspect-Oriented Programming).

### Quando usar Interceptor?

**Casos ideais:**

- Medir tempo de execução
- Ajustar nível de log
- Transformar resposta
- Adicionar metadados

**Quando NÃO usar:**

- Não para tratar exceções finais

### Exemplo: Interceptor de tempo + status

```typescript
@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler) {
    const start = Date.now();
    const ctx = context.switchToHttp();
    const response = ctx.getResponse<Response>();

    return next.handle().pipe(
      tap(() => {
        const duration = Date.now() - start;

        console.log({
          statusCode: response.statusCode,
          responseTime: duration,
        });
      }),
    );
  }
}
```

**Este interceptor:**

- Executa antes da rota
- Executa após a resposta
- Não interfere em erro

---

## 4. Exception Filters — o tratador oficial de erros

### O que é um Exception Filter?

Um Exception Filter é responsável por capturar exceções lançadas na aplicação.

Ele:

- Intercepta erros
- Padroniza resposta
- Pode registrar logs
- Decide o que o cliente recebe

**Observação:** Ele é o último ponto do pipeline.

### Quando usar Exception Filter?

**Casos ideais:**

- Capturar exceções
- Padronizar erro
- Logar falhas
- Mapear erros técnicos → erro de negócio

### Exemplo: Filter global de erros

```typescript
@Catch()
export class AllExceptionsFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse<Response>();
    const request = ctx.getRequest<Request>();

    const status =
      exception instanceof HttpException
        ? exception.getStatus()
        : 500;

    const errorResponse = {
      statusCode: status,
      path: request.url,
      message:
        exception instanceof HttpException
          ? exception.getResponse()
          : 'Internal server error',
    };

    console.error({
      error: exception,
      request: request.url,
    });

    response.status(status).json(errorResponse);
  }
}
```

**Observação:** Aqui é onde você tem acesso total ao erro.

---

## 5. Como Interceptor + Filter trabalham juntos para logging

### Estratégia correta

- **Middleware** → cria log base
- **Interceptor** → adiciona status, tempo, sucesso
- **Exception Filter** → adiciona erro

### Exemplo de log final (erro)

```json
{
  "timestamp": "2026-01-23T14:30:00Z",
  "level": "error",
  "service": "auth-api",
  "request": {
    "method": "POST",
    "url": "/login",
    "statusCode": 401,
    "responseTime": 32
  },
  "error": {
    "name": "UnauthorizedException",
    "message": "Invalid credentials"
  }
}
```

### Onde salvar o log?

**O Exception Filter:**

- Constrói o log de erro
- Chama o LogsService
- Persiste via ORM

---

## 6. Registrando Interceptor e Filter

### Interceptor global

```typescript
app.useGlobalInterceptors(new LoggingInterceptor());
```

### Exception Filter global

```typescript
app.useGlobalFilters(new AllExceptionsFilter());
```

### Ou via provider:

```typescript
providers: [
  {
    provide: APP_FILTER,
    useClass: AllExceptionsFilter,
  },
]
```

---

## 7. Comparação rápida

| Conceito | Função | Melhor uso |
|----------|--------|------------|
| Middleware | Infra | Captura request |
| Interceptor | Fluxo | Tempo, status |
| Exception Filter | Erros | Logging de erro |

---

## Resumo final

- Middleware não vê erro
- Interceptor mede execução
- Filter captura exceção
- Logs completos exigem as 3 camadas

---

**Material preparado para fins educacionais**