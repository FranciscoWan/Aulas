# Paradigmas de Programação

## O que são Paradigmas de Programação?

Paradigmas de programação são diferentes abordagens ou estilos fundamentais para estruturar e organizar código. Cada paradigma oferece uma maneira distinta de pensar sobre problemas e suas soluções.

**Analogia:** Assim como podemos construir uma casa usando diferentes técnicas (madeira, alvenaria, container), podemos resolver problemas de programação usando diferentes paradigmas.

---

## Grandes Grupos de Paradigmas

### 1. Programação Declarativa

**Conceito:** Descreve "**o que**" fazer, sem detalhar o "**como**" fazer.

**Características:**
- Foca no resultado desejado
- Abstrai os detalhes de implementação
- O programador declara o que quer alcançar
- A linguagem/framework decide como executar

**Exemplos de linguagens:**
- SQL
- HTML/CSS
- Linguagens funcionais (Haskell, Elm)
- Prolog

**Exemplo prático:**

```sql
-- SQL: Você declara O QUE quer, não COMO buscar
SELECT nome, idade 
FROM usuarios 
WHERE idade > 18;
```

Você não precisa dizer como percorrer a tabela, como comparar cada registro ou como armazenar os resultados. O banco de dados decide a melhor forma de executar.

---

### 2. Programação Imperativa

**Conceito:** Se concentra em alterar o estado do programa através de uma sequência de comandos. Foca em "**como**" fazer.

**Características:**
- As instruções são executadas de cima para baixo
- Alteradas por estruturas de controle (loops ou condicionais)
- O código é lido de cima para baixo, a menos que existam estruturas de controle
- Muda o estado do programa através de comandos

**Exemplos de linguagens:**
- Python
- C
- Pascal
- Basic

**Exemplo prático:**

```python
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]

for i in lista_numeros:
    if i % 2 == 0:
        print(f"O número {i} é par")

print("Programa encerrado")
```

O código executa linha por linha, alterando o estado conforme avança.

---

## Paradigmas Específicos

### 3. Programação Lógica

**Conceito:** Se baseia em regras e fatos declarativos. O programador define um conjunto de regras e fatos que descrevem a lógica do problema, após isso o programa encontra a solução automaticamente.

**Características:**
- Baseada em lógica formal
- Define relações e regras
- O sistema deduz as respostas
- Você não diz como procurar, o sistema deduz usando lógica

**Exemplos de linguagens:**
- Prolog
- Datalog

**Exemplo prático:**

```python
pais = [
    ("Joao", "Maria"),
    ("Maria", "Ana"),
    ("Carlos", "Pedro")
]

def eh_avo(avo, neto):
    for pai, filho in pais:
        if pai == avo:
            for pai2, filho2 in pais:
                if pai2 == filho and filho2 == neto:
                    return True
    return False

print(eh_avo("Joao", "Ana"))    # True
print(eh_avo("Carlos", "Ana"))  # False
```

Você define as relações (quem é pai de quem) e o sistema deduz quem é avô de quem.

---

### 4. Programação Funcional

**Conceito:** Se concentra em funções puras e imutáveis, promovendo um estilo declarativo de programação.

**Características:**
- Menos dependente de ordem
- Não muda os dados (imutabilidade)
- Funções são cidadãos de primeira classe
- Evita efeitos colaterais
- Funções puras (mesma entrada = mesma saída)

**Exemplos de linguagens:**
- Haskell
- Lisp
- Scala
- Python
- JavaScript

**Exemplo prático:**

```python
def soma(num1: int, num2: int):
    return num1 + num2

def sub(num1: int, num2: int):
    return num1 - num2

def mult(num1: int, num2: int):
    return num1 * num2

def div(num1: int, num2: int):
    return num1 / num2

def menu():
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    print("Digite qual operação matemática deseja realizar, +, -, * ou /")
    opc = input("Opção: ")
    
    if opc == "+":
        print(soma(numero1, numero2))
    elif opc == "-":
        print(sub(numero1, numero2))
    elif opc == "*":
        print(mult(numero1, numero2))
    elif opc == "/":
        print(div(numero1, numero2))
    else:
        print("Opção inválida")

menu()
```

As funções não alteram dados externos, apenas retornam novos valores.

---

### 5. Programação Procedural

**Conceito:** Organiza o código em funções/procedimentos para dividir tarefas.

**Características:**
- As instruções são executadas em sequência, de cima para baixo
- Chamadas de funções para agrupar lógica
- Muda as variáveis de acordo com o decorrer do código
- A ordem importa muito
- Foco em procedimentos e rotinas

**Exemplos de linguagens:**
- C
- Pascal
- Fortran
- COBOL
- BASIC

**Exemplo prático:**

```python
total = 0

def adicionar_produto(preco):
    global total
    total += preco

def aplicar_desconto():
    global total
    total *= 0.9

adicionar_produto(100)
aplicar_desconto()

print(total)  # 90.0
```

A ordem das chamadas importa. Se inverter `aplicar_desconto()` e `adicionar_produto()`, o resultado será diferente.

---

### 6. Programação Orientada a Objetos (POO)

**Conceito:** Paradigma que modela o mundo real por meio de objetos, que são instâncias de classes. Cada objeto possui atributos (dados) e métodos (funções).

**Pilares da POO:**
1. **Encapsulamento:** Proteger dados internos
2. **Herança:** Reaproveitar código de classes pai
3. **Polimorfismo:** Mesmo método, comportamentos diferentes
4. **Abstração:** Simplificar complexidade

