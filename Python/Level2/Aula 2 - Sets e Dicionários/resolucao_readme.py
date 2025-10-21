# Resolução dos exercícios Readme.md

# Exercicio 1 
dicionario_pessoa = {}
for i in range(3):
    chave = input("Digite o nome do usuário: ")
    valor = input(f"Digite a idade do usuário, {chave}: ")
    dicionario_pessoa[chave] = valor
for c, v in dicionario_pessoa.items():
    print(f"O usuário {c} tem {v} anos.")

# Exercicio 2
dicionario_fruta = {}
for i in range(3):
    fruta = input("Digite o nome de uma fruta: ")
    preco = float(input(f"Digite o preço da fruta, {fruta}: "))
    dicionario_fruta[fruta] = preco
fruta_consultar = input("Digite o nome de uma fruta para consultar o preço: ")
if fruta_consultar in dicionario_fruta:
    print(f"O preço da fruta {fruta_consultar} é: R$ {dicionario_fruta[fruta_consultar]:.2f}")
else:   
    print(f"A fruta {fruta_consultar} não está no dicionário.")

# Exercicio 3
dicionario_alunos = {}
for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota do aluno, {nome}: "))
    dicionario_alunos[nome] = nota
for c, v in dicionario_alunos.items():
    if v >= 7:
        print(f"O aluno {c} foi aprovado com a nota {v}.")

# Exercicio 4
dicionario_login = {}
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")
dicionario_login[usuario] = senha
login_consultar = input("Digite o nome de usuário para login: ")
senha_consultar = input("Digite a senha para login: ")
if login_consultar == dicionario_login[usuario] and dicionario_login[login_consultar] == senha_consultar:
    print("Login bem sucedido!")
else:   
    print("Login falhou. Usuário ou senha incorretos.")

# Exercicio 5
set_numeros = set()
for i in range(5):
    numero = int(input("Digite um numero: "))
    set_numeros.add(numero)
numero_verificar = int(input("Digite um numero para verificar se está no conjunto: "))
if numero_verificar in set_numeros:
    print(f"O numero {numero_verificar} está no conjunto.")
else:
    print(f"O numero {numero_verificar} não está no conjunto.")

# Exercicio 6
set_cidades = set()
for i in range(5):
    cidade = input("Digite o nome de uma cidade: ")
    set_cidades.add(cidade)
cidade_verificar = input("Digite o nome de uma cidade para verificar se está no conjunto: ")
if cidade_verificar in set_cidades:
    print(f"A cidade {cidade_verificar} está no conjunto.")
else:
    print(f"A cidade {cidade_verificar} não está no conjunto.")

# Exercicio 7
dicionario_produtos = {}
for i in range(3):
    produto = input("Digite o nome do produto: ")
    qtd = int(input(f"Digite a quantidade do produto, {produto}: "))
    dicionario_produtos[produto] = qtd
produto_consultar = input("Digite o nome de um produto para consultar a quantidade: ")
if produto_consultar in dicionario_produtos:
    print(f"A quantidade do produto {produto_consultar} em estoque é: {dicionario_produtos[produto_consultar]}")
    nova_qtd = int(input(f"Digite a nova quantidade para atualizar o produto {produto_consultar}: "))
    dicionario_produtos[produto_consultar] = nova_qtd
    print(f"A quantidade do produto {produto_consultar} foi atualizada para: {dicionario_produtos[produto_consultar]}")
else:   
    print(f"O produto {produto_consultar} não está no estoque.")

# Exercicio 8
dicionario_alunos_notas = {"Pedro": [8, 7, 9], "Ana": [6, 5, 7], "Maria": [9, 8, 10]}
for aluno, notas in dicionario_alunos_notas.items():
    media = sum(notas) / len(notas)
    if media >= 7:
        print(f"O aluno {aluno} foi aprovado com média {media:.2f}.")
    else:
        print(f"O aluno {aluno} foi reprovado com média {media:.2f}.")

# Exercicio 9
turma_um = {"Alice", "Bruno", "Carla"}
turma_dois = {"Bruno", "Daniel", "Eva"}
alunos_comuns = turma_um.intersection(turma_dois)
print(f"Alunos que estão em ambas as turmas: {alunos_comuns}")
alunos_somente_turma_um = turma_um.difference(turma_dois)
print(f"Alunos que estão somente na turma um: {alunos_somente_turma_um}")

# Exercicio 10
cadastro_usuarios = {}
while True:
    print("Menu de opções - ")
    print('''
    1 - Cadastrar usuário
    2 - Atualizar dados do usuário
    3 - Listar usuários cadastrados
    4 - Sair''')
    opc = input("Digite a opção desejada: ")
    if opc == '4':
        break
    elif opc == '3':
        for usuario, dados in cadastro_usuarios.items():
            print(f"Usuário: {usuario}, Dados: {dados}")
    elif opc == '2':
        usuario_atualizar = input("Digite o nome de usuário para atualizar os dados: ")
        if usuario_atualizar in cadastro_usuarios:
            nova_senha = input("Digite a nova senha: ")
            novo_email = input("Digite o novo email: ")
            nova_idade = input("Digite a nova idade: ")
            cadastro_usuarios[usuario_atualizar]["senha"] = nova_senha
            cadastro_usuarios[usuario_atualizar]["email"] = novo_email
            cadastro_usuarios[usuario_atualizar]["idade"] = nova_idade
            print(f"Dados do usuário {usuario_atualizar} atualizados com sucesso.")
        else:
            print(f"O usuário {usuario_atualizar} não está cadastrado.")
    elif opc == '1':
        dicionario_dados_usuarios = {}
        usuario = input("Digite o nome de usuário para cadastro: ")
        senha = input("Digite a senha para cadastro: ")
        email = input("Digite o email para cadastro: ")
        idade = input("Digite a idade para cadastro: ")
        dicionario_dados_usuarios["senha"] = senha
        dicionario_dados_usuarios["email"] = email
        dicionario_dados_usuarios["idade"] = idade
        cadastro_usuarios[usuario] = dicionario_dados_usuarios
    else:
        print("Opção inválida. Tente novamente.")
