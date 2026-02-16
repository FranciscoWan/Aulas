# ESTUDO COMPLETO DO FRONTEND COM ANGULAR

### Bibliotecas Angular
- [ngBootstrap](https://ng-bootstrap.github.io/)
- [ngxBootstrap](https://valor-software.com/ngx-bootstrap/components)
- [PrimeBlocks](https://primeblocks.org/free)
- [Nebular](https://akveo.github.io/nebular/docs/components/components-overview)
- [Modelo-Calendário](https://www.htmlelements.com/angular/demos/scheduler/overview/)


## 1️⃣ O que é Angular (visão arquitetural)

Angular é um framework frontend completo, opinionado, baseado em:

* Componentes
* Modules (ou standalone components)
* Services (injeção de dependência)
* Roteamento
* Reactive Forms / Template Forms
* Change Detection
* RxJS (Observables)

👉 Diferente de React, Angular já entrega arquitetura, padrões e ferramentas prontas.

No seu projeto, você usou:

* Angular moderno (standalone components)
* Services para comunicação com API
* Guards e controle de sessão
* Separação clara de responsabilidades

## 2️⃣ Instalação do Angular (CLI)

### Pré-requisitos

* Node.js (>= 18)
* npm

### Instalar Angular CLI globalmente

```bash
npm install -g @angular/cli
```

### Verificar instalação:

```bash
ng version
```

## 3️⃣ Criando um novo projeto Angular

```bash
ng new frontend
```

Durante a criação:

* Standalone components → YES
* Routing → YES
* CSS → CSS

👉 Exatamente o padrão moderno que você utilizou.

## 4️⃣ Executando o projeto

```bash
ng serve
```

Ou:

```bash
npm start
```

Acesso:

```
http://localhost:4200
```

## 5️⃣ Estrutura inicial do projeto Angular

Após criar o projeto:

```
frontend/
├─ angular.json
├─ package.json
├─ tsconfig.json
└─ src/
   ├─ main.ts
   ├─ index.html
   ├─ styles.css
   └─ app/
```

## 6️⃣ Arquivos principais (núcleo do Angular)

### 🔹 main.ts

```typescript
bootstrapApplication(AppComponent, appConfig);
```

👉 Ponto de entrada da aplicação
👉 Inicializa o Angular
👉 Injeta providers globais (router, http, etc)

### 🔹 index.html

```html
<app-root></app-root>
```

👉 HTML base
👉 Onde o Angular "monta" a aplicação

### 🔹 styles.css

👉 CSS global
👉 Afeta TODA a aplicação
👉 Você usou isso para:

* layout
* navbar
* scroll global

## 7️⃣ Pasta app/ (o coração do frontend)

```
app/
├─ app.component.ts
├─ app.routes.ts
├─ auth/
├─ users/
├─ items/
├─ navbar/
├─ home/
```

Essa estrutura não é aleatória.
Ela representa domínios da aplicação.

## 8️⃣ Componentes (base do Angular)

### O que é um Component?

Um component é composto por:

* .ts → lógica
* .html → template
* .css → estilo

### Exemplo real seu:

```
login/
├─ login.ts
├─ login.html
├─ login.css
```

Component é responsável por:

* Interação com o usuário
* Estado da tela
* Eventos (click, submit, etc)

👉 Nunca regra de negócio pesada

## 9️⃣ Standalone Components (Angular moderno)

Você usou:

```typescript
@Component({
  standalone: true,
  imports: [CommonModule, FormsModule],
})
```

Vantagens:

* Não precisa de módulos (NgModule)
* Importa apenas o que usa
* Mais performático
* Arquitetura mais simples

👉 Esse é o padrão atual do Angular.

## 🔟 Services (camada de comunicação)

Exemplo:

```
auth.service.ts
items.service.ts
users.service.ts
```

Service é responsável por:

* Comunicação com API
* Regras reutilizáveis
* Estado compartilhado
* Sessão do usuário

Exemplo real seu:

```typescript
this.http.post('http://localhost:3000/auth/login', ...)
```

👉 O componente consome
👉 O service executa

## 1️⃣1️⃣ Injeção de dependência

Angular injeta automaticamente:

```typescript
private http = inject(HttpClient);
```

Ou:

```typescript
constructor(private auth: AuthService) {}
```

👉 Você não cria instâncias manualmente
👉 Angular gerencia tudo

## 1️⃣2️⃣ Roteamento (app.routes.ts)

Arquivo:

```
app.routes.ts
```

Exemplo:

```typescript
{
  path: 'items',
  component: ItemsListComponent,
}
```

Responsabilidade:

* Definir URLs
* Proteger rotas
* Lazy loading (se necessário)

👉 No seu projeto:

* /login
* /home
* /items
* /users/manage

## 1️⃣3️⃣ Guards (proteção de rotas)

Você usou:

* Role guard
* Sessão ativa

Guards decidem:

```
Pode ou não acessar essa rota?
```

Exemplo conceitual:

```typescript
if (!logged) redirect('/login')
```

👉 Segurança no frontend não substitui backend, mas melhora UX.

## 1️⃣4️⃣ Forms no Angular

Você usou Reactive Forms no login:

```typescript
this.fb.group({
  email: ['', Validators.required],
  password: ['', Validators.required],
});
```

E Template Forms no manage users:

```html
<input [(ngModel)]="newUser.email">
```

### Resumo:

| Tipo | Quando usar |
|------|-------------|
| Reactive Forms | Login, validação forte |
| Template Forms | Formulários simples |

## 1️⃣5️⃣ Comunicação com Backend (HTTP)

Angular usa:

```
HttpClient
```

Sempre com:

```typescript
{ withCredentials: true }
```

👉 Necessário porque você usa sessão (cookie) no backend.

### Fluxo:

```
Component → Service → HttpClient → Backend → Response
```

## 1️⃣6️⃣ Navbar + estado global

Navbar:

* Lê sessão
* Mostra nome/email
* Mostra opções conforme role

AuthService:

* Guarda role
* Guarda email
* Centraliza autenticação

👉 Padrão de state management simples e eficiente.

## 🔁 Como tudo se conecta (fluxo real)

```
LoginComponent
   ↓
AuthService
   ↓
Backend /auth/login
   ↓
Sessão criada
   ↓
Navbar atualiza
   ↓
Rotas protegidas liberadas
```

## 🧠 Resumo mental 

"No frontend usamos Angular moderno com standalone components, arquitetura baseada em componentes e services, comunicação via HttpClient, controle de sessão com cookies, guards para proteção de rotas e formulários reativos para autenticação."
