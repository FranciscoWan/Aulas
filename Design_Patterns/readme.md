# Design Patterns (Padrões de Projeto)

## 1. Introdução aos Design Patterns

### O que são Design Patterns?

**Design Patterns (Padrões de Projeto)** são soluções reutilizáveis para problemas comuns no desenvolvimento de software.

**Importante entender:**
- **NÃO são códigos prontos** para copiar e colar
- **SÃO ideias e modelos** de solução testados e aprovados
- **NÃO são bibliotecas** ou frameworks
- **SÃO boas práticas** documentadas

### Analogia: Construção Civil

Na construção civil existem padrões estabelecidos:
- **Planta elétrica:** Ninguém reinventa como fazer instalação elétrica
- **Planta hidráulica:** Segue-se um padrão conhecido e seguro
- **Estrutura de concreto:** Há proporções e técnicas estabelecidas

**No software é a mesma coisa:**
- Sistema de login
- Criação de objetos
- Comunicação entre componentes
- Notificações de eventos

Os patterns surgem para evitar que cada desenvolvedor invente soluções ruins para problemas já resolvidos.

---

### Por que usar Design Patterns?

**Vantagens:**
- **Código organizado:** Estrutura clara e consistente
- **Facilita manutenção:** Outros devs reconhecem o padrão
- **Facilita entendimento:** Linguagem comum entre desenvolvedores
- **Reduz erros comuns:** Soluções já testadas
- **Padrão de mercado:** Usado em empresas do mundo todo
- **Acelera desenvolvimento:** Não reinventa a roda
- **Facilita comunicação:** "Vamos usar um Singleton aqui" - todos entendem

**Quando usar:**
- Problema recorrente no projeto
- Código ficando confuso ou repetitivo
- Necessidade de flexibilidade futura
- Trabalho em equipe (padronização)

**Quando NÃO usar:**
- Projeto muito simples
- Adiciona complexidade desnecessária
- Você não entende bem o pattern
- Forçar pattern onde não cabe

---

### História dos Design Patterns

Os Design Patterns foram popularizados pelo livro **"Design Patterns: Elements of Reusable Object-Oriented Software"** (1994), escrito por Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides, conhecidos como **"Gang of Four" (GoF)**.

O livro catalogou **23 padrões** divididos em 3 categorias.

---

### Classificação dos Patterns

Os Design Patterns são divididos em **3 grandes categorias:**

#### 1. Padrões Criacionais
**Objetivo:** Controlar **como objetos são criados**

Focam em mecanismos de criação de objetos de forma adequada para cada situação.

**Exemplos:**
- Singleton
- Factory Method
- Abstract Factory
- Builder
- Prototype

---

#### 2. Padrões Estruturais
**Objetivo:** Controlar **como objetos se conectam e se organizam**

Focam em como classes e objetos são compostos para formar estruturas maiores.

**Exemplos:**
- Adapter
- Facade
- Decorator
- Composite
- Proxy
- Bridge
- Flyweight

---

#### 3. Padrões Comportamentais
**Objetivo:** Controlar **como objetos se comunicam e distribuem responsabilidades**

Focam em algoritmos e atribuição de responsabilidades entre objetos.

**Exemplos:**
- Observer
- Strategy
- Command
- State
- Template Method
- Chain of Responsibility
- Iterator
- Mediator
- Memento
- Visitor

---

## 2. Padrões Criacionais

### Singleton

#### O que é Singleton?

**Singleton** garante que exista **apenas uma única instância** de uma classe em todo o sistema, e fornece um ponto de acesso global a ela.

#### Analogia

**Controle remoto da TV:**
- Só existe um controle oficial
- Todos na casa usam o mesmo
- Não faz sentido ter 10 controles fazendo coisas diferentes

**Outros exemplos do mundo real:**
- Presidente de um país (só existe um)
- Configuração do sistema
- Gerenciador de impressão
- Pool de conexões com banco de dados

---

#### Problema Sem Singleton

