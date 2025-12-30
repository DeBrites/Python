# ============================================
# AULA 6 — ESTRUTURAS CONDICIONAIS (IF / ELIF / ELSE)
# Mundo 1 — Fundamentos do Python
# ============================================

# Estruturas condicionais permitem que o programa
# tome decisões e execute diferentes caminhos
# dependendo de uma condição (True ou False).

# As principais estruturas são:
# if    → se
# elif  → senão se
# else  → senão

# --------------------------------------------
# ESTRUTURA CONDICIONAL SIMPLES (if)
# --------------------------------------------

idade = 18

# O bloco dentro do if só executa se a condição for verdadeira
if idade >= 18:
    print('Você é maior de idade.')

# --------------------------------------------
# ESTRUTURA CONDICIONAL COM ELSE
# --------------------------------------------

idade = 16

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

# --------------------------------------------
# ESTRUTURA CONDICIONAL COM ELIF
# --------------------------------------------

# O elif permite testar várias condições
# Apenas o primeiro bloco verdadeiro será executado

nota = 85

if nota >= 90:
    print('Você recebeu um A.')
elif nota >= 80:
    print('Você recebeu um B.')
elif nota >= 70:
    print('Você recebeu um C.')
else:
    print('Você precisa melhorar.')

# --------------------------------------------
# ESTRUTURA CONDICIONAL ANINHADA
# --------------------------------------------

# Um if dentro de outro if

numero = 10

if numero > 0:
    if numero % 2 == 0:
        print('O número é positivo e par.')
    else:
        print('O número é positivo e ímpar.')
else:
    print('O número é negativo ou zero.')

# --------------------------------------------
# OPERADORES LÓGICOS (and / or / not)
# --------------------------------------------

idade = 20
renda = 3000

# Operador AND: todas as condições devem ser verdadeiras
if idade >= 18 and renda >= 2500:
    print('Você é elegível para o empréstimo.')
else:
    print('Você não é elegível para o empréstimo.')

# Operador OR: pelo menos uma condição precisa ser verdadeira
if idade < 18 or renda < 2500:
    print('Você não atende a algum dos requisitos.')

# Operador NOT: inverte o valor lógico
tem_carteira_de_trabalho = False

if not tem_carteira_de_trabalho:
    print('Você precisa tirar a carteira de trabalho.')

# --------------------------------------------
# CONDIÇÃO TERNÁRIA
# --------------------------------------------

# Forma curta de escrever if e else em uma linha

idade = 22
status = 'Maior de idade' if idade >= 18 else 'Menor de idade'
print(status)

# --------------------------------------------
# VERIFICAÇÃO DE STRING VAZIA
# --------------------------------------------

nome = ''

# Strings vazias são avaliadas como False
if not nome:
    print('O nome não pode estar vazio.')

# --------------------------------------------
# VERIFICAÇÃO DE INTERVALO
# --------------------------------------------

numero = 15

# Forma simples e legível de verificar intervalos
if 10 <= numero <= 20:
    print('O número está entre 10 e 20.')

# --------------------------------------------
# USO DO PASS
# --------------------------------------------

# O pass é usado quando a estrutura existe,
# mas ainda não há código para executar

idade = 25

if idade < 18:
    pass  # Ainda não implementado
else:
    print('Você é maior de idade.')

# ============================================
# FIM DA AULA
# ============================================
