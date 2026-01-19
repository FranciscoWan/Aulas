#  Programação que se baseia em regras e fatos declarativos. O programador define um conjunto de regras e fatos que descrevem a lógica do problema, após isso o programa encontra a solução automaticamente.

pais = [
    ("Joao", "Maria"),
    ("Maria", "Ana"),
    ("Carlos", "Pedro")
]

def eh_avo(avo, neto):
    for pai, filho in pais:
        if pai == avo:
            for pai2, filho2 in pais:
                if pai2 == filho and filho2 == neto:
                    return True
    return False

print(eh_avo("Joao", "Ana"))     # True
print(eh_avo("Carlos", "Ana"))  # False

# Você não disse como procurar o número, o sistema deduziu usando lógica.

#  Exemplos de linguagens de programação, Prolog, DataLog

