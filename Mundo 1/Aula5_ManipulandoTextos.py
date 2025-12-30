# ============================================
# AULA 5 — MANIPULAÇÃO DE STRINGS (TEXTOS)
# Mundo 1 — Fundamentos do Python
# ============================================

# Strings são textos no Python.
# Elas podem ser delimitadas por aspas simples ('')
# ou aspas duplas ("").

texto = 'Curso em Vídeo de Python'

# --------------------------------------------
# TAMANHO E ÍNDICES DA STRING
# --------------------------------------------

# A string possui 27 caracteres
# Os índices vão de 0 até 26

print('Texto:', texto)
print('Quantidade de caracteres:', len(texto))

# --------------------------------------------
# FATIAMENTO (SLICING)
# --------------------------------------------

# Fatiamento permite acessar partes da string
# Sintaxe geral:
# texto[inicio:fim:passo]

print(texto[9])        # V (caractere no índice 9)
print(texto[9:14])     # Vídeo
print(texto[:5])       # Curso
print(texto[10:])      # ídeo de Python

# Passo (pula caracteres)
print(texto[::5])      # C eVd y  (de 5 em 5)
print(texto[9::3])     # VePh     (de 3 em 3 a partir do índice 9)
print(texto[9:21:2])   # Vdo ePto (de 2 em 2)

# Invertendo a string
print(texto[::-1])

# --------------------------------------------
# ANÁLISE DE TEXTO
# --------------------------------------------

# Contagem de caracteres
print(texto.count('o'))            # Quantas vezes aparece 'o'
print(texto.count('o', 0, 13))     # Conta 'o' apenas do índice 0 ao 12

# Procurando textos
print(texto.find('Vídeo'))         # Índice onde começa a palavra
print(texto.find('Android'))       # -1 (não encontrado)

# Verificando existência
print('Curso' in texto)            # True
print('Android' in texto)          # False

# --------------------------------------------
# TRANSFORMAÇÃO DE STRINGS
# --------------------------------------------

print(texto.replace('Python', 'Android'))
print(texto.upper())        # Tudo em maiúsculas
print(texto.lower())        # Tudo em minúsculas
print(texto.capitalize())  # Primeira letra maiúscula
print(texto.title())       # Primeira letra de cada palavra

# Remoção de espaços
texto_com_espacos = '   Python é incrível!   '
print(texto_com_espacos.strip())   # Remove espaços dos dois lados
print(texto_com_espacos.lstrip())  # Remove espaços da esquerda
print(texto_com_espacos.rstrip())  # Remove espaços da direita

# --------------------------------------------
# DIVISÃO E JUNÇÃO DE STRINGS
# --------------------------------------------

# Divide a string em palavras
palavras = texto.split()
print(palavras)

# Junta caracteres ou palavras com separador
print('-'.join(texto))

# --------------------------------------------
# COMBINAÇÃO DE MÉTODOS
# --------------------------------------------

# Pegando a terceira palavra e transformando em maiúscula
print(texto.split()[2].upper())  # VÍDEO

# --------------------------------------------
# TEXTOS LONGOS COM TRÊS ASPAS
# --------------------------------------------

print("""
Curso em Vídeo de Python
Aprenda Python de forma fácil e divertida!
Domine a programação com exemplos práticos.
""")

# ============================================
# FIM DA AULA
# ============================================
