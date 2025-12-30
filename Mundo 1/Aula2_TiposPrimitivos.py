"""
==================================================
AULA 02 — TIPOS DE DADOS EM PYTHON
Mundo 1 — Fundamentos da Linguagem
==================================================

Nesta aula você vai aprender:
- O que são tipos de dados
- Tipos primitivos mais comuns do Python
- Como descobrir o tipo de uma variável
- Conversão de tipos (casting)
- Entrada de dados convertida
- Formatação de strings
"""

# ------------------------------------------------
# 1. O QUE SÃO TIPOS DE DADOS?
# ------------------------------------------------
# Toda variável em Python armazena um valor.
# Esse valor possui um TIPO DE DADO.
#
# O tipo define:
# - Que tipo de informação é
# - Quais operações podem ser feitas

# ------------------------------------------------
# 2. TIPOS DE DADOS MAIS COMUNS
# ------------------------------------------------
# int   → números inteiros (ex: 10, -3, 0)
# float → números decimais (ex: 3.14, 1.75)
# bool  → valores lógicos (True ou False)
# str   → textos (strings)

n1 = 5            # int
n2 = 3.14         # float
ligado = True     # bool
nome = 'Maria'    # str

print(n1, n2, ligado, nome)

# ------------------------------------------------
# 3. DESCOBRINDO O TIPO DE UMA VARIÁVEL
# ------------------------------------------------
# A função type() mostra o tipo de dado da variável.

print(type(n1))       # <class 'int'>
print(type(n2))       # <class 'float'>
print(type(ligado))   # <class 'bool'>
print(type(nome))     # <class 'str'>

# ------------------------------------------------
# 4. CONVERSÃO DE TIPOS (CASTING)
# ------------------------------------------------
# Às vezes precisamos converter um tipo em outro.
# Isso é feito com funções como:
# int(), float(), str()

idade_str = '25'
idade_int = int(idade_str)  # string → inteiro

altura_float = float('1.75')  # string → float

peso_str = '70.5'
peso_float = float(peso_str)

print(idade_int, type(idade_int))
print(altura_float, type(altura_float))
print(peso_float, type(peso_float))

# ------------------------------------------------
# 5. INPUT() SEMPRE RETORNA STRING
# ------------------------------------------------
# Tudo que vem do input() chega como texto (str).
# Por isso, precisamos converter quando queremos números.

idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

print('Idade:', idade)
print('Altura:', altura)

# ------------------------------------------------
# 6. FORMATAÇÃO DE STRINGS
# ------------------------------------------------
# Existem várias formas de montar textos com variáveis.

nome = 'Ana'
idade = 30

# Forma moderna e recomendada → f-strings
print(f'Nome: {nome}, Idade: {idade}')

# Forma mais antiga → format()
print('Nome: {}, Idade: {}'.format(nome, idade))

"""
==================================================
FIM DA AULA 02
==================================================
"""