```
Situação: Sistema criando múltiplas conexões ao banco

Conexão 1 → Banco de Dados
Conexão 2 → Banco de Dados  
Conexão 3 → Banco de Dados
Conexão 4 → Banco de Dados

Problemas:
❌ Múltiplas conexões desperdiçam recursos
❌ Dados podem ficar inconsistentes
❌ Alto consumo de memória
❌ Dificuldade de controle
```

#### Solução com Singleton

```
Conexão Única (Singleton) → Banco de Dados
    ↑         ↑         ↑
    |         |         |
Parte A   Parte B   Parte C

Benefícios:
✔ Um único objeto compartilhado
✔ Todos acessam a mesma instância
✔ Controle centralizado
✔ Economia de recursos
```

#### Exemplo Conceitual

```
ConfiguracaoSistema (Singleton)
- tema: "escuro"
- idioma: "pt-BR"
- timezone: "America/Sao_Paulo"

Métodos:
- getInstancia() → retorna sempre a mesma instância
- setTema()
- getIdioma()

Todos os módulos do sistema acessam 
a MESMA configuração
```

#### Estrutura do Singleton

**Elementos principais:**
1. **Construtor privado:** Impede criação de novas instâncias
2. **Instância estática:** Armazena a única instância
3. **Método estático de acesso:** Retorna a instância única

#### Quando usar Singleton?

**Use quando:**
- Precisa de exatamente uma instância
- Configurações globais do sistema
- Gerenciamento de recursos compartilhados
- Logger/sistema de logs
- Cache global

**Evite quando:**
- Pode dificultar testes unitários
- Pode criar dependências ocultas
- Pode virar "variável global disfarçada"

#### Cuidados com Singleton

**Atenção:**
- Pode dificultar testes (instância compartilhada entre testes)
- Pode criar acoplamento excessivo
- Em sistemas multi-thread, precisa de sincronização
- Pode violar o Princípio da Responsabilidade Única

---

### Factory Method

#### O que é Factory Method?

**Factory Method** define uma interface para criar objetos, mas permite que as subclasses decidam qual classe instanciar. Centraliza a criação de objetos sem expor a lógica de criação.

#### Analogia

**Concessionária de carros:**
- Você pede: "Quero um carro econômico"
- A concessionária decide qual modelo entregar
- Você não monta o carro peça por peça
- Você não precisa saber como o carro é fabricado

**Outros exemplos:**
- Restaurante (você pede, a cozinha prepara)
- Fábrica de móveis (você escolhe o tipo, eles produzem)

---

#### Problema Sem Factory Method

```
Código cheio de condicionais:

if (tipo == "PIX") {
    pagamento = new PagamentoPIX()
} else if (tipo == "CARTAO") {
    pagamento = new PagamentoCartao()
} else if (tipo == "BOLETO") {
    pagamento = new PagamentoBoleto()
}

Problemas:
❌ Código repetitivo
❌ Difícil adicionar novos tipos
❌ Lógica de criação espalhada
❌ Viola o princípio Open/Closed
```

#### Solução com Factory Method

```
PagamentoFactory
- criarPagamento(tipo)

Se tipo = "PIX" → retorna PagamentoPIX
Se tipo = "CARTAO" → retorna PagamentoCartao
Se tipo = "BOLETO" → retorna PagamentoBoleto

Benefícios:
✔ Lógica centralizada
✔ Fácil adicionar novos tipos
✔ Código mais limpo
✔ Facilita manutenção
```

#### Exemplo Conceitual

```
NotificacaoFactory

Método: criarNotificacao(tipo)

Tipos disponíveis:
- "EMAIL" → NotificacaoEmail
- "SMS" → NotificacaoSMS
- "PUSH" → NotificacaoPush

Uso:
notificacao = factory.criarNotificacao("EMAIL")
notificacao.enviar("Olá!")

Adicionar novo tipo:
1. Criar classe NotificacaoWhatsApp
2. Adicionar caso na factory
3. Pronto!
```

#### Quando usar Factory Method?

**Use quando:**
- Não sabe antecipadamente os tipos exatos de objetos
- Quer delegar a lógica de criação
- Precisa centralizar criação de objetos relacionados
- Quer facilitar adição de novos tipos

