# ==================================================
# AULA 9 — ESTRUTURAS DE REPETIÇÃO (for)
# Mundo 2 — Fundamentos do Python
# ==================================================

# Estruturas de repetição permitem executar um bloco
# de código várias vezes sem precisar repetir linhas.
#
# O laço "for" é usado quando sabemos previamente
# quantas vezes a repetição deve acontecer.
#
# Muito utilizado em:
# - Processamento de listas
# - Geração de sequências numéricas
# - Percorrer textos (strings)
# - Repetições controladas

# ==================================================
# EXEMPLO 1 — ITERANDO SOBRE UMA LISTA
# ==================================================

frutas = ['maçã', 'banana', 'laranja']

for fruta in frutas:
    print(fruta)

# Saída:
# maçã
# banana
# laranja

# O laço percorre cada item da lista
# e a variável "fruta" recebe um valor por vez.

# ==================================================
# EXEMPLO 2 — USANDO range()
# ==================================================

# range(n) gera uma sequência de 0 até n-1

for numero in range(5):
    print(numero)

# Saída:
# 0
# 1
# 2
# 3
# 4

# ==================================================
# range(início, fim, passo)
# ==================================================

for numero in range(2, 10, 2):
    print(numero)

# Saída:
# 2
# 4
# 6
# 8

# Neste caso:
# - começa em 2
# - termina antes de 10
# - pula de 2 em 2

# ==================================================
# EXEMPLO 3 — ITERANDO SOBRE UMA STRING
# ==================================================

palavra = 'Python'

for letra in palavra:
    print(letra)

# Saída:
# P
# y
# t
# h
# o
# n

# Cada caractere da string é tratado
# como um elemento da repetição.

# ==================================================
# EXEMPLO 4 — SOMANDO VALORES DE UMA LISTA
# ==================================================

numeros = [1, 2, 3, 4, 5]
soma = 0

for numero in numeros:
    soma += numero

print('Soma dos números:', soma)

# Saída:
# Soma dos números: 15

# O operador += acumula valores ao longo do loop.

# ==================================================
# EXEMPLO 5 — for ANINHADO (loop dentro de loop)
# ==================================================

for i in range(1, 4):
    for j in range(1, 4):
        print(f'i: {i}, j: {j}')

# Saída:
# i: 1, j: 1
# i: 1, j: 2
# i: 1, j: 3
# i: 2, j: 1
# i: 2, j: 2
# i: 2, j: 3
# i: 3, j: 1
# i: 3, j: 2
# i: 3, j: 3

# Loops aninhados são usados para:
# - Matrizes
# - Combinações
# - Tabelas
# - Simulações

# ==================================================
# EXEMPLO 6 — CONTAGEM REGRESSIVA
# ==================================================

for numero in range(10, 0, -1):
    print(numero)

# Saída:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

# Aqui usamos um passo negativo (-1)
# para contar de trás para frente.

# ==================================================
# EXEMPLO 7 — USANDO enumerate()
# ==================================================

frutas = ['maçã', 'banana', 'laranja']

for indice, fruta in enumerate(frutas):
    print(f'Índice: {indice}, Fruta: {fruta}')

# Saída:
# Índice: 0, Fruta: maçã
# Índice: 1, Fruta: banana
# Índice: 2, Fruta: laranja

# enumerate() retorna:
# - o índice do elemento
# - o valor do elemento

# Muito útil quando precisamos:
# - Saber a posição
# - Manipular listas
# - Exibir dados formatados

# ==================================================
# RESUMO DA AULA
# ==================================================
#
# ✔ O for repete um bloco de código
# ✔ Pode percorrer listas, strings e ranges
# ✔ range() gera sequências numéricas
# ✔ enumerate() fornece índice + valor
# ✔ for pode ser aninhado
#
# ==================================================
# FIM DA AULA
# ==================================================