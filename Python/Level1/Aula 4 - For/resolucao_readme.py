# Resolução exercícios readme - while

# Atividade 1
for i in range(1, 6):
    print(i)

# Atividade 2
# Resolução 1 -
for i in range(0, 21, 2): #Começa em 0, vai até 20 e incrementa de 2 em 2
    print(i)

# Resolução 2 -
for i in range(21):
    if i % 2 == 0: #Verifica se o número é par (Através do módulo %)
        print(i)

# Aividade 3
palavra = input("Digite uma palavra: ")
for letra in palavra:
    print(letra)

# Atividade 4 - Resultado esperado: 55
soma = 0
for i in range(1, 11):   
    soma += i  #soma = soma + i
print(f"A soma dos números de 1 a 10 é: {soma}")

# Atividade 5
palavra = input("Digite uma palavra: ")
cont_vogal = 0
for letra in palavra:
    if letra.lower() in 'aeiou':  #Verifica se a letra é uma vogal
        cont_vogal += 1
print(f"Número de vogais na palavra: {cont_vogal}")

# Atividade 6
for i in range(1, 11):
    print(i*i) #Imprime o quadrado dos números de 1 a 10

# Atividade 7
compras = ["arroz", "feijão", "leite", "pão"]
for item in compras:
    print(item)

# Atividade 8
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("-"*20)  #Linha em branco entre as tabelas de multiplicação

# Atividade 9
for i in range(10, 0, -1):
    print(i)
print("Feliz Ano Novo!")

# Atividade 10
# Resoluçaõ 1 -
for i in range(3, 31, 3):
    print(i)

# Resolução 2 -
for i in range(1, 31):
    if i % 3 == 0: #Verifica se o número é múltiplo de 3 utilizando o módulo %
        print(i)