**Exemplos de linguagens:**
- Python
- Java
- Ruby
- Kotlin
- JavaScript
- C++
- C#

**Exemplo prático:**

```python
class conta_corrente():
    # Atributos do objeto
    def __init__(self, cpf, saldo, banco):
        self.__cpf = cpf  # Atributo privado (Encapsulamento)
        self.saldo = saldo
        self.banco = banco

    # Métodos do objeto
    def adicionar_saldo(self, novo_saldo):
        self.saldo += novo_saldo
        return self.saldo

    # Encapsulamento - Acesso controlado ao CPF
    @property
    def visualizar_cpf(self):
        return self.__cpf


# Herança - conta_cnpj herda métodos e atributos de conta_corrente
class conta_cnpj(conta_corrente):
    def __init__(self, __cpf, /, saldo, banco):
        super().__init__(__cpf, saldo, banco)


# Exemplo de Abstração e Polimorfismo
class animal():
    def __init__(self):
        pass

    # Abstração - Todo animal se move
    def mover(self):
        pass


# Herança
class peixe(animal):
    def __init__(self):
        super().__init__()

    # Polimorfismo - Implementação específica
    def mover(self):
        print("Nadando")


# Herança
class anfibio(animal):
    def __init__(self):
        super().__init__()
    
    # Polimorfismo - Implementação específica
    def mover(self):
        print("Pulando")
```

**Explicação dos conceitos:**
- **Encapsulamento:** O CPF é privado (`__cpf`) e só pode ser acessado via propriedade
- **Herança:** `conta_cnpj` herda de `conta_corrente`, `peixe` e `anfibio` herdam de `animal`
- **Polimorfismo:** O método `mover()` tem implementações diferentes em cada classe
- **Abstração:** A classe `animal` define a estrutura básica que todas as subclasses seguem

---

### 7. Programação Orientada a Eventos (Reativa)

**Conceito:** A programação reativa é orientada a eventos (cliques de mouse, mudanças em dados). Aguarda um evento acontecer para poder executar determinada ação.

**Características:**
- Responde a eventos
- Como cliques de usuários
- Mudanças em dados
- Assíncrona por natureza
- Baseada em callbacks, promises ou observables

**Exemplos de linguagens/frameworks:**
- JavaScript
- RxJS (JavaScript)
- ReactiveX
- Java (com frameworks reativos)
- Python (com frameworks reativos)

**Exemplo prático em HTML:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programação Orientada a Eventos</title>
</head>
<body>
    <!-- Na programação reativa é esperado um dado ou informação 
         para que seja efetuada alguma ação. -->
    <form id="meuFormulario">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" placeholder="Digite seu nome">
        <button type="button" onclick="mostrarNome()">Enviar</button>
    </form>

    <!-- Local onde o nome aparecerá, só irá aparecer 
         após a inserção dos dados no input -->
    <p>Bem-vindo, <span id="resultado"></span>!</p>
    
    <script src="./script.js"></script>
</body>
</html>
```

**JavaScript (script.js):**

```javascript
function mostrarNome() {
    // 1. Seleciona o input e pega o valor
    var nomeDigitado = document.getElementById("nome").value;
    
    // 2. Seleciona o local onde o texto será exibido
    var localExibicao = document.getElementById("resultado");
    
    // 3. Define o texto do elemento com o nome digitado
    localExibicao.innerText = nomeDigitado;
}
```

**Explicação:**
- O programa fica "esperando" o usuário clicar no botão
- Quando o evento `onclick` acontece, a função `mostrarNome()` é executada
- Não há execução sequencial - tudo depende dos eventos do usuário

---

## Comparação Visual dos Paradigmas

| Paradigma | Foco Principal | Exemplo de Uso |
|-----------|----------------|----------------|
| **Declarativa** | O QUE fazer | SQL, HTML |
| **Imperativa** | COMO fazer passo a passo | Scripts, automações |
| **Lógica** | Regras e deduções | Sistemas especialistas, IA |
| **Funcional** | Funções puras e imutabilidade | Processamento de dados |
| **Procedural** | Procedimentos sequenciais | Programas estruturados |
| **POO** | Objetos e suas interações | Sistemas complexos, apps |
| **Eventos** | Reação a eventos | Interfaces, APIs |

---

## Paradigmas Múltiplos

**Importante:** Muitas linguagens modernas são **multiparadigma**, ou seja, suportam mais de um paradigma.

**Exemplos:**
- **Python:** Imperativa, Procedural, Funcional, POO
- **JavaScript:** Imperativa, Funcional, POO, Orientada a Eventos
- **Java:** Imperativa, POO, Funcional (a partir do Java 8)
- **Scala:** Funcional, POO

Isso permite aos desenvolvedores escolher a melhor abordagem para cada situação específica dentro do mesmo projeto.

---

## Quando usar cada Paradigma?

- **Declarativa:** Consultas a banco de dados, marcação de páginas web
- **Imperativa:** Scripts de automação, processamento sequencial
- **Lógica:** Sistemas de regras de negócio, inteligência artificial
- **Funcional:** Processamento de dados, operações matemáticas, transformações
- **Procedural:** Programas estruturados simples, scripts
- **POO:** Sistemas complexos com muitas entidades relacionadas, aplicações empresariais
- **Eventos:** Interfaces de usuário, aplicações web, sistemas assíncronos

---

## Conclusão

Não existe um paradigma "melhor" - cada um tem seus pontos fortes e fracos. O desenvolvedor moderno deve conhecer vários paradigmas e saber quando aplicar cada um para criar soluções eficientes e elegantes.