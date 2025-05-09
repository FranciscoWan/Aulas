# Programa para calcular média de alunos com lista.

# Lista para armazenar os dados de todos os alunos
alunos = []

# Início da coleta de dados
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break

    notas = []  # Lista para armazenar as 3 notas do aluno

    # Coletando 3 notas com um laço for
    for i in range(3):

        # Criação da variável soma_total
        soma_total = 0
        nota = float(input(f"Digite a nota {i + 1}: "))

        # Adição das notas dentro da lista de notas
        notas.append(nota)
        soma_total += nota

    media = soma_total/3
    # Determinando a situação com base na média (que foi mal calculada)
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    # Armazenando os dados do aluno em um dicionário
    aluno = {
        'nome': nome,
        'notas': notas,
        'media': media,
        'situacao': situacao
    }

    alunos.append(aluno)

# Exibição final do boletim de todos os alunos
print("\n--- Boletim Final ---")
for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}\n")