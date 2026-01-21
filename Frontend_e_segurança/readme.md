# Frontend e Segurança

## 1. Introdução – Frontend e Segurança

### O que é Frontend?

**Frontend** é a parte visual do sistema, a camada de apresentação com a qual o usuário interage diretamente.

**Elementos do frontend:**
- Botões
- Formulários
- Textos
- Imagens
- Navegação
- Animações
- Feedback visual

### Tecnologias comuns

**HTML (HyperText Markup Language):**
- Estrutura da página
- Define elementos e conteúdo
- Semântica do documento

**CSS (Cascading Style Sheets):**
- Estilo e apresentação
- Layout e posicionamento
- Cores, fontes, espaçamentos
- Responsividade

**JavaScript:**
- Comportamento e interatividade
- Manipulação do DOM
- Requisições ao backend
- Validações
- Lógica da interface

### Por que segurança no frontend é importante?

O frontend é a **primeira linha de defesa** do sistema.

**O frontend recebe dados do usuário:**
- Formulários de cadastro
- Campos de busca
- Upload de arquivos
- Inputs diversos

**O usuário pode tentar:**
- Enviar dados maliciosos
- Burlar regras de validação
- Injetar scripts
- Manipular o DOM
- Interceptar requisições
- Explorar vulnerabilidades

### Princípio fundamental

**Frontend não é confiável.**

- Qualquer coisa no frontend pode ser manipulada
- Usuário tem controle total sobre o navegador
- DevTools permite alterar código em tempo real
- Validações frontend podem ser desabilitadas

**Segurança começa no frontend, mas não termina nele.**

A verdadeira segurança está no backend, mas o frontend deve:
- Prevenir erros comuns
- Melhorar experiência do usuário
- Dificultar ataques básicos
- Validar dados antes de enviar

---

## 2. DOM – Document Object Model

### O que é o DOM?

**DOM** é a representação do HTML em forma de **árvore de objetos** que o JavaScript consegue acessar e modificar.

O navegador transforma o HTML em uma estrutura de dados que pode ser manipulada programaticamente.

### Analogia: Árvore genealógica

Imagine o HTML como uma árvore genealógica onde cada tag é um **nó**, tags podem ter **filhos**, um **pai** e **irmãos**.

### Estrutura do DOM

```
Document
└── html
    ├── head
    │   └── title
    │       └── "Minha Página"
    └── body
        ├── h1
        │   └── "Título"
        └── p
            └── "Parágrafo"
```

### Exemplo de manipulação

```html
<button id="btn">Clique aqui</button>
<p id="texto">Texto original</p>
```

```javascript
const botao = document.getElementById("btn");
const texto = document.getElementById("texto");

botao.addEventListener("click", () => {
  texto.textContent = "Texto alterado!";
  alert("Botão clicado!");
});
```

O JavaScript conversa com o HTML através do DOM.

### O que podemos fazer com o DOM?

- **Ler dados:** Obter valores de campos e textos
- **Alterar textos:** Modificar conteúdo de elementos
- **Alterar estilos:** Mudar cores, tamanhos, visibilidade
- **Criar elementos:** Adicionar novos elementos à página
- **Remover elementos:** Deletar elementos da página

### DOM e segurança

**Importante entender:**

**Alterar DOM ≠ alterar regras do backend**
- Mudar texto "Admin" no frontend não te torna admin
- Esconder botão no frontend não impede acesso
- Validação apenas no DOM pode ser burlada

**Usuário pode manipular o DOM via DevTools:**
- Inspecionar elementos
- Editar HTML/CSS ao vivo
- Executar JavaScript no console
- Alterar valores de campos
- Remover validações

**Conclusão:** Nunca confie apenas no frontend. Sempre valide no backend.

---

## 3. Responsividade – Mobile First

### O que é responsividade?

**Responsividade** é a capacidade de um site se adaptar a diferentes tamanhos de tela e dispositivos.

**Dispositivos comuns:**
- **Mobile:** Celulares (320px - 480px)
- **Tablet:** Tablets (481px - 768px)
- **Desktop:** Computadores (769px - 1024px)
- **Wide:** Telas grandes (1025px+)

