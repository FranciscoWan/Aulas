# Facade simplifica o uso de vários objetos

class Estoque:
    def verificar(self, produto):
        return True

class Pagamento:
    def pagar(self, produto):
        print("Pagamento realizado.")

class Entrega:
    def agendar(self, produto):
        print("Entrega agendada.")

class Notificacao:
    def enviar(self):
        print("Notificação enviada ao cliente.")

class CompraFacade:
    def __init__(self):
        self.estoque = Estoque()
        self.pagamento = Pagamento()
        self.entrega = Entrega()
        self.notificacao = Notificacao()

    def realizar_compra(self, produto):
        if self.estoque:
            self.pagamento.pagar(produto)
            self.entrega.agendar(produto)
            self.notificacao.enviar()
        else:
            print("Produto indisponível")

facade = CompraFacade()
facade.realizar_compra("Notebook")




