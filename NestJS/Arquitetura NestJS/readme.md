# A Arquitetura do NestJS: Modules, Controllers e Services

## Introdução

O NestJS é um framework opinionado. Isso significa que ele força uma organização para evitar bagunça conforme o projeto cresce.

Pense nele como uma empresa bem organizada.

## Visão geral (o mapa mental)

```
Requisição HTTP
      │
      ▼
Controller  →  Service  →  (Banco / API externa)
      ▲
      │
    Module
```

- **Controller** → conversa com o mundo externo
- **Service** → pensa, decide e executa regras
- **Module** → organiza tudo isso

## Analogia simples (empresa)

| NestJS | Analogia |
|--------|----------|
| Controller | Recepcionista |
| Service | Especialista |
| Module | Departamento |

---

## 1. Controllers — "A porta de entrada"

### O que é um Controller?

O Controller é responsável por receber requisições HTTP e retornar respostas.

Ele:

- Lê dados da request
- Chama o service correto
- Retorna a resposta

**Observação:** Ele não toma decisões complexas.

### Responsabilidades do Controller

**O que um Controller DEVE fazer:**

- Receber requisição
- Extrair parâmetros (`body`, `params`, `query`)
- Delegar para o service
- Retornar resposta

**O que um Controller NÃO DEVE fazer:**

- Acessar banco de dados
- Conter regra de negócio

### Exemplo simples

```typescript
@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Post()
  create(@Body() data: CreateUserDto) {
    return this.usersService.createUser(data);
  }
}
```

**Observe:**

- Controller não sabe como o usuário é salvo
- Ele apenas delega

---

## 2. Services — "O cérebro da aplicação"

### O que é um Service?

O Service contém a lógica de negócio da aplicação.

Ele:

- Decide o que fazer
- Orquestra dados
- Aplica regras
- Fala com banco, APIs externas, filas, etc.

### Responsabilidades do Service

**O que um Service DEVE fazer:**

- Regras de negócio
- Orquestração de dados
- Validações complexas
- Chamadas ao ORM

**O que um Service NÃO DEVE fazer:**

- Lidar com HTTP
- Conhecer request ou response

### Exemplo simples

```typescript
@Injectable()
export class UsersService {
  createUser(data: CreateUserDto) {
    if (!data.email.includes('@')) {
      throw new Error('Email inválido');
    }

    // salvar no banco
    return { id: 1, ...data };
  }
}
```

**Observação:** Aqui é onde o sistema "pensa".

---

## 3. Modules — "O organizador"

### O que é um Module?

O Module é responsável por organizar a aplicação.

Ele:

- Agrupa controllers
- Agrupa services
- Define o que é público ou privado
- Controla dependências

### Responsabilidades do Module

**O que um Module DEVE fazer:**

- Organizar código
- Declarar dependências
- Controlar escopo
- Facilitar escalabilidade

**Observação:** Todo projeto NestJS tem pelo menos um módulo: `AppModule`.

### Exemplo simples

```typescript
@Module({
  controllers: [UsersController],
  providers: [UsersService],
})
export class UsersModule {}
```

**Este módulo diz:**

"UsersController pode usar UsersService"

---

## Como eles se conectam (fluxo real)

```
POST /users
   │
   ▼
UsersController
   │
   ▼
UsersService
   │
   ▼
Banco de Dados
```

E tudo isso existe dentro de um módulo.

---

## Injeção de Dependência (conceito-chave)

### Como o controller recebe o service?

NestJS usa Dependency Injection.

```typescript
constructor(private usersService: UsersService) {}
```

Você não cria o service manualmente. O NestJS faz isso por você.

**Isso traz:**

- Baixo acoplamento
- Facilidade de teste
- Código limpo

---

## Por que essa separação é tão importante?

### Sem essa organização, você teria:

- Controllers gigantes
- Código duplicado
- Dificuldade de teste
- Baixa escalabilidade

### Com essa organização:

- Código previsível
- Fácil manutenção
- Crescimento saudável

---

## Aplicando isso na central de logs

Como ficará o projeto:

| Camada | Responsabilidade |
|--------|------------------|
| LogsController | Recebe requisição /logs |
| LogsService | Trata, normaliza e valida logs |
| LogsModule | Organiza tudo |
| LoggingMiddleware | Captura dados automaticamente |

---

## Resumo final

### Controller
- Recebe requisições
- Retorna respostas

### Service
- Contém regras
- Executa lógica

### Module
- Organiza
- Conecta tudo

---

**Material preparado para fins educacionais**