**Exemplos práticos:**
- Sistema de pagamentos (múltiplos métodos)
- Sistema de notificações (email, SMS, push)
- Geração de relatórios (PDF, Excel, CSV)
- Criação de conexões (MySQL, PostgreSQL, MongoDB)

---

## 3. Padrões Estruturais

### Adapter (Adaptador)

#### O que é Adapter?

**Adapter** permite que interfaces incompatíveis trabalhem juntas. Atua como um tradutor entre duas interfaces diferentes.

#### Analogia

**Adaptador de tomada:**
- Tomada brasileira (padrão novo)
- Aparelho com plug antigo
- Adaptador conecta os dois

**Outros exemplos:**
- Adaptador HDMI → VGA
- Tradutor entre duas pessoas que falam idiomas diferentes
- Conversor de moedas

---

#### Problema

```
Situação: Sistema antigo precisa usar biblioteca nova

Sistema Legado:
- método: pagar(valor)

API Nova de Pagamento:
- método: processPayment(amount, currency)

Incompatibilidade:
❌ Nomes diferentes
❌ Parâmetros diferentes
❌ Não pode alterar o sistema legado
❌ Não pode alterar a API externa
```

#### Solução com Adapter

```
Sistema Legado → Adapter → API Nova

Adapter:
- Recebe: pagar(valor)
- Traduz para: processPayment(valor, "BRL")
- Chama a API
- Retorna resultado adaptado

Benefícios:
✔ Sistemas incompatíveis conversam
✔ Não precisa modificar código existente
✔ Reutiliza código legado
✔ Isola a complexidade de conversão
```

#### Exemplo Conceitual

```
PagamentoAdapter

Implementa interface: SistemaPagamento
- pagar(valor)

Internamente usa: APIExternaPagamento
- processPayment(amount, currency)

Código do Adapter:
pagar(valor):
    converter valor para formato da API
    chamar processPayment(valor, "BRL")
    converter resposta de volta
    retornar resultado
```

#### Quando usar Adapter?

**Use quando:**
- Integrar código legado com código novo
- Usar biblioteca externa com interface diferente
- Reutilizar classes existentes incompatíveis
- Criar camada de compatibilidade

**Exemplos práticos:**
- Integrar API de pagamento externa
- Conectar sistema legado a novo banco de dados
- Usar biblioteca com interface diferente
- Criar compatibilidade entre versões

---

### Facade (Fachada)

#### O que é Facade?

**Facade** fornece uma interface simples e unificada para um conjunto complexo de interfaces em um subsistema.

#### Analogia

**Controle remoto da TV:**
- Você aperta: botão "Netflix"
- A TV faz: 
  - Liga
  - Conecta no Wi-Fi
  - Abre o app Netflix
  - Carrega seu perfil
  - Mostra a tela inicial

Você não vê toda essa complexidade, apenas aperta um botão!

**Outros exemplos:**
- Inicializar um carro (girar a chave faz muitas coisas)
- Ligar o computador (um botão ativa todo o sistema)
- Pedir comida no delivery (app esconde toda a logística)

---

#### Problema

```
Sistema Financeiro Complexo:

Para pagar uma conta:
1. autenticacao.login()
2. validador.validarSaldo()
3. banco.verificarLimite()
4. transacao.criar()
5. transacao.processar()
6. notificacao.enviarEmail()
7. log.registrar()
8. relatorio.atualizar()

Problemas:
❌ Cliente precisa conhecer todas as classes
❌ Muitos métodos para chamar
❌ Ordem específica de chamadas
❌ Difícil usar o sistema
```

#### Solução com Facade

```
SistemaFinanceiroFacade

Método simples: pagarConta(conta, valor)

Internamente faz:
1. autenticacao.login()
2. validador.validarSaldo()
3. banco.verificarLimite()
4. transacao.criar()
5. transacao.processar()
6. notificacao.enviarEmail()
7. log.registrar()
8. relatorio.atualizar()

Benefícios:
✔ Interface simples
✔ Esconde complexidade
✔ Fácil de usar
✔ Ponto único de entrada
```

#### Exemplo Conceitual

