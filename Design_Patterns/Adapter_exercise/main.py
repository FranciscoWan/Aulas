from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor: float):
        pass

class PagamentoCartao(Pagamento):
    def pagar(self, valor: float):
        print(f"pagamento de R$ {valor} realizado com cartão.")

class PayPal:
    def make_payment(self, amount: float):
        print(f"Pagamento de R$ {amount} realizado via PayPal")

class PayPalAdapter(Pagamento):
    def __init__(self, paypal: PayPal):
        self.paypal = paypal

    def pagar(self, valor:float):
        return self.paypal.make_payment(valor)


pagamento_cartao = PagamentoCartao()
pagamento_cartao.pagar(100)

paypal = PayPal()
pagamento = PayPalAdapter(paypal)
pagamento.pagar(250)