### O que é Mobile First?

**Mobile First** é uma abordagem de design onde você começa desenvolvendo para dispositivos móveis e depois adapta para telas maiores.

**Fluxo Mobile First:**
```
Mobile → Tablet → Desktop
(começa pequeno, expande)
```

### Por que Mobile First?

**Dados de uso:**
- Mais de 60% dos acessos à internet são via mobile
- Tendência crescente de uso mobile
- Google prioriza sites mobile-friendly (SEO)

**Vantagens de design:**
- Obriga a priorizar conteúdo essencial
- Layout mais simples e limpo
- Foco na experiência do usuário
- Performance otimizada

**Vantagens técnicas:**
- Mais fácil expandir do que reduzir
- Menos sobrescrita de CSS
- Código mais limpo
- Melhor performance em dispositivos móveis

### Exemplo CSS – Mobile First

```css
/* Base: Mobile (sem media query) */
body {
  font-size: 16px;
  padding: 10px;
}

.container {
  display: flex;
  flex-direction: column;
}

/* Tablet: Telas médias */
@media (min-width: 768px) {
  body {
    font-size: 18px;
  }
  
  .container {
    flex-direction: row;
  }
}

/* Desktop: Telas grandes */
@media (min-width: 1024px) {
  body {
    font-size: 20px;
    padding: 30px;
  }
}
```

**Note:** Usamos `min-width` (não `max-width`) para construir de baixo para cima.

### Boas práticas de design responsivo

**Layout:**
- Layout em coluna única no mobile
- Use unidades relativas (%, em, rem, vw, vh)

**Interação:**
- Botões grandes e espaçados (mínimo 44x44px)
- Evite hover como funcionalidade principal
- Use gestos mobile (swipe, pinch)

**Conteúdo:**
- Texto legível sem zoom (mínimo 16px)
- Parágrafos curtos
- Imagens otimizadas e responsivas

**Navegação:**
- Menu hamburger para mobile
- Navegação simplificada

### Meta tag viewport

**Essencial para responsividade:**
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Sem essa tag, sites podem não funcionar corretamente em mobile.

---

## 4. Gerenciamento de Estado

### O que é "estado"?

**Estado** é a informação atual da aplicação em um determinado momento. É a "memória" da aplicação - dados que mudam conforme o usuário interage.

### Exemplos de estado

**Autenticação:**
- Usuário está logado?
- Qual o nome do usuário?
- Qual o nível de permissão?

**Carrinho de compras:**
- Quais produtos foram adicionados?
- Quantidades de cada item
- Valor total

**Interface:**
- Tema claro ou escuro?
- Modal está aberto ou fechado?
- Qual aba está ativa?

**Filtros e busca:**
- Termo de busca atual
- Filtros aplicados
- Ordenação selecionada

### Exemplo simples

```javascript
let usuarioLogado = false;

function login() {
  usuarioLogado = true;
}

function logout() {
  usuarioLogado = false;
}
```

Isso é estado.

### Onde o estado pode ser armazenado?

**1. Variáveis JavaScript (memória):**
- Perde ao recarregar página
- Rápido e simples
- Ideal para estado temporário

**2. LocalStorage:**
- Persiste após fechar navegador
- Específico por domínio
- Máximo ~5-10MB

**3. SessionStorage:**
- Persiste durante a sessão (aba aberta)
- Perde ao fechar aba

**4. Cookies:**
- Enviados automaticamente ao servidor
- Importante para autenticação
- Máximo ~4KB

**5. Frameworks (React, Vue, Angular):**
- Gerenciamento reativo
- Sincronização automática com UI

**6. Gerenciadores de estado (Redux, Vuex, MobX):**
- Estado centralizado
- Ideal para apps complexos

### Problema sem gerenciamento adequado

**Estado espalhado:**
- Dados duplicados em vários lugares
- Inconsistências entre componentes

**Bugs difíceis de rastrear:**
- Múltiplas fontes de verdade
- Difícil debugar

