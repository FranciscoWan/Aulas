# Resolução dos exercícios Readme.md

# Exercicio 1 
# Resolução 1, utilizando a função sum()
def soma_numeros(*args) -> int:
    return sum(args)

# Reolução 2, utilizando loop
def soma_numeros_loop(*args) -> int:
    total = 0
    for num in args:
        total += num
    return total

# Exercicio 2
def mostrar_dados(**kwargs) -> None:
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_dados(nome="Maria", idade=30, cidade="São Paulo")

# Exercicio 3
def media(*args) -> float:
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

# Exercicio 4
def informacoes_pessoais(nome:str, idade:int, **informacoes): # informacoes é o nosso kwargs
    lista_informacoes = []
    lista_informacoes.append(f"Nome: {nome}")
    lista_informacoes.append(f"Idade: {idade}")
    for i in informacoes:
        lista_informacoes.append(f"{i.capitalize()}: {informacoes[i]}") 
    return lista_informacoes

print(informacoes_pessoais("João", 25, cidade="Rio de Janeiro", profissao="Engenheiro"))

# Exercicio 5
def listar_elementos(*itens): # itens é o nosso args
    for elemento in itens:
        print(elemento)

listar_elementos("maçã", "banana", "laranja")

# Repare que a o que determina se é args ou kwargs é o uso do * ou ** no parâmetro da função. E não a plavra args ou kwargs.
