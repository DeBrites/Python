# ==================================================
# AULA 14 — VARIÁVEIS COMPOSTAS: LISTAS (Parte 2)
# Mundo 3 — Fundamentos do Python
# ==================================================
#
# Nesta aula, vamos aprofundar o uso de LISTAS,
# principalmente listas dentro de listas
# (listas compostas).
#
# Também veremos um conceito MUITO IMPORTANTE:
# - Referência vs Cópia de listas
#
# ==================================================
# CRIANDO UMA LISTA SIMPLES
# ==================================================

dados = list()

dados.append('Pedro')
dados.append(25)

print(dados[0])  # Pedro
print(dados[1])  # 25

# ==================================================
# LISTAS DENTRO DE LISTAS (LISTAS COMPOSTAS)
# ==================================================
#
# Podemos criar uma lista que contém OUTRAS listas

pessoas = list()

# IMPORTANTE: usamos [:] para copiar a lista
pessoas.append(dados[:])

print(pessoas)  # [['Pedro', 25]]

# Alterando a lista original
dados[0] = 'Maria'
dados[1] = 30

print(dados)     # ['Maria', 30]
print(pessoas)   # [['Pedro', 25]]  → NÃO mudou

# Isso acontece porque usamos uma CÓPIA

# ==================================================
# ADICIONANDO NOVAS PESSOAS
# ==================================================

pessoas.append(['Ana', 22])

print(pessoas)
# [['Pedro', 25], ['Ana', 22]]

# Acessando dados
print(pessoas[0][0])  # Pedro
print(pessoas[0][1])  # 25
print(pessoas[1][0])  # Ana
print(pessoas[1][1])  # 22

# ==================================================
# PROBLEMA COM REFERÊNCIA DE LISTAS
# ==================================================
#
# Se NÃO copiarmos a lista, ocorre um problema

teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()

# Aqui NÃO estamos copiando!
galera.append(teste)

# Alterando a lista original
teste[0] = 'Maria'
teste[1] = 30

galera.append(teste)

print(galera)
# [['Maria', 30], ['Maria', 30]]

# Ambas apontam para a MESMA lista

# ==================================================
# COMO RESOLVER (CRIAR CÓPIA)
# ==================================================

galera = list()
teste = ['Gustavo', 40]

galera.append(teste[:])      # cópia
galera.append(list(teste))   # outra forma de copiar

print(galera)

# ==================================================
# PERCORRENDO LISTAS COMPOSTAS
# ==================================================

galera = [
    ['João', 19],
    ['Ana', 33],
    ['Jorge', 22],
    ['Maria', 45],
    ['Pedro', 25]
]

for p in galera:
    print(f'{p[0]} tem {p[1]} anos.')

# ==================================================
# COLETANDO DADOS COM LOOP
# ==================================================

galera = list()
dado = list()
totmaior = totmenor = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))

    galera.append(dado[:])  # cópia
    dado.clear()            # limpa a lista

print(galera)

# ==================================================
# ANÁLISE DOS DADOS
# ==================================================

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1

print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')

# ==================================================
# FUNÇÃO sorted() (ORDENAÇÃO SEM ALTERAR A LISTA)
# ==================================================

numeros = [5, 2, 9, 1, 5, 6]

print(sorted(numeros))  # lista ordenada
print(numeros)          # lista original intacta

# Com strings
palavras = ['banana', 'abacaxi', 'laranja', 'uva']

print(sorted(palavras))
print(palavras)

# ==================================================
# CONCLUSÃO
# ==================================================
#
# - Listas podem conter outras listas
# - Sempre cuidado com REFERÊNCIA vs CÓPIA
# - Use [:] ou list() para copiar
#
# Esse conceito é FUNDAMENTAL para evitar bugs.
#
# ==================================================
# FIM DA AULA 14 — LISTAS (Parte 2)
# ==================================================