**Tela fora de sincronia:**
- Dados mudam, mas interface não atualiza

### Segurança e estado

**Nunca confie em:**
- Dados do localStorage
- Variáveis do frontend
- Cookies manipuláveis

**Sempre:**
- Valide no backend
- Não armazene dados sensíveis no frontend
- Não confie em permissões apenas no frontend

**Backend sempre valida!**

---

## 5. Autenticação vs Autorização

### Autenticação: Quem é você?

**Autenticação** é o processo de verificar a identidade do usuário.

**Responde:** Este usuário é quem diz ser?

**Métodos comuns:**
- Login e senha
- Token JWT (JSON Web Token)
- OAuth (Google, Facebook, GitHub)
- Autenticação multifator (MFA)

**Exemplo:**
```javascript
async function login(email, senha) {
  const resposta = await fetch("/api/login", {
    method: "POST",
    body: JSON.stringify({ email, senha })
  });
  
  const dados = await resposta.json();
  
  if (dados.token) {
    localStorage.setItem("token", dados.token);
    return true;
  }
  return false;
}
```

### Autorização: O que você pode fazer?

**Autorização** é o processo de verificar se o usuário tem permissão para executar determinada ação.

**Responde:** Este usuário pode fazer isso?

**Níveis de permissão comuns:**
- Usuário comum
- Moderador
- Admin

### Analogia: Prédio comercial

**Autenticação:** Mostrar documento na portaria
- Você prova quem é
- Entra no prédio

**Autorização:** Acessar salas específicas
- Funcionário comum: apenas seu andar
- Gerente: vários andares
- Admin: todos os andares + sala de servidores

### Exemplo prático

```
Usuário logado? → Autenticação
Pode deletar usuário? → Autorização
```

### Erro comum: Autorização apenas no frontend

**NUNCA FAÇA ISSO:**
```javascript
if (usuario.role === "admin") {
  // Mostra botão deletar
  botaoDeletar.onclick = async () => {
    await fetch(`/api/usuarios/${id}`, { method: "DELETE" });
  };
}
```

Usuário pode executar no console e deletar qualquer usuário!

**Forma correta:**
- Frontend: controla interface (UX)
- Backend: valida permissões de verdade

### Resumo

| Autenticação | Autorização |
|--------------|-------------|
| Quem é você? | O que pode fazer? |
| Login, senha, token | Permissões, papéis |
| Acontece uma vez (login) | Acontece em cada ação |
| Prova identidade | Prova direito |

**Ambos devem ser validados no backend, sempre.**

---

## 6. CORS (Cross-Origin Resource Sharing)

### O que é CORS?

**CORS** é uma política de segurança implementada pelos navegadores para controlar quais sites podem fazer requisições a uma API.

É um mecanismo que restringe requisições HTTP entre diferentes origens.

### O que é "origem" (origin)?

**Origem** é a combinação de:
- Protocolo (http/https)
- Domínio (exemplo.com)
- Porta (80, 443, 3000, etc)

**Exemplos:**
```
https://site.com:443          → Origem A
https://api.site.com:443      → Origem B (subdomínio diferente)
http://site.com:80            → Origem C (protocolo diferente)
https://site.com:3000         → Origem D (porta diferente)
```

### Problema: Same-Origin Policy

Por padrão, navegadores bloqueiam requisições entre origens diferentes.

**Exemplo bloqueado:**

Frontend em: `http://meusite.com`
Backend em: `http://api.com`

Bloqueado por padrão.

### Por que essa proteção existe?

**Cenário de ataque sem CORS:**
1. Você está logado no seu banco (`banco.com`)
2. Visita site malicioso (`sitemalicioso.com`)
3. Site malicioso faz requisição para `banco.com/transferir`
4. Sem CORS, requisição seria bem-sucedida (você está autenticado)
5. Dinheiro transferido sem seu conhecimento

**Com CORS:** Navegador bloqueia requisição.

### Solução: Backend permite origem

O backend precisa permitir explicitamente:

```javascript
// Node.js (Express)
app.use(cors({
  origin: "https://meusite.com"
}));
```

