# ==================================================
# AULA 13 — VARIÁVEIS COMPOSTAS: LISTAS (Parte 1)
# Mundo 3 — Fundamentos do Python
# ==================================================
#
# Em Python, assim como as tuplas,
# as listas são usadas para armazenar
# múltiplos valores em uma única variável.
#
# A principal DIFERENÇA é que:
#
# - Listas são MUTÁVEIS
# - Tuplas são IMUTÁVEIS
#
# Ou seja, em listas podemos:
# - Alterar valores
# - Adicionar elementos
# - Remover elementos
#
# ==================================================
# CARACTERÍSTICAS DAS LISTAS
# ==================================================
#
# - São coleções ORDENADAS
# - Possuem índices numéricos (começando em 0)
# - Podem armazenar tipos diferentes
# - Utilizam colchetes []
#
# ==================================================
# CRIAÇÃO DE UMA LISTA
# ==================================================

minha_lista = [1, 2, 3, 'a', 'b', 'c']
print(minha_lista)

# ==================================================
# ADICIONANDO ELEMENTOS NA LISTA
# ==================================================

# append() → adiciona no FINAL da lista
minha_lista.append('d')
print(minha_lista)
# [1, 2, 3, 'a', 'b', 'c', 'd']

# insert() → adiciona em uma POSIÇÃO ESPECÍFICA
minha_lista.insert(0, 'e')
print(minha_lista)
# ['e', 1, 2, 3, 'a', 'b', 'c', 'd']

# ==================================================
# REMOVENDO ELEMENTOS DA LISTA
# ==================================================

# del → remove pelo índice
del minha_lista[3]
print(minha_lista)

# pop() → remove pelo índice (ou o último elemento)
minha_lista.pop(3)
print(minha_lista)

# remove() → remove pelo VALOR
minha_lista.remove('c')
print(minha_lista)

# Todos os métodos acima:
# - removem o elemento
# - reorganizam os índices automaticamente

# ==================================================
# EVITANDO ERRO COM remove()
# ==================================================
#
# Se tentar remover um valor inexistente,
# o Python gera um erro.
# Podemos evitar isso usando if + in

if 'a' in minha_lista:
    minha_lista.remove('a')

print(minha_lista)

# ==================================================
# CRIANDO LISTAS COM range()
# ==================================================

valores = list(range(4, 11))
print(valores)
# [4, 5, 6, 7, 8, 9, 10]

# range(início, fim, passo)
valores_pulo = list(range(4, 11, 3))
print(valores_pulo)
# [4, 7, 10]

# ==================================================
# ORDENANDO LISTAS
# ==================================================

valor = [8, 2, 5, 4, 9, 3, 0]
print(valor)

# sort() → ordena em ordem crescente
valor.sort()
print(valor)

# sort(reverse=True) → ordem decrescente
valor.sort(reverse=True)
print(valor)

# ==================================================
# TAMANHO DA LISTA
# ==================================================

print(len(valor))
# Retorna a quantidade de elementos da lista

# ==================================================
# PERCORRENDO LISTAS COM for
# ==================================================

for v in valor:
    print(v)

# Com enumerate() → índice + valor
for c, v in enumerate(valor):
    print(f'Na posição {c} encontrei o valor {v}')

# ==================================================
# LIGAÇÃO ENTRE LISTAS (CUIDADO!)
# ==================================================
#
# Quando fazemos b = a, as listas ficam ligadas

a = [2, 3, 4, 7]
b = a

b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
# Alterar uma altera a outra

# ==================================================
# CÓPIA DE LISTAS (FORMA CORRETA)
# ==================================================
#
# Para criar uma CÓPIA independente,
# usamos fatiamento [:]

c = [2, 3, 4, 7]
d = c[:]

d[2] = 8

print(f'Lista C: {c}')
print(f'Lista D: {d}')

# ==================================================
# CONCLUSÃO
# ==================================================
#
# Listas são estruturas extremamente poderosas
# por serem mutáveis e flexíveis.
#
# São ideais para:
# - Conjuntos de dados dinâmicos
# - Armazenar entradas do usuário
# - Trabalhar com sequências que mudam
#
# ==================================================
# FIM DA AULA — LISTAS (PARTE 1)
# ==================================================