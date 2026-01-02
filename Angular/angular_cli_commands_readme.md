# PRINCIPAIS COMANDOS DO ANGULAR (ANGULAR CLI)

## 1️⃣ Instalação do Angular CLI

### Pré-requisitos
* Node.js (recomendado ≥ 18)
* npm

### Instalar Angular CLI globalmente

```bash
npm install -g @angular/cli
```

### Verificar instalação:

```bash
ng version
```

## 2️⃣ Criar um novo projeto Angular

```bash
ng new nome-do-projeto
```

Durante o setup, o CLI perguntará:
* Routing? → Yes
* Stylesheet → CSS / SCSS / etc

### Exemplo real:

```bash
ng new frontend
```

## 3️⃣ Executar o projeto Angular

### Modo desenvolvimento

```bash
ng serve
```

Ou:

```bash
npm start
```

### Definir porta

```bash
ng serve --port 4300
```

A aplicação ficará disponível em:

```
http://localhost:4200
```

## 4️⃣ Build da aplicação (produção)

```bash
ng build
```

### Build para produção

```bash
ng build --configuration production
```

Arquivos gerados em:

```
dist/
```

👉 Usado para deploy (Vercel, Netlify, etc).

## 5️⃣ Gerar componentes

### Criar um componente

```bash
ng generate component nome
```

### Forma curta:

```bash
ng g c nome
```

### Exemplo:

```bash
ng g c login
ng g c navbar
```

### Estrutura criada:

```
login/
├─ login.component.ts
├─ login.component.html
├─ login.component.css
└─ login.component.spec.ts
```

## 6️⃣ Criar componentes standalone (Angular moderno)

```bash
ng g c login --standalone
```

👉 Ideal para projetos novos (como o seu).

## 7️⃣ Gerar services

```bash
ng generate service nome
```

### Forma curta:

```bash
ng g s nome
```

### Exemplo:

```bash
ng g s auth
ng g s items
ng g s users
```

Cria:

```
auth.service.ts
```

## 8️⃣ Gerar guards (proteção de rotas)

```bash
ng generate guard nome
```

### Forma curta:

```bash
ng g guard auth
```

👉 Usado para:
* autenticação
* autorização por role
* sessão ativa

## 9️⃣ Gerar interfaces / models

```bash
ng generate interface nome
```

### Forma curta:

```bash
ng g i user
```

### Exemplo:

```typescript
export interface User {
  id: number;
  email: string;
  role: string;
}
```

## 🔟 Gerar modules (caso use módulos)

(Você usou standalone, mas é bom saber)

```bash
ng generate module nome
```

### Forma curta:

```bash
ng g m nome
```

## 1️⃣1️⃣ Gerar pipes

```bash
ng generate pipe nome
```

### Forma curta:

```bash
ng g p nome
```

Usado para:
* formatar datas
* moedas
* textos

## 1️⃣2️⃣ Gerar directives

```bash
ng generate directive nome
```

### Forma curta:

```bash
ng g d nome
```

Usado para:
* comportamentos customizados no DOM

## 1️⃣3️⃣ Listar comandos disponíveis

```bash
ng help
```

Ou ajuda de um comando específico:

```bash
ng generate --help
```

## 1️⃣4️⃣ Atualizar Angular

```bash
ng update
```

Atualizar Angular core:

```bash
ng update @angular/core @angular/cli
```

## 1️⃣5️⃣ Instalar dependências comuns no Angular

### HTTP Client

```bash
npm install @angular/common
```

### Forms

```bash
npm install @angular/forms
```

### RxJS (geralmente já vem)

```bash
npm install rxjs
```

## 1️⃣6️⃣ Rodar testes

### Testes unitários

```bash
ng test
```

### Testes end-to-end

```bash
ng e2e
```

## 🧠 Resumo rápido (cola para o dia a dia)

| Ação | Comando |
|------|---------|
| Criar projeto | `ng new app` |
| Rodar projeto | `ng serve` |
| Criar componente | `ng g c nome` |
| Criar service | `ng g s nome` |
| Criar guard | `ng g guard nome` |
| Build produção | `ng build --prod` |
| Atualizar Angular | `ng update` |