```
MultimidiaFacade

Método: reproduzirFilme(arquivo)

Por trás faz:
- Codec.decodificar(arquivo)
- Audio.configurar()
- Video.configurar()
- Tela.ajustar()
- Som.ajustar()
- Player.iniciar()

Cliente só chama:
facade.reproduzirFilme("filme.mp4")
```

#### Quando usar Facade?

**Use quando:**
- Sistema complexo com muitas classes
- Quer simplificar interface para cliente
- Precisa de ponto único de entrada
- Quer desacoplar cliente do subsistema

**Exemplos práticos:**
- API simplificada para biblioteca complexa
- Interface unificada para sistema legado
- Simplificar acesso a frameworks complexos
- Criar camada de serviço

#### Facade vs Adapter

| Facade | Adapter |
|--------|---------|
| Simplifica interface complexa | Converte interface incompatível |
| Pode usar múltiplas classes | Geralmente adapta uma classe |
| Interface nova e simples | Mantém funcionalidade original |
| Oculta complexidade | Traduz chamadas |

---

## 4. Padrões Comportamentais

### Observer (Observador)

#### O que é Observer?

**Observer** define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.

#### Analogia

**Instagram/YouTube:**
- Você segue um canal/perfil (se inscreve)
- Quando há novo post/vídeo
- Você recebe notificação automaticamente
- Você não precisa ficar verificando

**Outros exemplos:**
- Newsletter por email
- Notificações de aplicativos
- Sistema de eventos
- Observador de bolsa de valores

---

#### Problema

```
Sistema de e-commerce:

Quando pedido é criado:
❌ Código acoplado:
    criarPedido()
    enviarEmail()
    enviarSMS()
    atualizarEstoque()
    gerarNota()

Problemas:
❌ Difícil adicionar novas notificações
❌ Código acoplado
❌ Viola responsabilidade única
❌ Difícil testar
```

#### Solução com Observer

```
Pedido (Sujeito)
- lista de observadores
- notificarObservadores()

Observadores:
- EmailObserver → envia email
- SMSObserver → envia SMS
- EstoqueObserver → atualiza estoque
- NotaFiscalObserver → gera nota

Fluxo:
1. Pedido criado
2. Pedido.notificarObservadores()
3. Cada observador faz sua ação

Benefícios:
✔ Desacoplado
✔ Fácil adicionar observadores
✔ Cada um com sua responsabilidade
✔ Notificação automática
```

#### Exemplo Conceitual

```
SistemaDeEventos

Evento: usuarioCadastrado

Observadores registrados:
1. EmailBoasVindasObserver
   → Envia email de boas-vindas

2. CupomDescontoObserver
   → Gera cupom de primeiro desconto

3. LogObserver
   → Registra no log

4. AnalyticsObserver
   → Envia dados para analytics

Quando usuário se cadastra:
→ Todos os observadores são notificados
→ Cada um executa sua ação
```

#### Estrutura do Observer

**Elementos principais:**

1. **Subject (Sujeito):**
   - Mantém lista de observadores
   - Permite adicionar/remover observadores
   - Notifica observadores quando muda

2. **Observer (Observador):**
   - Define interface de atualização
   - Recebe notificações do sujeito

3. **ConcreteSubject:**
   - Implementa sujeito específico
   - Armazena estado de interesse

4. **ConcreteObserver:**
   - Implementa observador específico
   - Mantém referência ao sujeito

#### Quando usar Observer?

**Use quando:**
- Mudança em um objeto requer mudanças em outros
- Não sabe quantos objetos precisam ser notificados
- Quer baixo acoplamento
- Sistema de eventos/notificações

**Exemplos práticos:**
- Sistema de notificações
- Event-driven architecture
- UI reativa (frameworks modernos)
- Sistema de logs distribuído
- Atualização de dashboards

---

### Strategy (Estratégia)

#### O que é Strategy?

**Strategy** permite definir uma família de algoritmos, encapsular cada um deles e torná-los intercambiáveis. Strategy permite que o algoritmo varie independentemente dos clientes que o utilizam.

#### Analogia

