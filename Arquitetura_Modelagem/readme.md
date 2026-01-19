# Arquitetura e Modelagem de Software

## 1. Introdução — O que é Arquitetura e Modelagem?

### Arquitetura de Software

**Arquitetura é a forma como o sistema é organizado.**

**Analogia: Uma casa**
- **Arquitetura:** Onde ficam os quartos, cozinha, banheiro
- **Não é o móvel, é a estrutura**

**No software:**
- Onde fica o código?
- Quem conversa com quem?
- Onde ficam os dados?
- Como as partes se organizam?
- Quais tecnologias serão usadas?

**Por que a arquitetura importa?**
- Facilita manutenção do código
- Permite crescimento do sistema
- Melhora o trabalho em equipe
- Evita problemas no futuro

---

### Modelagem

**Modelagem é planejar antes de construir.**

**Analogia:**
- Planta da casa antes de construir
- Cardápio antes de cozinhar
- Roteiro antes de filmar

**No software:**
- Como os dados se relacionam
- Como as telas se conectam
- Como as regras funcionam
- Qual será o fluxo do usuário

**Benefícios da modelagem:**
- Identifica problemas antes de programar
- Economiza tempo e dinheiro
- Facilita comunicação entre a equipe
- Documenta o sistema

---

## 2. MVC — Model, View e Controller

### O que é MVC?

MVC é um padrão de arquitetura que **separa o sistema em 3 responsabilidades** distintas. Essa separação organiza o código e facilita a manutenção.

### Analogia do Restaurante

| Parte | No Restaurante | No Sistema |
|-------|----------------|------------|
| **Model** | Cozinha | Dados e regras |
| **View** | Prato | Tela |
| **Controller** | Garçom | Intermediário |

---

### Model (Modelo)

**Responsabilidade:** Gerenciar dados e regras de negócio

**O que faz:**
- Representa os dados do sistema
- Define regras de validação
- Comunica com o banco de dados
- Processa a lógica de negócio

**Exemplo:**

```
Usuário
- id
- nome
- email
- senha

Métodos:
- validarEmail()
- criptografarSenha()
- salvarNoBanco()
```

**Características importantes:**
- Não sabe nada sobre tela
- Só cuida dos dados
- Pode ser reutilizado em diferentes partes do sistema
- Independente da interface

---

### View (Visão)

**Responsabilidade:** Apresentar informações ao usuário

**O que faz:**
- Exibe dados na tela
- Recebe interações do usuário
- Renderiza HTML/CSS
- Mostra formulários e botões

**Exemplo:**

```
Tela de login
- Campo email
- Campo senha
- Botão entrar
- Link "Esqueci minha senha"
```

**Características importantes:**
- Não sabe como salvar no banco
- Só exibe informações
- Foca na experiência do usuário
- Pode ter múltiplas views para o mesmo model

---

### Controller (Controlador)

**Responsabilidade:** Intermediar Model e View

**O que faz:**
- Recebe ações do usuário
- Decide o que fazer
- Coordena Model e View
- Processa requisições

**Exemplo:**

```
Usuário clicou em "Entrar"
→ Controller recebe a requisição
→ Valida os dados enviados
→ Pede ao Model para buscar usuário
→ Verifica se a senha está correta
→ Retorna resposta para a View
→ Redireciona ou mostra erro
```

**Características importantes:**
- Age como intermediário
- Coordena o fluxo da aplicação
- Não tem lógica de negócio complexa
- Delega responsabilidades

---

### Vantagens do MVC

- **Código organizado:** Cada parte tem sua responsabilidade
- **Fácil manutenção:** Mudanças isoladas não quebram tudo
- **Trabalho em equipe:** Times podem trabalhar em partes diferentes
- **Reutilização:** Models e Views podem ser reutilizados
- **Testabilidade:** Mais fácil testar cada parte separadamente
- **Muito usado:** Django, Laravel, Spring, Rails, ASP.NET

### Fluxo completo MVC

