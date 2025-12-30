# ============================================
# AULA 3 — OPERADORES ARITMÉTICOS EM PYTHON
# Mundo 1 — Fundamentos
# ============================================

# Operadores aritméticos são utilizados para realizar
# operações matemáticas básicas no Python.

# PRINCIPAIS OPERADORES:
# +  Adição
# -  Subtração
# *  Multiplicação
# ** Exponenciação
# /  Divisão
# // Divisão inteira
# %  Módulo (resto da divisão)

# --------------------------------------------
# EXEMPLOS BÁSICOS
# --------------------------------------------

a = 10
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
exponenciacao = a ** b
divisao = a / b
divisao_inteira = a // b
modulo = a % b

print('Adição:', soma)                 # 13
print('Subtração:', subtracao)         # 7
print('Multiplicação:', multiplicacao) # 30
print('Exponenciação:', exponenciacao) # 1000
print('Divisão:', divisao)             # 3.333...
print('Divisão inteira:', divisao_inteira) # 3
print('Módulo:', modulo)               # 1

# --------------------------------------------
# OPERADORES COM DIFERENTES TIPOS DE DADOS
# --------------------------------------------

# Operações podem envolver números inteiros (int),
# números decimais (float) e strings (str)

x = 5        # int
y = 2.5      # float
z = 'Hello'  # str

soma_int_float = x + y
concat_str = z + ' World'

print('Soma int + float:', soma_int_float)
print('Concatenação de strings:', concat_str)

print('Tipo da soma:', type(soma_int_float))     # float
print('Tipo da concatenação:', type(concat_str)) # str

# --------------------------------------------
# ORDEM DE PRECEDÊNCIA DOS OPERADORES
# --------------------------------------------

# A ordem de execução segue esta hierarquia:
# 1. Parênteses ()
# 2. Exponenciação (**)
# 3. Multiplicação (*), Divisão (/), Divisão inteira (//), Módulo (%)
# 4. Adição (+), Subtração (-)

resultado = 3 + 5 * 2 ** 2 - (4 / 2)

# Passo a passo:
# 2 ** 2 = 4
# 5 * 4 = 20
# 4 / 2 = 2.0
# 3 + 20 - 2.0 = 21.0

print('Resultado da expressão:', resultado)

# Outro exemplo:

calculo = (10 + 2 * 3 ** 2) / 4 - 10 % 3

# Passo a passo:
# 3 ** 2 = 9
# 2 * 9 = 18
# 10 + 18 = 28
# 10 % 3 = 1
# 28 / 4 = 7.0
# 7.0 - 1 = 6.0

print('Resultado do cálculo:', calculo)

# --------------------------------------------
# DIFERENÇA ENTRE "=" E "=="
# --------------------------------------------

# "=" é operador de ATRIBUIÇÃO
# "==" é operador de COMPARAÇÃO

a = 5
b = 5
c = 10

print(a == b)  # True
print(a == c)  # False
print(b == c)  # False

# --------------------------------------------
# OPERAÇÕES COM STRINGS
# --------------------------------------------

# Concatenação com "+"
str1 = 'Olá, '
str2 = 'mundo!'
mensagem = str1 + str2
print(mensagem)

nome = 'Ana'
saudacao = 'Bem-vinda, ' + nome + '!'
print(saudacao)

idade = 25
info = 'Idade: ' + str(idade) + ' anos'
print(info)

# --------------------------------------------
# REPETIÇÃO DE STRINGS COM "*"
# --------------------------------------------

repeticao = 'Python! ' * 3
print(repeticao)

linha = '-' * 20
print(linha)

titulo = 'Capítulo 1\n' * 3
print(titulo)

# --------------------------------------------
# FORMATAÇÃO E ALINHAMENTO DE STRINGS
# --------------------------------------------

nome = input('Qual é o seu nome? ')

print('Prazer em te conhecer, {:<20}!'.format(nome))  # Alinhado à esquerda
print('Prazer em te conhecer, {:^20}!'.format(nome))  # Centralizado
print('Prazer em te conhecer, {:>20}!'.format(nome))  # Alinhado à direita
print('Prazer em te conhecer, {:*^20}!'.format(nome)) # Centralizado com preenchimento

# ============================================
# FIM DA AULA
# ============================================
