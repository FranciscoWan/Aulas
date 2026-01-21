# Princípios e Boas Práticas na Programação

## 1. Introdução — Por que Boas Práticas Importam?

Muitos desenvolvedores já pensaram ou disseram:

> "Meu código funciona, então está bom."

Essa mentalidade funciona no curto prazo, mas cria problemas sérios com o tempo.

Imagine um quarto bagunçado: dá para viver nele, mas quando você precisa achar algo rápido ou outra pessoa entra no quarto, tudo vira caos.

**Objetivo das boas práticas:**

- Código legível e compreensível  
- Fácil de manter e corrigir  
- Menor quantidade de bugs  
- Facilita o trabalho em equipe  
- Permite que o sistema evolua sem virar um pesadelo

Boas práticas não são luxo — são investimento no futuro do projeto e na sua saúde mental.

---

## 2. SOLID

SOLID é um acrônimo criado por Robert C. Martin (Uncle Bob) que reúne cinco princípios muito importantes na programação orientada a objetos.

### S — Single Responsibility Principle (Princípio da Responsabilidade Única)

Uma classe deve ter apenas **uma** razão para mudar.

**Exemplo ruim:**

```python
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def validar_email(self):
        # validação complexa...
        return "@" in self.email
    
    def salvar_no_banco(self):
        # código de conexão e insert
        pass
    
    def enviar_email_boas_vindas(self):
        # código SMTP
        pass
```

**Exemplo bom:**

```python
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class UsuarioRepository:
    def salvar(self, usuario):
        # código de persistência
        pass

class EmailService:
    def enviar_boas_vindas(self, usuario):
        # código de envio de email
        pass
```

---

### O — Open/Closed Principle (Princípio Aberto/Fechado)

Entidades de software (classes, módulos, funções) devem estar abertas para extensão, mas fechadas para modificação.

**Exemplo:**

```python
# Ruim - toda vez que adicionar um desconto novo, altera a classe
class CalculadoraDesconto:
    def calcular(self, produto, tipo_cliente):
        if tipo_cliente == "normal":
            return produto.preco * 0.95
        elif tipo_cliente == "vip":
            return produto.preco * 0.80
        elif tipo_cliente == "super_vip":
            return produto.preco * 0.70
        return produto.preco

# Bom
from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def aplicar(self, preco):
        pass

class DescontoNormal(Desconto):
    def aplicar(self, preco):
        return preco * 0.95

class DescontoVIP(Desconto):
    def aplicar(self, preco):
        return preco * 0.80

class CalculadoraDesconto:
    def __init__(self, desconto: Desconto):
        self.desconto = desconto
    
    def calcular(self, preco):
        return self.desconto.aplicar(preco)
```

---

### L — Liskov Substitution Principle (Princípio da Substituição de Liskov)

Objetos de uma subclasse devem ser substituíveis por objetos da superclasse sem alterar o comportamento correto do programa.

**Exemplo ruim:**

```python
class Passaro:
    def voar(self):
        return "Voando!"

class Pinguim(Passaro):
    def voar(self):
        raise Exception("Pinguins não voam!")
```

**Exemplo bom:** Separar comportamentos que nem todos os subtipos possuem.

---

### I — Interface Segregation Principle (Princípio da Segregação de Interfaces)

É melhor ter várias interfaces pequenas e específicas do que uma interface grande e genérica.

**Exemplo:**

```python
# Ruim
from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def trabalhar(self): pass
    @abstractmethod
    def dirigir(self): pass
    @abstractmethod
    def cozinhar(self): pass

# Bom
class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self): pass

class Motorista(ABC):
    @abstractmethod
    def dirigir(self): pass

class Cozinheiro(ABC):
    @abstractmethod
    def cozinhar(self): pass

class Gerente(Trabalhador):
    def trabalhar(self):
        print("Gerenciando equipe")
```

---

### D — Dependency Inversion Principle (Princípio da Inversão de Dependência)

Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.

**Exemplo:**

```python
# Ruim
class Pedido:
    def __init__(self):
        self.pagamento = PagamentoCartaoCredito()

# Bom
class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class Pedido:
    def __init__(self, metodo_pagamento: Pagamento):
        self.metodo_pagamento = metodo_pagamento
    
    def finalizar(self, valor):
        self.metodo_pagamento.processar(valor)
```

---

## 3. DRY — Don't Repeat Yourself (Não se Repita)

Evite duplicação de código. Toda peça de conhecimento deve ter uma única representação no sistema.

**Exemplo:**

```python
# Ruim
def criar_usuario(nome, email):
    if "@" not in email:
        raise ValueError("Email inválido")
    # ...

def atualizar_usuario(nome, email):
    if "@" not in email:
        raise ValueError("Email inválido")
    # ...

# Bom
def validar_email(email: str) -> None:
    if "@" not in email:
        raise ValueError("Email inválido")

def criar_usuario(nome, email):
    validar_email(email)
    # ...

def atualizar_usuario(nome, email):
    validar_email(email)
    # ...
```

**Benefícios:** menos bugs, manutenção concentrada, código mais enxuto.

---

## 4. KISS — Keep It Simple, Stupid (Mantenha Simples)

A solução mais simples que resolve o problema corretamente é quase sempre a melhor escolha.

- **Exemplo ruim:** usar padrões de projeto complexos para somar dois números
- **Exemplo bom:** `total = a + b`

Complexidade deve ser justificada.

---

## 5. YAGNI — You Ain't Gonna Need It (Você Não Vai Precisar Disso)

Não implemente funcionalidades, abstrações ou otimizações antes de ter evidência concreta de que serão necessárias.

- **Exemplo ruim:** criar um sistema completo de plugins para um programa que só precisa gerar um relatório simples
- **Exemplo bom:** resolver o problema atual da melhor forma possível e deixar o caminho aberto para evolução futura

---

## 6. Clean Code (Código Limpo)

Código limpo é aquele que qualquer desenvolvedor consegue entender rapidamente — inclusive você daqui a 6 meses.

**Princípios importantes:**

### Nomes significativos
- `calcular_total_pedido()` > `ctp()`

### Funções pequenas e com uma única responsabilidade
- Ideal: < 20 linhas (não é regra rígida, mas guia)

### Código bem formatado
- Indentação consistente, espaçamento adequado, linhas curtas

### Comentários úteis
- **Errado:** `x += 1  # incrementa x`
- **Certo:** `x += 1  # compensa o desconto de fidelidade`

### Tratamento adequado de erros

```python
# Ruim
try:
    resultado = 100 / valor
except:
    pass

# Bom
try:
    resultado = 100 / valor
except ZeroDivisionError:
    raise ValueError("O valor não pode ser zero")
```

---

## Resumo Geral

| Princípio | Ideia central |
|-----------|---------------|
| **SOLID** | Organização e extensibilidade em OO |
| **DRY** | Evitar repetição desnecessária |
| **KISS** | Priorizar simplicidade |
| **YAGNI** | Não antecipar necessidades futuras |
| **Clean Code** | Legibilidade e compreensão |

---

## Mensagem final

Código bom não é aquele que apenas funciona hoje.

É aquele que pode ser entendido, corrigido e evoluído amanhã — com tranquilidade.

Boas práticas não são sobre perfeição. São sobre respeito:
com os outros desenvolvedores, com o cliente e com o seu eu do futuro.