```
1. Usuário interage com a VIEW
2. VIEW envia ação para CONTROLLER
3. CONTROLLER processa e chama MODEL
4. MODEL acessa banco de dados
5. MODEL retorna dados para CONTROLLER
6. CONTROLLER envia para VIEW
7. VIEW exibe resultado para usuário
```

---

## 3. APIs — REST vs GraphQL

### O que é uma API?

**API (Application Programming Interface)** é um mensageiro entre sistemas.

**Analogia:**
- Garçom levando pedido da mesa para a cozinha
- Tomada elétrica que conecta aparelhos à energia
- Menu de restaurante que mostra o que você pode pedir

**Exemplo real:**
```
App de celular → API → Servidor → Banco de dados
```

**Por que usar APIs?**
- Separar frontend e backend
- Permitir múltiplos clientes (web, mobile, desktop)
- Facilitar integração entre sistemas
- Reutilizar funcionalidades

---

### API REST

**REST (Representational State Transfer)** é um estilo de arquitetura para APIs.

#### Como funciona

- URLs fixas para cada recurso
- Usa métodos HTTP (GET, POST, PUT, DELETE)
- Cada rota retorna um tipo de dado
- Baseado em recursos

#### Exemplo de rotas REST:

```
GET    /usuarios          → Lista todos os usuários
GET    /usuarios/1        → Busca usuário com id 1
POST   /usuarios          → Cria novo usuário
PUT    /usuarios/1        → Atualiza usuário 1
DELETE /usuarios/1        → Remove usuário 1

GET    /usuarios/1/posts  → Lista posts do usuário 1
```

#### Características

- **Simples de entender:** Rotas intuitivas
- **Muito usado:** Padrão da indústria
- **Stateless:** Cada requisição é independente
- **Cacheable:** Pode usar cache para otimizar
- **Às vezes traz dados a mais ou a menos:** Nem sempre retorna exatamente o que você quer

#### Exemplo de resposta REST:

```json
GET /usuarios/1

{
  "id": 1,
  "nome": "Ana Silva",
  "email": "ana@email.com",
  "telefone": "99999-9999",
  "endereco": "Rua X, 123",
  "cpf": "123.456.789-00",
  "dataNascimento": "1990-01-01"
}
```

Se você só precisar do nome e email, receberá todos os outros dados também.

---

### API GraphQL

**GraphQL** é uma linguagem de consulta para APIs desenvolvida pelo Facebook.

#### Como funciona

- Uma única rota (geralmente `/graphql`)
- Cliente pede exatamente o que quer
- Servidor retorna apenas o solicitado
- Baseado em um esquema de tipos

#### Exemplo de consulta GraphQL:

```graphql
{
  usuario(id: 1) {
    nome
    email
  }
}
```

#### Resposta:

```json
{
  "data": {
    "usuario": {
      "nome": "Ana Silva",
      "email": "ana@email.com"
    }
  }
}
```

Retorna **apenas** nome e email, nada mais.

#### Características

- **Flexível:** Cliente controla os dados
- **Menos dados desnecessários:** Economiza banda
- **Uma única requisição:** Pode buscar dados relacionados de uma vez
- **Tipado:** Esquema define tipos de dados
- **Mais complexo:** Curva de aprendizado maior

#### Exemplo avançado (buscando dados relacionados):

```graphql
{
  usuario(id: 1) {
    nome
    posts {
      titulo
      comentarios {
        texto
        autor {
          nome
        }
      }
    }
  }
}
```

Em REST, isso exigiria múltiplas requisições.

---

### Comparação REST vs GraphQL

| REST | GraphQL |
|------|---------|
| Várias rotas | Uma rota |
| Simples | Mais avançado |
| Muito popular | Crescendo |
| Pode retornar dados extras | Retorna só o necessário |
| Múltiplas requisições para dados relacionados | Uma requisição para tudo |
| Versionamento de API (v1, v2) | Evolução sem versões |
| Mais fácil de cachear | Cache mais complexo |

### Quando usar cada um?

**Use REST quando:**
- Sistema simples
- Equipe iniciante em APIs
- Precisa de cache agressivo
- Operações CRUD simples

