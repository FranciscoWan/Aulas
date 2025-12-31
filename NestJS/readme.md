# PARTE 1 — BACKEND COM NESTJS (DO ZERO AO PROJETO)

## 1️⃣ O que é o NestJS e por que você usou ele

O NestJS é um framework Node.js para backend que:

- Usa TypeScript por padrão
- É inspirado em Angular
- Força arquitetura modular
- Trabalha fortemente com injeção de dependência
- Facilita escalar projetos grandes

👉 **Ele resolve um problema clássico do Node:**

*"meu projeto cresceu e virou um caos"*

### No seu projeto (TechAgro), o NestJS foi ideal porque:

- Você tem auth, users, items
- Cada parte tem responsabilidades claras
- Controle de acesso (RBAC) fica organizado
- API pronta para crescer sem refatorar tudo

---

## 2️⃣ Instalação do NestJS (do zero)

### 2.1 Instalar o Nest CLI

```bash
npm install -g @nestjs/cli
```

Isso te dá o comando:

```bash
nest
```

### 2.2 Criar o projeto

```bash
nest new backend
```

Durante a criação:

- Escolha **npm**
- O Nest cria toda a estrutura inicial

---

## 3️⃣ Estrutura inicial gerada pelo NestJS

Logo após criar o projeto, você tem algo assim:

```
backend/
├─ src/
│  ├─ app.controller.ts
│  ├─ app.service.ts
│  ├─ app.module.ts
│  └─ main.ts
├─ package.json
├─ tsconfig.json
└─ nest-cli.json
```

Agora vamos entender arquivo por arquivo, porque isso é **FUNDAMENTAL**.

---

## 4️⃣ main.ts — O ponto de entrada da aplicação

```typescript
async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
}
bootstrap();
```

📌 **Responsabilidade**

- É o entrypoint
- Sobe o servidor HTTP
- Carrega o AppModule

👉 **Pense nele como:**

*"liga a tomada do backend"*

Tudo começa aqui.

---

## 5️⃣ app.module.ts — O módulo raiz

```typescript
@Module({
  imports: [],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

📌 **Responsabilidade**

- É o módulo principal
- Importa todos os outros módulos do sistema
- O Nest monta o grafo de dependências a partir daqui

👉 **Mentalidade correta:**

Tudo no Nest é módulo

---

## 6️⃣ O conceito mais importante do NestJS: MÓDULOS

No NestJS:

- Não existe "arquivo solto"
- Tudo pertence a um Module

Exemplo do seu projeto:

```
src/
├─ auth/
├─ users/
├─ items/
```

Cada pasta dessas é um **módulo funcional**.

---

## 📁 Estrutura real do seu backend (TechAgro)

Vamos montar mentalmente a estrutura que você construiu:

```
src/
├─ auth/
│  ├─ auth.controller.ts
│  ├─ roles.guard.ts
│  ├─ roles.decorator.ts
│  └─ auth.module.ts
│
├─ users/
│  ├─ users.controller.ts
│  ├─ users.service.ts
│  ├─ entities/
│  │  └─ user.entity.ts
│  ├─ dto/
│  │  └─ create-user.dto.ts
│  └─ users.module.ts
│
├─ items/
│  ├─ items.controller.ts
│  ├─ items.service.ts
│  ├─ item.entity.ts
│  └─ items.module.ts
│
├─ app.module.ts
└─ main.ts
```

Agora vamos entender o papel de cada camada, isso é **arquitetura de verdade**.

---

## 7️⃣ Controller — A porta de entrada HTTP

Exemplo:

```typescript
@Controller('users')
export class UsersController {
```

📌 **Responsabilidade**

- Receber requisições HTTP (GET, POST, PUT, DELETE)
- Validar entrada (DTO)
- Delegar lógica para o Service

👉 **Controller NÃO contém regra de negócio**

Pense assim:

- **Controller = atendente**
- **Service = cérebro**

---

## 8️⃣ Service — Regra de negócio

Exemplo:

```typescript
@Injectable()
export class UsersService {
```

📌 **Responsabilidade**

- Criar usuários
- Validar regras (email único)
- Buscar dados
- Atualizar
- Deletar

👉 **Tudo que é lógica, decisão, regra, mora aqui.**

### No seu projeto:

- Verificação de email duplicado
- Integração com TypeORM
- Controle de CRUD

---

## 9️⃣ Entity — Mapeamento do banco de dados

```typescript
@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ unique: true })
  email: string;
}
```

📌 **Responsabilidade**

- Representa uma tabela do banco
- Cada propriedade = coluna
- Define constraints (unique, nullable, etc)

👉 **Entity = espelho do banco no código**

---

## 🔁 Como tudo se conecta (fluxo real)

**Exemplo: login com email**

1️⃣ Front faz:

```
POST /auth/login
```

2️⃣ **AuthController** recebe

3️⃣ Chama **UsersService.findOneByEmail()**

4️⃣ **UsersService** usa **UserRepository**

5️⃣ **TypeORM** consulta o banco

6️⃣ Resultado volta

7️⃣ **Controller** cria sessão

8️⃣ Resposta vai para o frontend

**Esse fluxo é padrão profissional.**

---

## 🔐 Guards e Decorators (RBAC)

### roles.decorator.ts

```typescript
@Roles('admin')
```

👉 Apenas define metadados

### roles.guard.ts

```typescript
canActivate() { ... }
```

👉 Decide se a rota pode ser acessada

Isso separa:

- **declaração da regra**
- **execução da regra**

**Arquitetura limpa ✔️**

---

## 🔟 DTOs — Validação de entrada

```typescript
export class CreateUserDto {
  @IsEmail()
  email: string;
}
```

📌 **Responsabilidade**

- Validar dados antes de entrar no sistema
- Evitar lixo no banco
- Retornar erros claros (400 Bad Request)

👉 **DTO é um contrato de entrada**

---

## 1️⃣1️⃣ Injeção de Dependência (DI)

```typescript
constructor(private service: UsersService) {}
```

Você **não cria instâncias manualmente**.

O Nest:

- Cria
- Compartilha
- Gerencia ciclo de vida

Isso:

- Facilita testes
- Evita acoplamento
- Escala melhor

---

## ✅ O que você já domina (sem perceber)

Com esse projeto você já aplicou:

- ✔ Arquitetura modular
- ✔ RBAC (controle por roles)
- ✔ Sessões HTTP
- ✔ API REST profissional
- ✔ Validação de dados
- ✔ ORM com TypeORM
- ✔ Separação de responsabilidades
- ✔ Deploy-ready backend

**Isso não é projeto iniciante.**