**GPS com opções de rota:**
- Rota mais rápida
- Rota mais econômica (menos combustível)
- Rota mais curta
- Rota sem pedágios

Você escolhe a estratégia, mas o GPS funciona igual!

**Outros exemplos:**
- Métodos de ordenação (bubble sort, quick sort, merge sort)
- Formas de pagamento (cartão, PIX, boleto)
- Algoritmos de compressão (ZIP, RAR, 7Z)

---

#### Problema

```
Código cheio de condicionais:

calcularFrete(tipo):
    if tipo == "CORREIOS":
        // lógica correios
        prazo = 10
        valor = peso * 2
    else if tipo == "TRANSPORTADORA":
        // lógica transportadora
        prazo = 5
        valor = peso * 3
    else if tipo == "RETIRADA":
        // lógica retirada
        prazo = 0
        valor = 0

Problemas:
❌ Difícil adicionar novo tipo
❌ Código crescendo muito
❌ Difícil testar cada estratégia
❌ Viola Open/Closed
```

#### Solução com Strategy

```
Interface: FreteStrategy
- calcular(pedido)

Implementações:
1. CorreiosStrategy
   - calcular(): prazo 10 dias, R$ peso*2

2. TransportadoraStrategy
   - calcular(): prazo 5 dias, R$ peso*3

3. RetiradaStrategy
   - calcular(): prazo 0, R$ 0

Contexto:
- setStrategy(strategy)
- executar()

Uso:
contexto.setStrategy(new CorreiosStrategy())
contexto.executar()

Benefícios:
✔ Fácil adicionar estratégias
✔ Cada estratégia isolada
✔ Fácil testar
✔ Troca em tempo de execução
```

#### Exemplo Conceitual

```
SistemaDePagamento

Contexto: ProcessadorPagamento
- setStrategy(strategy)
- processar()

Estratégias:

1. PagamentoPIXStrategy
   - processar(): valida chave PIX, gera QR code

2. PagamentoCartaoStrategy
   - processar(): valida cartão, conecta operadora

3. PagamentoBoletoStrategy
   - processar(): gera código de barras, define vencimento

Cliente escolhe:
processador.setStrategy(new PagamentoPIXStrategy())
processador.processar()

Fácil trocar:
processador.setStrategy(new PagamentoCartaoStrategy())
processador.processar()
```

#### Estrutura do Strategy

**Elementos principais:**

1. **Strategy (interface):**
   - Define interface comum para algoritmos

2. **ConcreteStrategy:**
   - Implementa algoritmo específico

3. **Context (Contexto):**
   - Mantém referência a Strategy
   - Permite trocar Strategy
   - Delega trabalho para Strategy

#### Quando usar Strategy?

**Use quando:**
- Múltiplos algoritmos relacionados
- Precisa trocar comportamento em runtime
- Muitos if/else ou switch/case
- Quer isolar lógica de negócio

**Exemplos práticos:**
- Cálculo de frete
- Métodos de pagamento
- Algoritmos de ordenação/busca
- Compressão de arquivos
- Validação de dados (diferentes regras)
- Formatação de output (JSON, XML, CSV)

#### Strategy vs State

| Strategy | State |
|----------|-------|
| Cliente escolhe estratégia | Objeto muda estado automaticamente |
| Estratégias independentes | Estados conhecem uns aos outros |
| Troca explícita | Transição de estados |
| Foco em algoritmos | Foco em comportamento por estado |

---

## 5. Comparação e Resumo

### Tabela Resumo dos Patterns

| Categoria | Pattern | Função | Quando Usar |
|-----------|---------|--------|-------------|
| **Criacional** | **Singleton** | Uma única instância | Configuração global, conexão BD |
| **Criacional** | **Factory Method** | Criação de objetos | Múltiplos tipos relacionados |
| **Estrutural** | **Adapter** | Traduz interfaces | Integrar código incompatível |
| **Estrutural** | **Facade** | Simplifica sistemas | Sistema complexo, muitas classes |
| **Comportamental** | **Observer** | Notificações automáticas | Sistema de eventos, notificações |
| **Comportamental** | **Strategy** | Troca de comportamento | Múltiplos algoritmos, if/else excessivo |

