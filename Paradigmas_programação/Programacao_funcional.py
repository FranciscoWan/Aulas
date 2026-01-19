# A programação funcional se concentra em funções puras e imutáveis, promovendo um estilo declarativo de programação.
# Menos dependente de ordem
# Não muda os dados

def soma(num1:int,num2:int):
    return num1 + num2

def sub(num1:int,num2:int):
    return num1 - num2

def mult(num1:int,num2:int):
    return num1 * num2

def div(num1:int,num2:int):
    return num1/num2

def menu():
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    print("Digite qual operação matemática deseja realizar, +, -, * ou /")
    opc = input("Opção: ")
    if opc == "+":
        print(soma(numero1,numero2))
    elif opc == "-":
        print(sub(numero1, numero2))
    elif opc == "*":
        print(mult(numero1,numero2))
    elif opc == "/":
        print(div(numero1,numero2))
    else:
        print("Opção inválida")


menu()

# Exemplos de linguagens com o paradigma de programação funcional.
# Haskell, Lisp, Scala, Python, Javascript

