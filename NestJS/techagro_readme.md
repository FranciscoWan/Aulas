# TechAgro Backend

Backend completo construído com NestJS, TypeScript e TypeORM, implementando autenticação, controle de acesso baseado em roles (RBAC) e gerenciamento de usuários e itens.

## 🚀 Tecnologias

- **NestJS** - Framework Node.js modular e escalável
- **TypeScript** - Tipagem estática e segurança de código
- **TypeORM** - ORM para integração com banco de dados
- **Class Validator** - Validação de dados com decorators

## 📁 Estrutura do Projeto

```
src/
├─ auth/
│  ├─ auth.controller.ts      # Rotas de autenticação
│  ├─ roles.guard.ts           # Guard para controle de acesso
│  ├─ roles.decorator.ts       # Decorator para definir roles
│  └─ auth.module.ts           # Módulo de autenticação
│
├─ users/
│  ├─ users.controller.ts      # Rotas de usuários
│  ├─ users.service.ts         # Lógica de negócio de usuários
│  ├─ entities/
│  │  └─ user.entity.ts        # Entidade User (mapeamento do banco)
│  ├─ dto/
│  │  └─ create-user.dto.ts    # DTO para criação de usuário
│  └─ users.module.ts          # Módulo de usuários
│
├─ items/
│  ├─ items.controller.ts      # Rotas de itens
│  ├─ items.service.ts         # Lógica de negócio de itens
│  ├─ item.entity.ts           # Entidade Item
│  └─ items.module.ts          # Módulo de itens
│
├─ app.module.ts               # Módulo raiz da aplicação
└─ main.ts                     # Ponto de entrada da aplicação
```

## 🏗️ Arquitetura

O projeto segue os princípios de arquitetura do NestJS:

### **Controllers**
Responsáveis por receber requisições HTTP e delegar a lógica para os Services.

```typescript
@Controller('users')
export class UsersController {
  // Rotas HTTP (GET, POST, PUT, DELETE)
}
```

### **Services**
Contêm toda a lógica de negócio da aplicação.

```typescript
@Injectable()
export class UsersService {
  // Regras de negócio, validações, integrações
}
```

### **Entities**
Representam as tabelas do banco de dados usando TypeORM.

```typescript
@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ unique: true })
  email: string;
}
```

### **DTOs (Data Transfer Objects)**
Validam e tipam os dados de entrada.

```typescript
export class CreateUserDto {
  @IsEmail()
  email: string;
}
```

## 🔐 Sistema de Autenticação e RBAC

O projeto implementa controle de acesso baseado em roles:

### **Roles Decorator**
Define quais roles podem acessar uma rota:

```typescript
@Roles('admin')
@Get('sensitive-data')
getSensitiveData() {
  // Apenas admins podem acessar
}
```

### **Roles Guard**
Executa a verificação de permissão:

```typescript
canActivate(context: ExecutionContext): boolean {
  // Verifica se o usuário tem a role necessária
}
```

## 🔄 Fluxo de uma Requisição

Exemplo: Login de usuário

1. Frontend faz `POST /auth/login`
2. **AuthController** recebe a requisição
3. Controller chama **UsersService.findOneByEmail()**
4. Service usa **UserRepository** (TypeORM)
5. TypeORM consulta o banco de dados
6. Resultado retorna para o Service
7. Controller cria a sessão
8. Resposta é enviada ao frontend

## 🛠️ Instalação e Execução

### Pré-requisitos
- Node.js (v16+)
- npm ou yarn
- Banco de dados (PostgreSQL, MySQL, etc.)

### Instalar dependências
```bash
npm install
```

### Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USER=seu_usuario
DATABASE_PASSWORD=sua_senha
DATABASE_NAME=techagro
```

### Executar em desenvolvimento
```bash
npm run start:dev
```

A aplicação estará disponível em `http://localhost:3000`

### Build para produção
```bash
npm run build
npm run start:prod
```

## 📚 Comandos Úteis do NestJS

```bash
# Criar um novo módulo
nest generate module nome-do-modulo

# Criar um novo controller
nest generate controller nome-do-controller

# Criar um novo service
nest generate service nome-do-service

# Criar um recurso completo (module, controller, service)
nest generate resource nome-do-recurso
```

## ✨ Funcionalidades Implementadas

- ✅ Arquitetura modular e escalável
- ✅ Sistema de autenticação com sessões HTTP
- ✅ Controle de acesso baseado em roles (RBAC)
- ✅ CRUD completo de usuários
- ✅ CRUD completo de itens
- ✅ Validação de dados com DTOs
- ✅ Integração com banco de dados via TypeORM
- ✅ Injeção de dependência
- ✅ Separação clara de responsabilidades

## 🎯 Princípios Aplicados

- **Modularidade**: Cada funcionalidade em seu próprio módulo
- **Injeção de Dependência**: Gerenciamento automático de dependências
- **Separação de Responsabilidades**: Controllers, Services e Entities com papéis bem definidos
- **Validação de Dados**: DTOs garantem integridade dos dados
- **Segurança**: Guards e decorators para controle de acesso

## 📄 Licença

Este projeto está sob a licença MIT.

---

**Desenvolvido com NestJS** 🚀