from abc import ABC, abstractmethod

class FreteStrategy(ABC):
    @abstractmethod
    def calcular_frete(self, valor_compra):
        pass

class FreteNormal(FreteStrategy):
    def calcular_frete(self, valor_compra):
        v_frete = 0.1*valor_compra
        return v_frete+valor_compra
    
class FreteExpresso(FreteStrategy):
    def calcular_frete(self, valor_compra):
        v_frete = 0.2*valor_compra
        return v_frete+valor_compra

class FreteRetirada(FreteStrategy):
    def calcular_frete(self, valor_compra):
        return valor_compra
    
class Carrinho:
    def __init__(self, estrategia: FreteStrategy):
        self.estrategia = estrategia
    
    def total(self, valor_compra):
        return self.estrategia.calcular_frete(valor_compra)

    def set_strategy(self, estrategia:FreteStrategy):
        self.estrategia = estrategia


carrinho = Carrinho(FreteNormal())
print(carrinho.total(100)) # 110

carrinho.set_strategy(FreteExpresso())
print(carrinho.total(100)) # 120

carrinho.set_strategy(FreteRetirada())
print(carrinho.total(100)) # 100

