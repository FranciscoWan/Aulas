# Resolução dos exercícios Readme.md

# Exercicio 1 
def saudacao():
    print("Olá, Bem-vindo!")

saudacao()

# Exercicio 2
def dobro(numero:int) -> int:
    return numero * 2

print(dobro(5))

# Exercicio 3
def media(num1:int,num2:int,num3:int) -> float:
    return (num1 + num2 + num3) / 3

print(media(5, 10, 15))

# Exercicio 4
def par_ou_impar(numero:int) -> str:
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print(par_ou_impar(7))

# Exercicio 5
def maior_numero(num1:int,num2:int) -> int:
    if num1 > num2:
        return num1
    else:
        return num2

print(maior_numero(10, 20))

# Exercicio 6
def contar_vogais(palavra:str) -> int:
    vogais = "aeiou"
    contador = 0
    for letra in palavra.lower():
        if letra in vogais:
            contador += 1
    return contador

print(contar_vogais("Exemplo"))

# Exercicio 7
def tabuada(numero:int):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    
tabuada(5)

# Exercicio 8
def fatorial(numero:int) -> int:
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

print(fatorial(5))

# Exercicio 9
def eh_primo(numero:int) -> bool:
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

print(eh_primo(17))

# Exercicio 10
def cadastro_aluno(nome:str, lista_notas:list) -> str:
    media = sum(lista_notas) / len(lista_notas)
    if media >= 7:
        return f"Aluno {nome} aprovado com média {media:.2f}"
    else:
        return f"Aluno {nome} reprovado com média {media:.2f}"

print(cadastro_aluno("Pedro", [8, 7.5, 9]))