---

### Outros Patterns Importantes

#### Padrões Criacionais

**Builder:**
- Construir objetos complexos passo a passo
- Útil para objetos com muitos parâmetros opcionais

**Prototype:**
- Clonar objetos existentes
- Útil quando criação é custosa

**Abstract Factory:**
- Criar famílias de objetos relacionados
- Útil para temas/skins de aplicação

---

#### Padrões Estruturais

**Decorator:**
- Adicionar comportamento a objetos dinamicamente
- Útil para adicionar funcionalidades sem herança

**Proxy:**
- Controlar acesso a objetos
- Útil para lazy loading, controle de acesso

**Composite:**
- Tratar objetos individuais e composições uniformemente
- Útil para estruturas em árvore

---

#### Padrões Comportamentais

**Command:**
- Encapsular requisições como objetos
- Útil para desfazer/refazer, filas de comandos

**State:**
- Alterar comportamento quando estado interno muda
- Útil para máquinas de estado

**Template Method:**
- Definir esqueleto de algoritmo
- Útil quando algoritmo tem etapas fixas e variáveis

**Chain of Responsibility:**
- Passar requisição por cadeia de handlers
- Útil para validações em sequência

---

## 6. Boas Práticas e Dicas

### Quando NÃO usar Design Patterns

**Evite usar patterns quando:**
- Complica código simples desnecessariamente
- Você não entende bem o pattern
- Está forçando um pattern onde não se aplica
- O problema não se encaixa no pattern
- Over-engineering (engenharia excessiva)

### KISS vs Design Patterns

**KISS (Keep It Simple, Stupid):**
- Simplicidade é fundamental
- Patterns devem simplificar, não complicar
- Use apenas quando realmente necessário

### Combinando Patterns

Patterns podem ser combinados:
- **Factory + Singleton:** Factory que é Singleton
- **Observer + Strategy:** Observadores com diferentes estratégias
- **Adapter + Facade:** Facade que usa Adapters internamente

### Aprendendo Patterns

**Dicas para aprender:**
1. **Entenda o problema** antes da solução
2. **Pratique com exemplos** simples
3. **Reconheça patterns** em código existente
4. **Não decore código**, entenda o conceito
5. **Use quando necessário**, não force

### Refatoração para Patterns

**Sinais de que precisa refatorar:**
- Código duplicado
- Classes muito grandes
- Muitos if/else ou switch
- Difícil adicionar funcionalidades
- Testes difíceis

**Processo:**
1. Identifique o problema
2. Escolha o pattern adequado
3. Refatore gradualmente
4. Teste continuamente

---

## 7. Mensagem Final

### Design Patterns não são obrigatórios

**Mas sabê-los te faz pensar como um desenvolvedor profissional.**

**Benefícios de conhecer patterns:**
- Vocabulário comum com outros desenvolvedores
- Soluções testadas e comprovadas
- Código mais manutenível
- Pensamento em arquitetura
- Diferencial no mercado

### Próximos Passos

1. **Pratique cada pattern** com exemplos simples
2. **Identifique patterns** em frameworks que você usa
3. **Leia código** de projetos open source
4. **Refatore código** existente usando patterns
5. **Estude outros patterns** da GoF
6. **Explore patterns** específicos (web, mobile, microsserviços)

### Recursos para Aprofundamento

**Livros:**
- "Design Patterns" - Gang of Four (clássico)
- "Head First Design Patterns" (didático)
- "Refactoring" - Martin Fowler

**Online:**
- Refactoring.Guru (excelente site visual)
- SourceMaking
- Documentação de frameworks (veja patterns aplicados)

---

## Conclusão

Design Patterns são ferramentas poderosas no arsenal de qualquer desenvolvedor. Eles não resolvem todos os problemas, mas fornecem soluções elegantes para problemas comuns.

**Lembre-se:**
- Entenda o problema primeiro
- Escolha o pattern certo
- Não complique o simples
- Patterns servem para ajudar, não dificultar

**A verdadeira maestria** está em saber quando usar, quando não usar, e como adaptar patterns para suas necessidades específicas.