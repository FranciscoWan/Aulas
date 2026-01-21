# Solid é um acrônimo criado por Robert C. Martin (Uncle Bob) que reúne cinco princípios muito importantes na programação orientada a objetos.

# S - Single responsibility Principle (Princípio da Responsabilidade Única)
# Uma classe deve ter apenas uma responsabilidade bem definida

# Exemplo ruim 
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def validar_email(self):
        # validação complexa
        return "@" in self.email
    
    def salvar_no_banco(self):
        # código de conexão e insert
        pass

# Exemplo bom:
class Ususario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class UsuarioRepository:
    def salvar(self, usuario: Usuario):
        # código de persistência 
        pass

class EmailService:
    def enviar_boas_vindas(self, usuario: Usuario):
        # código de envio de email
        pass


# O - Open / Closed Principle (Princípio Aberto / Fechado)
# Entidades de software (classes, módulos, funções) devem estar abertas para extensão, mas fechadas para modificação.

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

# L - Liskov Substitution Principle (Princípio da Substituição de Liskov)
# Objetos de uma subclasse devem ser substituíveis por objetos da super classe sem alterar o comportamento correto do programa.

class Passaro:
    def voar(self):
        return "Voando!"

class Pinguim(Passaro):
    def voar(self):
        raise Exception("Pinguins não voam!")

# Exemplo bom: Separar comportamentos que nem todos os subtipos possuem.

class Passaro:
    def voar(self):
        return "Voando!"

class Pinguim(Passaro):
    def voar(self):
        pass

# I - Interface Segregation Principle (Princípio da Segregação de Interfaces)
# É melhor ter várias interfaces pequenas e específicas do que uma interface grande e genérica.

# Ruim
from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def trabalhar(self):
        pass
    @abstractmethod
    def dirigir(self):
        pass
    @abstractmethod
    def cozinhar(self):
        pass

# Bom
class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

class Motorista(ABC):
    @abstractmethod
    def dirigir(self):
        pass

class Cozinheiro(ABC):
    @abstractmethod
    def cozinhar(self):
        pass

class Gerente(Trabalhador):
    def trabalhar(self):
        print("Gerenciando equipe")

# D - Dependency Inversion Principle (Princípio da Inversão de Dependência)
#  Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.

# Ruim
class PagamentoCartaoCredito:
    def __init__(self):
        pass

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