**Use GraphQL quando:**
- Frontend precisa de flexibilidade
- Múltiplos clientes com necessidades diferentes
- Dados muito relacionados
- Quer evitar múltiplas requisições

---

## 4. Monolito vs Microserviços

### Arquitetura Monolítica

**Monolito:** Tudo em um único sistema.

**Analogia:**
- Uma loja com tudo dentro
- Um único prédio com todos os departamentos

#### Estrutura:

```
Aplicação Monolítica
├── Login
├── Pagamento
├── Produtos
├── Usuários
├── Relatórios
└── Notificações

→ Tudo no mesmo projeto
→ Um único banco de dados
→ Deploy único
```

#### Vantagens

- **Simples de desenvolver:** Tudo em um lugar
- **Fácil de começar:** Menos complexidade inicial
- **Deploy simples:** Um único deploy
- **Debugging mais fácil:** Stack trace completa
- **Performance:** Chamadas internas são rápidas

#### Desvantagens

- **Difícil de escalar:** Precisa escalar tudo junto
- **Se cair, cai tudo:** Sem redundância
- **Acoplamento:** Mudanças afetam todo o sistema
- **Deploy arriscado:** Um bug pode derrubar tudo
- **Tecnologia única:** Difícil mudar de tecnologia

---

### Arquitetura de Microserviços

**Microserviços:** Sistema dividido em vários serviços independentes.

**Analogia:**
- Shopping center onde cada loja é independente
- Cada departamento em um prédio separado

#### Estrutura:

```
Aplicação com Microserviços
├── Serviço de Usuários (Node.js)
├── Serviço de Pagamento (Java)
├── Serviço de Produtos (Python)
├── Serviço de Notificações (Go)
└── API Gateway (para coordenar)

→ Projetos separados
→ Bancos de dados separados
→ Deploys independentes
```

#### Vantagens

- **Escala fácil:** Escala só o que precisa
- **Times independentes:** Cada time cuida de um serviço
- **Tecnologias diferentes:** Cada serviço pode usar a melhor tecnologia
- **Falhas isoladas:** Se um cai, outros continuam
- **Deploy independente:** Atualiza sem afetar outros

#### Desvantagens

- **Mais complexo:** Muitas partes para gerenciar
- **Comunicação de rede:** Mais lento que chamadas internas
- **Debugging difícil:** Erro pode estar em múltiplos serviços
- **Mais caro:** Mais infraestrutura
- **Consistência de dados:** Difícil manter dados sincronizados

---

### Quando usar cada um?

**Use Monolito quando:**
- Está começando o projeto
- Equipe pequena
- Sistema simples
- MVP (Produto Mínimo Viável)
- Poucos usuários

**Use Microserviços quando:**
- Sistema grande e complexo
- Múltiplas equipes
- Precisa escalar partes específicas
- Alta disponibilidade é crítica
- Diferentes partes têm diferentes requisitos

### Padrão comum: Começar Monolito, evoluir para Microserviços

Muitas empresas começam com monolito e, conforme crescem, vão quebrando em microserviços. Isso é chamado de **"Strangler Pattern"**.

---

## 5. Bancos de Dados — SQL vs NoSQL

### O que é um Banco de Dados?

**Banco de dados** é onde o sistema guarda informações de forma organizada e persistente.

**Por que usar banco de dados?**
- Armazenar dados permanentemente
- Buscar informações rapidamente
- Garantir integridade dos dados
- Permitir múltiplos acessos simultâneos
- Fazer backup e recuperação

---

### SQL (Banco Relacional)

**SQL (Structured Query Language)** - Linguagem de Consulta Estruturada

#### Estrutura fixa (tabelas)

```
Tabela: USUARIOS
+----+----------+-------------------+
| id | nome     | email             |
+----+----------+-------------------+
| 1  | Ana      | ana@email.com     |
| 2  | João     | joao@email.com    |
+----+----------+-------------------+
```

#### Características

