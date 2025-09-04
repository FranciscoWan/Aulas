# 📘 Aula 1 – Fundamentos de Python e Condicionais  

## 📖 Conteúdo da Aula  
Nesta primeira aula, revisamos os principais fundamentos da linguagem Python.  

### 1. Variáveis e Tipos de Dados  
- **Variáveis:** espaços na memória usados para armazenar valores.  
- **Tipos básicos em Python:**  
  - `int` → números inteiros  
  - `float` → números decimais  
  - `str` → textos  
  - `bool` → verdadeiro/falso  

Exemplo:  
```python
idade = 25
altura = 1.80
nome = "Maria"
estudante = True
```

---

### 2. Entrada e Saída de Dados  
- **Saída:** `print()`  
- **Entrada:** `input()`  

Exemplo:  
```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}")
```

---

### 3. Operadores  

**Aritméticos:** `+`, `-`, `*`, `/`, `//`, `%`, `**`  
```python
print(2 + 3)   # 5
print(10 % 3)  # 1
```

**Comparação:** `==`, `!=`, `>`, `<`, `>=`, `<=`  
```python
print(5 > 3)   # True
```

**Lógicos:** `and`, `or`, `not`  
```python
print(10 > 5 and 8 > 3)  # True
```

---

### 4. Estruturas Condicionais  
Permitem tomar decisões no código.  

```python
nota = 75

if nota >= 90:
    print("Aprovado com nota A")
elif nota >= 60:
    print("Aprovado com nota B")
else:
    print("Reprovado")
```

---

## 📝 Exercícios  

### Exercícios propostos em aula  

1. **Verificador de Número Par ou Ímpar**  
   Peça um número inteiro ao usuário e use uma condição para determinar e exibir se ele é par ou ímpar.  
   *(Dica: o operador de resto `%` será muito útil aqui!)*  

2. **Sistema de Média Escolar**  
   Desenvolva um programa que receba duas notas de um aluno.  
   Calcule a média dessas notas. Em seguida, usando condicionais, informe se o aluno está **Aprovado** (média ≥ 6) ou **Reprovado**.  

3. **Mini-Calculadora Interativa**  
   Crie um programa que receba dois números e pergunte ao usuário qual operação matemática (**soma, subtração, multiplicação ou divisão**) ele deseja realizar.  
   Utilize condicionais para executar a operação escolhida e, por fim, exiba o resultado.  

---

### Exercícios extras  

4. Peça ao usuário para digitar um número e verifique se ele é **positivo, negativo ou zero**.  
5. Peça ao usuário três números e mostre qual é o **maior** deles.  
6. Crie um programa que peça o nome de um usuário e exiba uma mensagem de boas-vindas personalizada.  
7. Peça um número e mostre o **dobro**, o **triplo** e a **raiz quadrada** desse número.  
8. Crie um programa que pergunte a senha ao usuário e só mostre “Acesso permitido” se a senha for `"python123"`.  

---

### Lista de exercícios extras

[Lista para exercícios](https://github.com/FranciscoWan/Desafios/tree/main/Python/condicionais)
