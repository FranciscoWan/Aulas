# Resolução exercícios readme - while

# Exercício 1
cont = 1
while cont <= 10:
    print(cont)
    cont += 1

# Exercício 2
senha = ""
while senha != "1234":
    senha = input("Digite a senha: ")
print("Acesso permitido")

# Exercício 3
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        print("Programa encerrado")
        break
    elif numero % 2 == 0:
        print("Número par")
    else:
        print("Número ímpar")

# Exercício 4
while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /) ou 'sair' para encerrar: ")
    if operacao == 'sair':
        print("Calculadora encerrada")
        break
    elif operacao == '+':
        print(f"Resultado: {num1 + num2}")  
    elif operacao == '-':
        print(f"Resultado: {num1 - num2}")
    elif operacao == '*':
        print(f"Resultado: {num1 * num2}")
    elif operacao == '/':
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Erro: Divisão por zero")
    else:
        print("Operação inválida")

# Exercício 5
menu = 0
while menu != 3:
    print("Menu:")
    print("1. Dizer Olá")
    print("2. Como vai?")
    print("3. Sair")
    menu = int(input("Escolha uma opção: "))
    if menu == 1:
        print("Olá!")
    elif menu == 2:
        print("Como vai?")
    elif menu == 3:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida")

# Exercício 6
soma = 0
while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        print(f"Soma total: {soma}")
        break
    soma += numero

# Exercício 7
import random

numero_aleatorio = random.randint(1, 10)
while True:
    palpite = int(input("Adivinhe o número (entre 1 e 10): "))
    if palpite == numero_aleatorio:
        print("Parabéns!")
        break
    print("Tente novamente.")

# Exercício 8
frase = input("Digite uma frase: ")
num = 0
cont_vogal = 0
while num <= len(frase) - 1:
    if frase[num].lower() in 'aeiou':
        cont_vogal += 1
    num += 1
print(f"Número de vogais na frase {frase} é: {cont_vogal}")

# Exercício 9
num = int(input("Digite um número para calcular a tabuada: "))
cont = 1
while cont <= 10:
    print(f"{num} x {cont} = {num * cont}")
    cont += 1

# Exercício 10
soma = 0
while True:
    valor = float(input("Digite o valor do produto (0 para encerrar): "))
    if valor == 0:
        print(f"A soma total dos produtos foi de: R${soma:.2f}")
        print("Encerrando o programa.")
        break
    elif valor < 0:
        print("Valor inválido. Tente novamente.")
    else:
        soma += valor
