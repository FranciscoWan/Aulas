# Resolução dos exercícios Readme.md

# Exercicio 1 
# Resolução 1, utilizando a função sum(), max() e min()
lista_numeros = []
for i in range(5):
    num = int(input("Digite um número: "))
    lista_numeros.append(num)
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)
soma = sum(lista_numeros)

print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Soma dos números: {soma}")

# Resolução 2, sem utilizar a função sum(), max() e min()
lista_numeros = []
maior_numero = None
menor_numero = None
soma = 0
for i in range(5):
    num = int(input("Digite um número: "))
    lista_numeros.append(num)
for numero in lista_numeros:
    soma += numero
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero
    if menor_numero is None or numero < menor_numero:
        menor_numero = numero

print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Soma dos números: {soma}")

# Exercicio 2
dias_semana = ("Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado")
dia_para_buscar = int(input("Digite um número de 1 a 7 para ver o dia da semana correspondente: "))
if 1 <= dia_para_buscar <= 7:
    print(f"O dia correspondente é: {dias_semana[dia_para_buscar - 1]}")
else:
    print("Número inválido! Por favor, digite um número entre 1 e 7.")

# Exercicio 3
set_nomes = set()
for i in range(5):
    nome = input("Digite um nome: ")
    set_nomes.add(nome)

print(f"Nomes únicos digitados: {set_nomes}")

# Exercicio 4
dicionario_pessoas = {}
for i in range(3):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    dicionario_pessoas[nome] = idade
print("Pessoa mais velha: ", end="")
mais_velha = max(dicionario_pessoas, key=dicionario_pessoas.get)
print(f"{mais_velha} com {dicionario_pessoas[mais_velha]} anos.")
print("Pessoa mais nova: ", end="")
mais_nova = min(dicionario_pessoas, key=dicionario_pessoas.get)
print(f"{mais_nova} com {dicionario_pessoas[mais_nova]} anos.")

# Exercicio 5
lista_contatos = {}
while True:
    print("\nMenu de Contatos")
    print("Escolha uma opção:\n1. Adicionar contato\n2. Remover contato\n3. Exibir todos os contatos\n4. Sair")
    opc = int(input("Opção: "))
    if opc == 1:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        lista_contatos[nome] = telefone
        print(f"Contato {nome} adicionado.")
    elif opc == 2:
        nome = input("Digite o nome do contato a ser removido: ")
        if nome in lista_contatos:
            del lista_contatos[nome]
            print(f"Contato {nome} removido.")
        else:
            print(f"Contato {nome} não encontrado.")
    elif opc == 3:
        print("Lista de Contatos:")
        for nome, telefone in lista_contatos.items():
            print(f"{nome}: {telefone}")
    elif opc == 4:
        print("Saindo do programa de contatos.")
        break
    else:
        print("Opção inválida! Tente novamente.")