- **Estrutura rígida:** Esquema definido previamente
- **Tabelas relacionadas:** Dados conectados por chaves
- **ACID:** Garantias de consistência
  - **A**tomicidade: Tudo ou nada
  - **C**onsistência: Dados sempre válidos
  - **I**solamento: Transações independentes
  - **D**urabilidade: Dados salvos permanentemente
- **SQL padrão:** Linguagem universal

#### Exemplos de bancos SQL:

- **MySQL:** Mais popular, open source
- **PostgreSQL:** Mais recursos, open source
- **SQL Server:** Microsoft
- **Oracle:** Enterprise
- **SQLite:** Embutido, mobile

#### Exemplo de consulta SQL:

```sql
-- Buscar usuários com idade acima de 18
SELECT nome, email 
FROM usuarios 
WHERE idade > 18;

-- Relacionar tabelas
SELECT usuarios.nome, pedidos.total
FROM usuarios
INNER JOIN pedidos ON usuarios.id = pedidos.usuario_id;
```

---

### NoSQL (Banco Não Relacional)

**NoSQL (Not Only SQL)** - Não é apenas SQL

#### Estrutura flexível

```json
{
  "id": 1,
  "nome": "Ana",
  "email": "ana@email.com",
  "telefones": ["99999-9999", "88888-8888"],
  "endereco": {
    "rua": "Rua X",
    "numero": 123,
    "cidade": "São Paulo"
  }
}
```

#### Características

- **Estrutura flexível:** Sem esquema fixo
- **Escalabilidade horizontal:** Adiciona mais servidores facilmente
- **Tipos variados:** Documento, chave-valor, grafo, coluna
- **Menos relacionamentos:** Dados geralmente desnormalizados
- **BASE ao invés de ACID:**
  - **B**asically Available
  - **S**oft state
  - **E**ventually consistent

#### Tipos de NoSQL:

**1. Documento (MongoDB, CouchDB)**
```json
{
  "usuario": "Ana",
  "posts": [
    {"titulo": "Post 1", "curtidas": 10},
    {"titulo": "Post 2", "curtidas": 5}
  ]
}
```

**2. Chave-Valor (Redis, DynamoDB)**
```
"usuario:1" → {"nome": "Ana", "email": "ana@email.com"}
"sessao:abc123" → {"userId": 1, "expira": "2024-12-31"}
```

**3. Grafo (Neo4j)**
```
(Ana)-[:AMIGA_DE]->(João)
(Ana)-[:TRABALHA_EM]->(Empresa X)
```

**4. Coluna (Cassandra, HBase)**
```
Row Key: usuario:1
  nome: "Ana"
  email: "ana@email.com"
```

#### Exemplos de bancos NoSQL:

- **MongoDB:** Documentos, muito popular
- **Redis:** Chave-valor, cache
- **Firebase:** Tempo real, Google
- **Cassandra:** Colunas, escalável
- **Neo4j:** Grafos, relacionamentos complexos

---

### Comparação SQL vs NoSQL

| SQL | NoSQL |
|-----|-------|
| Estrutura fixa (esquema) | Estrutura flexível |
| Tabelas e relacionamentos | Documentos, chave-valor, etc |
| Escalabilidade vertical | Escalabilidade horizontal |
| ACID (consistência forte) | BASE (consistência eventual) |
| Melhor para dados estruturados | Melhor para dados variados |
| Consultas complexas com JOIN | Consultas simples e rápidas |
| Integridade referencial | Sem integridade automática |
| Normalização | Desnormalização |

### Quando usar SQL?

- Dados estruturados e relacionados
- Transações financeiras
- Sistemas que exigem consistência forte
- Relatórios complexos
- Dados que não mudam de estrutura frequentemente

**Exemplos:**
- Sistema bancário
- ERP
- E-commerce
- Sistema de RH

### Quando usar NoSQL?

- Dados não estruturados ou variáveis
- Grande volume de dados
- Necessidade de escalabilidade
- Leituras/escritas muito rápidas
- Estrutura de dados que muda frequentemente

**Exemplos:**
- Redes sociais
- Logs de sistema
- Cache
- Catálogo de produtos
- IoT (Internet das Coisas)