**Header enviado pelo backend:**
```
Access-Control-Allow-Origin: https://meusite.com
```

### Importante: CORS é proteção do navegador

**CORS não protege a API diretamente:**
- Ferramentas como Postman, cURL ignoram CORS
- Apenas navegadores respeitam CORS
- Servidor ainda precisa de autenticação/autorização própria

**Analogia:**
- CORS = porteiro do prédio (primeira barreira)
- Autenticação/Autorização = fechadura da porta (barreira real)

### Boas práticas CORS

**1. Nunca use `*` em produção:**
```javascript
// Ruim
Access-Control-Allow-Origin: *

// Bom
Access-Control-Allow-Origin: https://meusite.com
```

**2. Liste apenas origens confiáveis**

**3. Minimize headers e métodos expostos**

---

## 7. Sanitização de Dados

### O que é sanitização?

**Sanitização** é o processo de limpar e validar dados recebidos do usuário para prevenir ataques e garantir integridade dos dados.

**Objetivo:** Remover ou escapar caracteres perigosos que possam ser usados para atacar o sistema.

### Tipos de ataques sem sanitização

**1. XSS (Cross-Site Scripting):**
Injeção de código JavaScript malicioso

**2. SQL Injection:**
Injeção de comandos SQL

**3. Command Injection:**
Injeção de comandos do sistema

**4. Path Traversal:**
Acesso a arquivos não autorizados

### XSS - Cross-Site Scripting

**O ataque mais comum no frontend.**

**Exemplo de ataque:**

Usuário digita no campo de comentário:
```html
<script>alert("hackeado")</script>
```

Sem sanitização, código é executado no navegador de todos que veem o comentário.

**Consequências:**
- Roubo de cookies e tokens
- Redirecionamento para sites maliciosos
- Modificação da página
- Roubo de dados do usuário

### Prevenindo XSS

**Use textContent ao invés de innerHTML:**

```javascript
// PERIGOSO - executa scripts
element.innerHTML = inputUsuario;

// SEGURO - trata como texto
element.textContent = inputUsuario;
```

### Boas práticas de sanitização

**No frontend:**
- Validar formato (email, telefone, CPF)
- Limitar tamanho de texto
- Bloquear caracteres especiais quando desnecessários
- Usar textContent para exibição

**No backend:**
- Validar todos os dados recebidos
- Sanitizar antes de salvar no banco
- Usar prepared statements (SQL)
- Escapar output ao exibir
- Validar tipos de dados

### Validação vs Sanitização

**Validação:** Verifica se dado está correto
```javascript
if (!email.includes("@")) {
  return "Email inválido";
}
```

**Sanitização:** Limpa/transforma o dado
```javascript
const emailLimpo = email.trim().toLowerCase();
```

**Ambos são necessários!**

---

## Revisão Final

### Conceitos-chave

**DOM:**
- É a ponte entre JavaScript e HTML
- Permite manipular página dinamicamente
- Pode ser alterado pelo usuário (DevTools)

**Mobile First:**
- Começa pelo celular, expande para desktop
- Maioria dos acessos são mobile
- Obriga design simples e focado

**Estado:**
- É a "memória" da aplicação
- Dados que mudam durante uso
- Precisa ser gerenciado adequadamente

**Autenticação vs Autorização:**
- Autenticação: Quem é você?
- Autorização: O que pode fazer?
- Sempre validar no backend

**CORS:**
- Controla acesso entre diferentes origens
- Proteção implementada pelo navegador
- Backend precisa permitir explicitamente

**Sanitização:**
- Limpa dados do usuário
- Previne ataques XSS, SQL Injection
- Validar no frontend E no backend

---

## Mensagem Final

**Frontend é a porta de entrada do sistema.**

**Segurança começa nele, mas só funciona com backend bem feito.**

**Lembre-se:**
- Nunca confie apenas no frontend
- Usuário pode manipular tudo no navegador
- Backend sempre valida tudo
- Segurança é responsabilidade compartilhada
- Frontend melhora UX, backend garante segurança