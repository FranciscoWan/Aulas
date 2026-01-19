# A programação funcional se concentra em funções puras e imutáveis, promovendo um estilo declarativo de programação.
# Procedural é o mesmo paradigma de funcional? 

# Função sem parâmetro:
def menu():
    print('''
Digite a opção desejada
1 - Adicionar preço
2 - Calcular total
3 - Finalizar compra''')
    opcao = input("Digite a opção desejada: ")

menu()

# Função com parâmetro:
def soma(num1:int,num2:int):
    return num1+num2

# Exemplos de linguagens com o paradigma de programação funcional.
# Haskell, Lisp, Scala, Python, Javascript

