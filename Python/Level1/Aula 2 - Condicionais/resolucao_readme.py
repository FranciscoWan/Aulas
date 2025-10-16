# Resolução dos exercícios readme.md

# Exercício 1
num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"{num} é par.")
else:
    print(f"{num} é ímpar.")

# Exercício 2
idade = int(input("Digite uma idade: "))
if idade < 18:
    print("Menor de idade.")
else:
    print("Maior de idade.")

# Exercício 3 - Aninhamento de if (condicionais dentro de condicionais)
nota = float(input("Digite uma nota (0 a 10): "))
if 0 <= nota <= 10:  # Verifica se a nota está no intervalo válido (entre 0 e 10)
    if nota >= 7:
        print("Aprovado.")
    elif 5 <= nota < 7:  # Verifica se a nota está entre 5 (inclusive) e 7 (exclusivo). Pode ser escrito também como: elif nota >= 5 and nota < 7: 
        print("Recuperação.")
    else:
        print("Reprovado.")
else:
    print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")

# Exercício 4 
idade = int(input("Digite uma idade: "))
if idade < 0: # Verifica se a idade é negativa
    print("Idade inválida.")    
elif idade < 12: # Verifica se a idade é menor que 12
    print("Criança.")   
elif idade < 18: # Verifica se a idade é menor que 18
    print("Adolescente.")   
elif idade >= 18: # Verifica se a idade é maior ou igual a 18
    print("Adulto.")

# Exercício 5
nome_usuario = str(input("Digite o nome de usuário: "))
if nome_usuario == "admin": # Verifica se o nome_usuario é igual a "admin", comparação de strings
    print("Bem-vindo, administrador!")
else:
    print("Usuário comum.")

# Exercício 6
numero = int(input("Digite um número e tente acertar: "))
if numero == 10:
    print("Acertou o número mágico!")
elif numero > 10:
    print("Muito alto!")
else:
    print("Muito baixo!")

# Exercício 7
numero = int(input("Digite um número: "))
if numero > 0:
    print("Positivo.")
elif numero < 0:
    print("Negativo.")
else:
    print("Zero.")

# Exercício 8
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print(f"{num1} é maior que {num2}.")
elif num1 < num2:
    print(f"{num2} é maior que {num1}.")
else:
    print("Os dois números são iguais.")

# Exercício 9 
temperatura = float(input("Digite a temperatura em Celsius: "))
if temperatura < 0:
    print("Congelando.")
elif 0 <= temperatura <= 20:
    print("Frio.")
elif 21 <= temperatura <= 30:
    print("Agradável.")
else:
    print("Quente.")

# Exercício 10
letra = str(input("Digite uma letra: ")).lower() # Converte a letra para minúscula para facilitar a comparação
if letra in 'aeiou': # Verifica se a letra está na string 'aeiou'
    print("Vogal.")
else:
    print("Consoante.")