### Pode usar os dois juntos?

**Sim!** Muitos sistemas modernos usam **arquitetura poliglota** (múltiplos bancos):

```
Sistema de E-commerce:
├── PostgreSQL → Pedidos e pagamentos (precisa ACID)
├── MongoDB → Catálogo de produtos (estrutura flexível)
└── Redis → Cache e sessões (rapidez)
```

---

## 6. Modelagem de Banco de Dados

### O que é Modelar um Banco?

**Modelagem** é organizar os dados para evitar:
- Bagunça
- Repetição (redundância)
- Inconsistências
- Problemas de manutenção

**É como organizar um armário:** cada coisa em seu lugar.

---

### Exemplo Ruim (Sem Modelagem)

```
Tabela: PEDIDOS
+----+---------------+-------------------+-----------+-------+
| id | nome_cliente  | email_cliente     | produto   | preco |
+----+---------------+-------------------+-----------+-------+
| 1  | Ana Silva     | ana@email.com     | Notebook  | 3000  |
| 2  | Ana Silva     | ana@email.com     | Mouse     | 50    |
| 3  | João Santos   | joao@email.com    | Teclado   | 150   |
+----+---------------+-------------------+-----------+-------+
```

**Problemas:**
- Nome e email de Ana repetidos
- Se Ana mudar o email, precisa atualizar em vários lugares
- Desperdício de espaço
- Risco de inconsistência

---

### Exemplo Correto (Com Normalização)

```
Tabela: CLIENTES
+----+---------------+-------------------+
| id | nome          | email             |
+----+---------------+-------------------+
| 1  | Ana Silva     | ana@email.com     |
| 2  | João Santos   | joao@email.com    |
+----+---------------+-------------------+

Tabela: PEDIDOS
+----+------------+------------+-------+
| id | cliente_id | produto    | preco |
+----+------------+------------+-------+
| 1  | 1          | Notebook   | 3000  |
| 2  | 1          | Mouse      | 50    |
| 3  | 2          | Teclado    | 150   |
+----+------------+------------+-------+
```

**Benefícios:**
- Dados do cliente em um só lugar
- Fácil atualizar email
- Menos repetição
- Dados organizados

---

### Relacionamentos entre Tabelas

#### 1. Relacionamento 1 para 1 (Um para Um)

**Um registro se relaciona com apenas um registro de outra tabela.**

**Exemplo:** Usuário → Perfil

```
USUARIOS              PERFIS
+----+------+         +----+------------+-------------+
| id | nome |         | id | usuario_id | bio         |
+----+------+         +----+------------+-------------+
| 1  | Ana  |←------- | 1  | 1          | "Ola..."    |
+----+------+         +----+------------+-------------+

Cada usuário tem UM perfil
Cada perfil pertence a UM usuário
```

**Quando usar:**
- Separar dados raramente acessados
- Organizar melhor grandes tabelas
- Questões de segurança

---

#### 2. Relacionamento 1 para Muitos (Um para Vários)

**Um registro se relaciona com vários registros de outra tabela.**

**Exemplo:** Cliente → Pedidos

```
CLIENTES              PEDIDOS
+----+------+         +----+------------+-------+
| id | nome |         | id | cliente_id | total |
+----+------+         +----+------------+-------+
| 1  | Ana  |←--------| 1  | 1          | 100   |
+----+------+    ┌----| 2  | 1          | 200   |
                 └----| 3  | 1          | 50    |
                      +----+------------+-------+

Um cliente pode ter VÁRIOS pedidos
Cada pedido pertence a UM cliente
```

**É o relacionamento mais comum!**

**Outros exemplos:**
- Autor → Livros
- Categoria → Produtos
- Departamento → Funcionários

---

#### 3. Relacionamento Muitos para Muitos (Vários para Vários)

**Vários registros se relacionam com vários registros.**

**Exemplo:** Alunos ↔ Cursos

