# PARTE 2 — TYPEORM NO SEU PROJETO (DO ZERO À PRODUÇÃO)

## 1️⃣ O que é o TypeORM e por que você usou

O TypeORM é um **ORM (Object-Relational Mapper)**.

O que isso significa na prática?

Ele faz a ponte entre:

- Objetos TypeScript
- Tabelas SQL

### Sem ORM:

```sql
SELECT * FROM users WHERE email = 'x';
```

### Com ORM:

```typescript
this.userRepository.findOne({ where: { email } });
```

👉 **No seu projeto, o TypeORM foi usado para:**

- Modelar o banco com Entities
- Fazer CRUD sem SQL manual
- Integrar naturalmente com NestJS
- Facilitar deploy e manutenção

---

## 2️⃣ Bancos suportados pelo TypeORM

TypeORM funciona com:

- **PostgreSQL** ✅ (ideal para produção)
- MySQL / MariaDB
- SQLite
- SQL Server

👉 **No seu caso:**

- PostgreSQL em produção
- ORM abstrai diferenças entre bancos

---

## 3️⃣ Instalação do TypeORM no NestJS

### 3.1 Dependências principais

```bash
npm install @nestjs/typeorm typeorm
```

### 3.2 Driver do banco (ex: PostgreSQL)

```bash
npm install pg
```

👉 Cada banco tem seu driver específico.

---

## 4️⃣ Integração do TypeORM no backend (AppModule)

Esse é um dos pontos mais importantes.

```typescript
// app.module.ts
import { TypeOrmModule } from '@nestjs/typeorm';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: process.env.DB_HOST,
      port: 5432,
      username: process.env.DB_USER,
      password: process.env.DB_PASS,
      database: process.env.DB_NAME,
      autoLoadEntities: true,
      synchronize: true,
    }),
  ],
})
export class AppModule {}
```

### 📌 O que cada opção faz

| Opção | Função |
|-------|--------|
| `type` | Tipo do banco |
| `host` | Endereço do banco |
| `username/password` | Credenciais |
| `database` | Nome do banco |
| `autoLoadEntities` | Carrega entities automaticamente |
| `synchronize` | Cria/atualiza tabelas |

### ⚠️ Importante

`synchronize: true` é ótimo para desenvolvimento, **não recomendado em produção real**.

---

## 5️⃣ Entities — O coração do TypeORM

### Exemplo real do seu projeto

```typescript
@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ unique: true })
  email: string;

  @Column()
  password: string;

  @Column({ default: 'guest' })
  role: Role;
}
```

### 📌 O que está acontecendo aqui

| Decorator | Função |
|-----------|--------|
| `@Entity()` | Define uma tabela |
| `@PrimaryGeneratedColumn()` | ID auto incremental |
| `@Column()` | Coluna simples |
| `unique: true` | Constraint no banco |

👉 **A entity é o contrato entre código e banco.**

---

## 6️⃣ Estrutura de pastas com TypeORM (como você fez)

Padrão profissional:

```
users/
├─ entities/
│  └─ user.entity.ts
├─ dto/
│  └─ create-user.dto.ts
├─ users.service.ts
├─ users.controller.ts
├─ users.module.ts
```

### 📌 Por que separar `entities/`?

- Evita bagunça
- Facilita leitura
- Escala melhor com múltiplas entities

---

## 7️⃣ Repositories — Acesso ao banco

No NestJS + TypeORM, você injeta o repositório:

```typescript
constructor(
  @InjectRepository(User)
  private repo: Repository<User>,
) {}
```

### O que o Repository oferece

- `find()`
- `findOne()`
- `findOneBy()`
- `save()`
- `update()`
- `delete()`
- `findAndCount()`

👉 **Você usou praticamente todos no projeto.**

---

## 8️⃣ Criando registros (CREATE)

```typescript
async create(data: CreateUserDto) {
  const user = this.repo.create(data);
  return this.repo.save(user);
}
```

### 📌 Boas práticas

- `create()` → cria instância
- `save()` → persiste no banco
- Nunca faça lógica direto no controller.

---

## 9️⃣ Buscando dados (READ)

### Buscar todos

```typescript
this.repo.find();
```

### Buscar por campo específico

```typescript
this.repo.findOne({ where: { email } });
```

### Buscar por ID

```typescript
this.repo.findOneBy({ id });
```

👉 **Você usou isso no login, users e items.**

---

## 🔍 Paginação (como você implementou)

```typescript
findAndCount({
  skip: (page - 1) * limit,
  take: limit,
  order: { id: 'ASC' },
});
```

Retorna:

```
[data, total]
```

Você transformou isso em:

```json
{
  "data": [...],
  "total": 100,
  "page": 1,
  "lastPage": 10
}
```

👉 **Padrão profissional de API.**

---

## 🔄 Atualização (UPDATE)

```typescript
await this.repo.update(id, data);
return this.repo.findOneBy({ id });
```

### Por que assim?

- `update()` não retorna o registro atualizado
- Por isso você faz um `findOne` depois

---

## ❌ Exclusão (DELETE)

```typescript
this.repo.delete(id);
```

Simples e direto.

---

## 🔟 Validação de regras com TypeORM

### Verificar email duplicado

```typescript
const existing = await this.repo.findOne({
  where: { email: data.email }
});

if (existing) {
  throw new ConflictException('Email já cadastrado');
}
```

👉 **Você fez isso corretamente no UsersService.**

---

## 1️⃣1️⃣ TypeORM + Guards + Auth

Fluxo real:

1️⃣ Guard permite acesso

2️⃣ Controller recebe

3️⃣ Service usa Repository

4️⃣ Banco responde

5️⃣ Resultado volta

**TypeORM não sabe nada de auth**

**Auth não sabe nada do banco**

👉 **Separação perfeita de responsabilidades.**

---

## 1️⃣2️⃣ Environment Variables (produção)

Em produção você usou:

```
DATABASE_URL=postgresql://user:pass@host:port/db
```

E no TypeORM:

```typescript
url: process.env.DATABASE_URL
```

👉 **Isso permite:**

- Railway
- Render
- Fly.io
- Docker

---

## 1️⃣3️⃣ O que você NÃO fez (e está tudo bem)

Por enquanto você não usou:

- Migrations
- Relations (OneToMany, ManyToOne)
- QueryBuilder

👉 **Ótimo sinal:**

Você não complicou antes da hora.

---

## ✅ O que você já domina em TypeORM

Com esse projeto você já sabe:

- ✔ Criar Entities
- ✔ Integrar ORM ao NestJS
- ✔ CRUD completo
- ✔ Paginação
- ✔ Validações no Service
- ✔ Integração com Auth
- ✔ Deploy com PostgreSQL
- ✔ Arquitetura limpa

**Isso é base sólida de backend profissional.**