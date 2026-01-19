# Paradigma que modela o mundo real por meio de objetos, que são instâncias de classes.
# Cada objeto possui atributos (dados) e metodos (funções).

class conta_corrente():
    # Atributos do objeto
    def __init__(self, cpf, saldo, banco):
        self.__cpf = cpf
        self.saldo = saldo
        self.banco = banco

    # Métodos do objeto
    def adicionar_saldo(self, novo_saldo):
        self.saldo += novo_saldo
        return self.saldo

    # Encapsulamento
    @property
    def visualizar_cpf(self):
        return self.__cpf
    

# Herança - conta_cnpj está herdando tantos os métodos quanto os atributos de conta_corrente. 
class conta_cnpj(conta_corrente):
    def __init__(self, __cpf, /, saldo, banco):
        super().__init__(__cpf, saldo, banco)

    
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

    # Polimorfismo
    def mover():
        print("Nadando")

# Herança
class abfibio(animal):
    def __init__(self):
        super().__init__()
    
    # Polimorfismo
    def mover(self):
        print("Pulando")

# Exemplos de linguagens com paradigma de orientação de objetos:
# Python, Java, Ruby, Kotlin, Javascript