```
ALUNOS                              CURSOS
+----+------+                       +----+-----------+
| id | nome |                       | id | nome      |
+----+------+                       +----+-----------+
| 1  | Ana  |                       | 1  | Python    |
| 2  | João |                       | 2  | SQL       |
+----+------+                       +----+-----------+
     ↓                                    ↑
     └──────────→ MATRICULAS ←───────────┘
                 +----+----------+----------+
                 | id | aluno_id | curso_id |
                 +----+----------+----------+
                 | 1  | 1        | 1        |
                 | 2  | 1        | 2        |
                 | 3  | 2        | 1        |
                 +----+----------+----------+

Ana está matriculada em Python e SQL
João está matriculado em Python
Python tem Ana e João
```

**Precisa de uma tabela intermediária!**

**Outros exemplos:**
- Produtos ↔ Categorias
- Atores ↔ Filmes
- Tags ↔ Posts

---

### Normalização de Dados

**Normalização** é o processo de organizar dados para reduzir redundância.

#### Primeira Forma Normal (1FN)

**Regra:** Cada campo deve ter apenas um valor (atômico).

**Errado:**
```
CLIENTES
+----+------+-------------------------+
| id | nome | telefones               |
+----+------+-------------------------+
| 1  | Ana  | 99999-9999, 88888-8888 |
+----+------+-------------------------+
```

**Correto:**
```
CLIENTES              TELEFONES
+----+------+         +----+------------+-----------+
| id | nome |         | id | cliente_id | numero    |
+----+------+         +----+------------+-----------+
| 1  | Ana  |         | 1  | 1          | 99999-... |
+----+------+         | 2  | 1          | 88888-... |
                      +----+------------+-----------+
```

---

#### Segunda Forma Normal (2FN)

**Regra:** Estar em 1FN + não ter dependência parcial (todos os campos devem depender da chave primária completa).

---

#### Terceira Forma Normal (3FN)

**Regra:** Estar em 2FN + não ter dependência transitiva (campos não-chave não devem depender de outros campos não-chave).

**Errado:**
```
PEDIDOS
+----+------------+---------------+---------+
| id | cliente_id | cidade_client | estado  |
+----+------------+---------------+---------+

cidade depende de cliente, não de pedido!
```

**Correto:**
```
Cidade e estado devem estar na tabela CLIENTES
```

---

### Benefícios da Normalização

- **Menos repetição:** Cada dado aparece uma vez
- **Banco organizado:** Fácil entender
- **Manutenção fácil:** Atualizar em um lugar só
- **Integridade:** Menos chance de dados inconsistentes
- **Economia de espaço:** Menos redundância

### Quando desnormalizar?

Às vezes, **desnormalizar** (duplicar dados) pode ser útil para:
- **Performance:** Evitar JOINs complexos
- **Leitura rápida:** Data warehouses
- **Relatórios:** Dados agregados

**Exemplo:** Guardar o nome do cliente no pedido para consultas rápidas, mesmo que ele esteja na tabela de clientes.

---

## Fechamento - Recapitulando

### Conceitos principais

- **Arquitetura** = organização do sistema
- **Modelagem** = planejamento antes de construir

- **MVC** = separação de responsabilidades (Model, View, Controller)
- **API** = comunicação entre sistemas
- **REST vs GraphQL** = formas diferentes de pedir dados

- **Monolito vs Microserviços** = estrutura e organização do sistema
- **SQL vs NoSQL** = tipos diferentes de banco de dados
- **Modelagem de dados** = planejar como os dados serão organizados

### Dicas finais

1. **Comece simples:** Monolito, REST, SQL são ótimos pontos de partida
2. **Planeje antes:** Modelagem economiza tempo depois
3. **Escolha a ferramenta certa:** Não existe bala de prata
4. **Aprenda os fundamentos:** Padrões existem por boas razões
5. **Evolua conforme necessário:** Não precisa usar tudo de uma vez

### Próximos passos

- Praticar modelagem de dados com projetos reais
- Implementar um projeto usando MVC
- Criar uma API REST simples
- Estudar padrões de design (Design Patterns)
- Aprender sobre testes e qualidade de código