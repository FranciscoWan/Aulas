# DRY - Don't Repeat Yourself (Não se repita)

#  Evite duplicação de código. Toda peça de conhecimento deve ter uma única representação no sistema.

# Ruim
def criar_usuario(nome, email):
    if "@" not in email:
        raise ValueError("Email inválido")
    # ...

def atualizar_usuario(nome, email):
    if "@" not in email:
        raise ValueError("Email inválido")
    # ...

# Bom
def validar_email(email: str) -> None:
    if "@" not in email:
        raise ValueError("Email inválido")

def criar_usuario(nome, email):
    validar_email(email)
    # ...

def atualizar_usuario(nome, email):
    validar_email(email)
    # ...

# Benefícios: Menos bugs, manutenção concentrada, códigos mais enxutos.

