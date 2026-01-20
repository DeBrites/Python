# ==================================================
# AULA 12 — VARIÁVEIS COMPOSTAS: TUPLAS
# Mundo 3 — Fundamentos do Python
# ==================================================
#
# Em Python, existem três tipos principais
# de variáveis compostas:
#
# - Tuplas (tuple)
# - Listas (list)
# - Dicionários (dict)
#
# Variáveis compostas são estruturas capazes
# de armazenar MÚLTIPLOS valores em uma única variável.
#
# ==================================================
# DIFERENÇAS ENTRE TUPLAS, LISTAS E DICIONÁRIOS
# ==================================================
#
# Tuplas:
# - Imutáveis (não podem ser alteradas após criadas)
# - Usam parênteses ()
#
# Listas:
# - Mutáveis (podem ser alteradas)
# - Usam colchetes []
#
# Dicionários:
# - Mutáveis
# - Armazenam pares de chave : valor
# - Usam chaves {}
#
# ==================================================
# O QUE SÃO TUPLAS
# ==================================================
#
# Uma tupla é uma coleção ORDENADA de elementos.
# Cada elemento possui um índice numérico,
# começando sempre do índice 0.
#
# Uma tupla pode armazenar dados de
# TIPOS DIFERENTES ao mesmo tempo.
#
# Uma vez criada, a tupla NÃO pode ser modificada.
#
# ==================================================
# CRIAÇÃO DE UMA TUPLA
# ==================================================

minha_tupla = (1, 2, 3, 'a', 'b', 'c')
print(minha_tupla)

# ==================================================
# ACESSANDO ELEMENTOS DA TUPLA
# ==================================================

print(minha_tupla[0])  # Primeiro elemento
print(minha_tupla[3])  # Quarto elemento

# print(minha_tupla[6])
# Isso geraria um erro, pois o índice não existe

# ==================================================
# IMUTABILIDADE DAS TUPLAS
# ==================================================
#
# Tuplas NÃO permitem alteração de seus valores.
# O código abaixo geraria um erro:

# minha_tupla[0] = 10  # ERRO: tuplas são imutáveis

# ==================================================
# MÉTODOS ÚTEIS PARA TUPLAS
# ==================================================

# count() → conta quantas vezes um elemento aparece
print(minha_tupla.count(2))  # Saída: 1

# index() → retorna o índice da primeira ocorrência
print(minha_tupla.index('b'))  # Saída: 4

# ==================================================
# DESEMPACOTAMENTO DE TUPLAS
# ==================================================
#
# Podemos atribuir cada valor da tupla
# a uma variável individual

a, b, c, d, e, f = minha_tupla

print(a)
print(d)
print(f)

# ==================================================
# CONCATENAÇÃO DE TUPLAS
# ==================================================

tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')

tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)
# Saída: (1, 2, 3, 'a', 'b', 'c')

# A ordem da soma altera o resultado
tupla_concatenada_diferente = tupla2 + tupla1
print(tupla_concatenada_diferente)
# Saída: ('a', 'b', 'c', 1, 2, 3)

# ==================================================
# INDEX E COUNT EM TUPLAS CONCATENADAS
# ==================================================

print(tupla_concatenada.index('a'))  # Retorna 3

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(c)  # (5, 8, 1, 2, 2, 5, 4)

# index pode receber um ponto inicial de busca
print(c.index(5, 1))  # Retorna o segundo 5

# ==================================================
# FATIAMENTO DE TUPLAS
# ==================================================

print(minha_tupla[1:4])
print(minha_tupla[:3])
print(minha_tupla[3:])
print(minha_tupla[::2])
print(minha_tupla[::-1])

# Índices negativos
print(minha_tupla[-1])
print(minha_tupla[-2])
print(minha_tupla[-3:])
print(minha_tupla[-4:-1])

# ==================================================
# ITERANDO SOBRE UMA TUPLA
# ==================================================

# Forma simples
for elemento in minha_tupla:
    print(elemento)

# Usando índice
for i in range(len(minha_tupla)):
    print(minha_tupla[i])

# Elemento + posição
for pos, elemento in enumerate(minha_tupla):
    print(f'O elemento {elemento} está na posição {pos}')

# ==================================================
# TAMANHO DA TUPLA
# ==================================================

print(len(minha_tupla))

# ==================================================
# TUPLAS ANINHADAS
# ==================================================

tupla_aninhada = (1, 2, (3, 4), (5, 6))

print(tupla_aninhada[2])
print(tupla_aninhada[2][0])

# ==================================================
# FUNÇÃO sorted() COM TUPLAS
# ==================================================
#
# sorted() NÃO altera a tupla original.
# Ela retorna uma LISTA ordenada.

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(sorted(lanche))  # Retorna uma lista ordenada
print(lanche)          # Tupla original permanece igual

# ==================================================
# EXCLUINDO UMA TUPLA INTEIRA
# ==================================================
#
# Não é possível apagar ou alterar elementos,
# mas é possível apagar a tupla inteira.

del(lanche)

# print(lanche)
# Isso geraria erro, pois a tupla foi apagada

# ==================================================
# VANTAGENS DAS TUPLAS
# ==================================================
#
# - Mais rápidas que listas para leitura
# - Ocupam menos memória
# - Garantem integridade dos dados
#
# Ideais para:
# - Constantes
# - Dados fixos
# - Configurações
#
# ==================================================
# CONCLUSÃO
# ==================================================
#
# Tuplas são estruturas simples, eficientes
# e seguras para armazenar dados imutáveis.
#
# Entender tuplas é fundamental antes de
# avançar para listas e dicionários.
#
# ==================================================
# FIM DA AULA 12 — TUPLAS
# ==================================================