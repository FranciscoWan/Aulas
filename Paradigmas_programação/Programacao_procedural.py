# Organiza o código em funções para dividir tarefas. 
# As instruções são executadas em sequência, de cima para baixo, com chamadas de funções para agrupar lógica.
# Muda as variáveis de acordo com o decorrer do código.
# A ordem importa muito

total = 0

def adicionar_produto(preco):
    global total
    total += preco

def aplicar_desconto():
    global total
    total *= 0.9

adicionar_produto(100)
aplicar_desconto()

print(total)

# Exemplos de linguagens de programação procedural: C, Pascal, Fortran, COBOL, BASIC.