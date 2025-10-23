# Resolução dos exercícios Readme.md

# Exercicio 1 
def saudacao(nome:str="Maria") -> None:
    print(f"Olá, seja bem vindo(a), {nome}!")

saudacao() # Chamada sem argumento, usa o padrão "Maria"
saudacao("João") # Chamada com argumento "João"

# Exercicio 2
def divisao(num1:int,num2:int) -> float:
    if num2 == 0:
        return "Divisão por zero não é permitida."
    return num1 / num2

print(divisao(10, 2))

# Exercicio 3
def soma_quadrados(num1:int,num2:int) -> int:
    return num1**2 + num2**2

print(soma_quadrados(3, 4))

# Exercicio 4
def classificar_idade(idade:int) -> str:
    if idade < 0:
        return "Idade negativa não é válida."
    elif idade >= 18:
        return "Maior de idade"
    elif idade >= 12:
        return "Adolescente"
    else:
        return "Criança"

print(classificar_idade(15))

# Exercicio 5
def maior_numero(num1:int,num2:int,num3:int) -> int:
    return max(num1, num2, num3)

print(maior_numero(10, 25, 15))

# Exercicio 6
def analise_precos(lista_precos:list) -> tuple:
    maior = max(lista_precos)
    menor = min(lista_precos)
    media = sum(lista_precos) / len(lista_precos)
    return maior, menor, media

print(analise_precos([10.5, 23.9, 5.0, 15.75]))

# Exercicio 7
def ordenar_lista(lista_valores:list) -> list:
    return sorted(lista_valores)

print(ordenar_lista([5, 2, 9, 1, 5, 6]))

# Exercicio 8
def coletar_nomes() -> list:
    nomes = []
    for _ in range(3):
        nome = input("Digite um nome: ")
        nomes.append(nome)
    return nomes

print(coletar_nomes())

# Exercicio 9
def criar_dicionario(nome:str, lista_notas:list) -> dict:
    return {"nome": nome, "notas": lista_notas}

print(criar_dicionario("Ana", [9, 8.5, 7]))

# Exercicio 10
def menu() -> None:
    opcao = int(input("Selecione uma opção (1-4): "))
    if opcao == 1:
        print("Você selecionou 1")
    elif opcao == 2:
        print("Você selecionou 2")
    elif opcao == 3:
        print("Você selecionou 3")
    elif opcao == 4:
        print("Você selecionou 4")
    else:
        print("Opção inválida")
    
menu()