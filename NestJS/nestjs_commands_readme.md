# COMANDOS PRINCIPAIS DO NESTJS (DO ZERO AO PROFISSIONAL)

## 1️⃣ Instalação do NestJS (CLI)

### Pré-requisitos
* Node.js (>= 18 recomendado)
* npm ou yarn

### Instalar o Nest CLI globalmente

```bash
npm install -g @nestjs/cli
```

### Verificar instalação:

```bash
nest --version
```

## 2️⃣ Criando um novo projeto NestJS

```bash
nest new nome-do-projeto
```

### Exemplo real:

```bash
nest new backend
```

### Durante a criação:
* Escolha o gerenciador de pacotes (npm/yarn/pnpm)
* O Nest cria toda a estrutura base

## 3️⃣ Executando o projeto

### Modo desenvolvimento (watch)

```bash
npm run start:dev
```

### Modo padrão

```bash
npm run start
```

### Modo produção

```bash
npm run start:prod
```

### Porta padrão

```
http://localhost:3000
```

## 4️⃣ Estrutura inicial criada pelo Nest

```
src/
├─ app.controller.ts
├─ app.service.ts
├─ app.module.ts
├─ main.ts
```

### Papel de cada arquivo

| Arquivo | Responsabilidade |
|---------|------------------|
| `main.ts` | Bootstrap da aplicação |
| `app.module.ts` | Módulo raiz |
| `app.controller.ts` | Rotas iniciais |
| `app.service.ts` | Regras de negócio |
| `*.spec.ts` | Testes |

## 5️⃣ Comandos para gerar arquivos (o mais importante)

O Nest gera arquivos já integrados automaticamente ao projeto.

### 📦 Criar um módulo

```bash
nest generate module users
```

ou

```bash
nest g module users
```

Cria:

```
users/
└─ users.module.ts
```

👉 Também registra automaticamente no `AppModule`.

### 🎮 Criar um controller

```bash
nest generate controller users
```

Ou já dentro de um módulo:

```bash
nest g controller users --no-spec
```

Cria:

```
users/
└─ users.controller.ts
```

### ⚙️ Criar um service (provider)

```bash
nest generate service users
```

Cria:

```
users/
└─ users.service.ts
```

👉 O service já vem com `@Injectable()`.

### 🧩 Criar módulo + controller + service juntos

Esse é MUITO usado:

```bash
nest generate resource users
```

Durante o processo ele pergunta:
* REST API
* GraphQL
* CRUD endpoints? (sim/não)

Se escolher REST + CRUD:
* Ele gera controller, service e rotas padrão

## 6️⃣ Flags úteis nos comandos

### Não gerar arquivos de teste

```bash
nest g service users --no-spec
```

### Criar dentro de pasta específica

```bash
nest g controller auth/login
```

Cria:

```
auth/login/login.controller.ts
```

## 7️⃣ Criando Guards, Pipes, Interceptors e Decorators

### Guard

```bash
nest g guard auth/roles
```

### Pipe

```bash
nest g pipe common/validation
```

### Interceptor

```bash
nest g interceptor common/logging
```

### Decorator

```bash
nest g decorator auth/roles
```

👉 Foi exatamente assim que você criou:
* `RolesGuard`
* `Roles` decorator

## 8️⃣ Criando DTOs (Data Transfer Objects)

DTO não tem comando automático, mas padrão é:

```bash
mkdir src/users/dto
```

Arquivo:

```
create-user.dto.ts
```

👉 DTOs:
* Validam dados
* Padronizam entrada
* Trabalham com `class-validator`

## 9️⃣ Criando Entities (TypeORM)

Também não há comando nativo, padrão manual:

```bash
mkdir src/users/entities
```

Arquivo:

```
user.entity.ts
```

👉 Separação clara:
* Entity = banco
* DTO = entrada
* Service = regra
* Controller = rota

## 🔐 Criando um módulo de autenticação

```bash
nest g module auth
nest g controller auth
nest g service auth
```

Ou:

```bash
nest g resource auth
```

## 🔟 Comandos de build e produção

### Build da aplicação

```bash
npm run build
```

Gera:

```
dist/
```

### Rodar build

```bash
node dist/main.js
```

## 1️⃣1️⃣ Comandos de teste

### Testes unitários

```bash
npm run test
```

### Testes e2e

```bash
npm run test:e2e
```

## 1️⃣2️⃣ Comandos úteis do dia a dia

| Comando | Uso |
|---------|-----|
| `nest info` | Informações do ambiente |
| `nest new` | Novo projeto |
| `nest g` | Gerar arquivos |
| `nest build` | Build manual |
| `npm run start:dev` | Desenvolvimento |

## 1️⃣3️⃣ Padrão profissional que você seguiu (e está certo)

No seu projeto você:
* Usou `nest g module`
* Criou services e controllers separados
* Evitou lógica no controller
* Centralizou regras no service
* Usou guards e decorators

👉 Esse é exatamente o padrão adotado em backends NestJS profissionais.

## 🧠 Resumo mental (para entrevistas)

"Uso o Nest CLI para gerar módulos, controllers e services, mantendo uma arquitetura modular. Controllers lidam apenas com rotas, services concentram regras de negócio e o acesso ao banco é feito via TypeORM usando repositories injetados."