# ==================================================
# AULA 8 — CONDIÇÕES ANINHADAS (if dentro de if)
# Mundo 1 — Fundamentos do Python
# ==================================================

# Condições aninhadas permitem colocar uma estrutura
# condicional (if / elif / else) dentro de outra.
#
# Elas são utilizadas quando uma decisão depende
# do resultado de uma condição anterior.
#
# Muito comuns em:
# - Validações
# - Classificações
# - Sistemas de decisão
# - Regras de negócio

# ==================================================
# EXEMPLO 1 — CLASSIFICAÇÃO POR IDADE
# ==================================================

idade = int(input('Digite sua idade: '))

# Primeira condição
if idade >= 18:
    print('Você é maior de idade.')

    # Condição aninhada
    if idade >= 65:
        print('Você é um idoso.')
    else:
        print('Você é um adulto.')

else:
    print('Você é menor de idade.')

    # Condição aninhada
    if idade < 13:
        print('Você é uma criança.')
    else:
        print('Você é um adolescente.')

# ==================================================
# EXPLICAÇÃO
# ==================================================
#
# 1. Primeiro o programa verifica se a idade é >= 18
# 2. Se for verdadeira, entra no bloco interno
# 3. Caso contrário, entra no else e faz novas verificações
#
# Isso evita repetições e deixa o código mais lógico.

# ==================================================
# EXEMPLO 2 — AVALIAÇÃO DE NOTA COM elif ANINHADO
# ==================================================

nota = int(input('Digite sua nota: '))

if nota >= 60:
    print('Você passou no exame.')

    # Classificação da nota
    if nota >= 90:
        print('Parabéns! Conceito A.')
    elif nota >= 80:
        print('Bom trabalho! Conceito B.')
    elif nota >= 70:
        print('Conceito C.')
    else:
        print('Conceito D.')

else:
    print('Você não passou no exame.')

# ==================================================
# OBSERVAÇÃO IMPORTANTE
# ==================================================
#
# - Um if pode ter vários elif
# - Um if pode ter apenas um else
# - elif e else só existem se houver um if antes
# - A ordem das condições importa

# ==================================================
# EXEMPLO 3 — NÚMERO POSITIVO, PAR OU ÍMPAR
# ==================================================

numero = int(input('Digite um número: '))

if numero > 0:
    print('O número é positivo.')

    if numero % 2 == 0:
        print('O número é par.')
    else:
        print('O número é ímpar.')

else:
    print('O número não é positivo.')

# ==================================================
# EXEMPLO 4 — VALIDAÇÃO DE NOME
# ==================================================

nome = input('Digite seu nome: ')

if nome != '':
    if len(nome) > 4:
        print('Nome válido.')
    elif len(nome) == 3:
        print('Nome com 3 caracteres.')
    elif len(nome) == 4 and nome == 'Caio':
        print('Que nome bonito!')
    elif nome in 'Luiza Maria Raquel':
        print('Nome interessante.')
    else:
        print('Nome muito curto.')
else:
    print('O nome não pode estar vazio.')

print(f'Olá, {nome}!')

# ==================================================
# RESUMO DA AULA
# ==================================================
#
# ✔ Condições aninhadas são if dentro de if
# ✔ Usadas quando decisões dependem de outras
# ✔ Tornam o código mais organizado
# ✔ Muito usadas em validações reais
#
# ==================================================
# FIM DA AULA
# ==================================================
