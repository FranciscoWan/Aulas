# Resolução dos exercícios Readme.md

# Exercicio 1 
lista_numerica = []
for i in range(5):
    valor = int(input("Digite um numero: "))
    lista_numerica.append(valor)

print(lista_numerica)

# Exercicio 2
# Resolução 1
lista_numerica = []
soma = 0
for i in range(5):
    valor = int(input("Digite um numero: "))
    lista_numerica.append(valor)
for numero in lista_numerica:
    soma += numero
print(f"A soma dos valores da lista {lista_numerica} é: {soma}")

# Resolução 2
lista_numerica = []
for i in range(5):
    valor = int(input("Digite um numero: "))
    lista_numerica.append(valor)
soma = sum(lista_numerica)
print(f"A soma dos valores da lista {lista_numerica} é: {soma}")

# Exercicio 3
# Resolução 1
maior = -999
lista_numeros = [1,2,3,4,5]
for numero in lista_numeros:
    if numero > maior:
        maior = numero
print(f"O maior numero da lista {lista_numeros} é: {maior}")

# Resolução 2
lista_numeros = [1,2,3,4,5]
maior = max(lista_numeros)
print(f"O maior numero da lista {lista_numeros} é: {maior}")

# Exercicio 4
lista_par = []
for i in range(10):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        lista_par.append(numero)
print(f"A quantidade de numeros pares digitados foi: {len(lista_par)}")

# Exercicio 5
lista_nomes = []
for i in range(3):
    nome = input("Digite um nome: ")
    lista_nomes.append(nome)
nome_verificar = input("Digite um nome para verificar se está na lista: ")
if nome_verificar in lista_nomes:
    print(f"O nome {nome_verificar} está na lista.")
else:   
    print(f"O nome {nome_verificar} não está na lista.")

# Exercicio 6
lista_frutas = []
for i in range(5):
    fruta = input("Digite o nome de uma fruta: ")
    lista_frutas.append(fruta)
fruta_remover = input("Digite o nome de uma fruta para remover da lista: ")
if fruta_remover in lista_frutas:
    lista_frutas.remove(fruta_remover)
    print(f"A fruta {fruta_remover} foi removida da lista.")
else:
    print(f"A fruta {fruta_remover} não está na lista.")

print(f"A lista atualizada de frutas é: {lista_frutas}")

# Exercicio 7
lista_numeros = []
for i in range(6):
    numero = int(input("Digite um numero: "))
    lista_numeros.append(numero)
lista_crescente = sorted(lista_numeros)
lista_decrescente = sorted(lista_numeros, reverse=True)
print(f"Lista em ordem crescente: {lista_crescente}")
print(f"Lista em ordem decrescente: {lista_decrescente}")

# Exercicio 8
lista_numeros = []
for i in range(8):
    numero = int(input("Digite um numero: "))
    lista_numeros.append(numero)
ocorrencia_numero = int(input("Digite um numero para verificar sua ocorrência na lista: "))
quantidade = lista_numeros.count(ocorrencia_numero)
print(f"O numero {ocorrencia_numero} aparece {quantidade} vezes na lista.")

# Exercicio 9
lista_maior_sete = []
for i in range(1, 6):
    nota = float(input(f"Digite a nota do {i}º aluno: "))
    if nota > 7:
        lista_maior_sete.append(nota)
print(f"As notas maiores que 7 são: {lista_maior_sete}")

# Exercicio 10
lista_compras = []
while True:
    item = input("Digite um item para adicionar à lista de compras (ou 'sair' para finalizar): ")
    if item.lower() == 'sair':
        if len(lista_compras) == 0:
            print("Sua lista de compras está vazia.")
        else:
            print(f"Sua lista de compras é {lista_compras}")
        break
    lista_compras.append(item)