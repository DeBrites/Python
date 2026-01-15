# ==================================================
# AULA 10 — ESTRUTURAS DE REPETIÇÃO (while)
# Mundo 2 — Fundamentos do Python
# ==================================================
#
# Nesta aula vamos estudar o laço de repetição "while".
#
# Estruturas de repetição servem para executar um mesmo
# bloco de código várias vezes, sem precisar reescrever
# as mesmas linhas.
#
# O laço "while" é usado quando NÃO sabemos previamente
# quantas vezes o código deve se repetir.
#
# Ele funciona da seguinte forma:
# - Enquanto a condição for verdadeira (True),
#   o bloco de código será executado.
# - Quando a condição se tornar falsa (False),
#   o laço é encerrado.
#
# Muito utilizado em:
# - Contadores
# - Validação de entrada do usuário
# - Menus interativos
# - Jogos simples
# - Processos controlados por condição
#
# OBSERVAÇÃO:
# O comando 'break' pode ser usado para sair de um laço
# while antes da condição se tornar falsa.
# Ele será estudado em aulas futuras.
#
# ==================================================
# EXEMPLO 1 — CONTADOR SIMPLES
# ==================================================

# Criamos uma variável contador iniciando em 0
contador = 0

# Enquanto o valor do contador for menor que 5,
# o bloco de código dentro do while será executado
while contador < 5:
    print(contador)  # Exibe o valor atual do contador
    contador += 1    # Incrementa 1 ao contador

# Saída esperada:
# 0
# 1
# 2
# 3
# 4
#
# Quando o contador chega a 5, a condição
# (contador < 5) se torna falsa e o laço termina.

# ==================================================
# EXEMPLO 2 — VALIDAÇÃO DE ENTRADA
# ==================================================

# Pedimos ao usuário um número inteiro
numero = int(input("Digite um número positivo: "))

# Enquanto o número for negativo,
# o programa continuará pedindo um novo valor
while numero < 0:
    print("Número inválido! Tente novamente.")
    numero = int(input("Digite um número positivo: "))

# Quando o usuário digitar um número válido,
# o laço termina
print("Obrigado! Você digitou o número:", numero)

# Esse tipo de estrutura é muito usada para
# garantir que o usuário informe dados corretos.

# ==================================================
# EXEMPLO 3 — MENU INTERATIVO
# ==================================================

# Criamos uma variável para armazenar a opção escolhida
opcao = ''

# O laço continuará enquanto a opção for diferente de 'S'
while opcao != 'S':
    print("\nMENU DE OPÇÕES")
    print("[A] Opção A")
    print("[B] Opção B")
    print("[S] Sair")

    # Recebe a opção do usuário e converte para maiúscula
    opcao = input("Escolha uma opção: ").upper()

    if opcao == 'A':
        print("Você escolheu a Opção A.")
    elif opcao == 'B':
        print("Você escolheu a Opção B.")
    elif opcao == 'S':
        print("Saindo do programa...")
    else:
        print("Opção inválida! Tente novamente.")

# O menu será exibido repetidamente
# até o usuário escolher a opção 'S'.

# ==================================================
# EXEMPLO 4 — CONTADOR REVERSO
# ==================================================

# Inicializamos o contador em 10
contador = 10

# Enquanto o contador for maior ou igual a 0,
# o laço continuará executando
while contador >= 0:
    print(contador)
    contador -= 1  # Decrementa 1 do contador

# Saída esperada:
# 10
# 9
# 8
# ...
# 1
# 0

# ==================================================
# EXEMPLO 5 — ACUMULADOR DE VALORES
# ==================================================

# Criamos uma variável para armazenar a soma
soma = 0

# Pedimos um número ao usuário
numero = int(input("Digite um número (0 para sair): "))

# Enquanto o número for diferente de 0,
# o valor será somado
while numero != 0:
    soma += numero
    numero = int(input("Digite um número (0 para sair): "))

# Quando o usuário digitar 0, o laço termina
print("A soma dos números digitados é:", soma)

# Esse padrão é muito usado para
# processar entradas contínuas.

# ==================================================
# EXEMPLO 6 — JOGO DE ADIVINHAÇÃO SIMPLES
# ==================================================

import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializamos a variável tentativa
tentativa = None

# Enquanto o usuário não acertar o número,
# o jogo continua
while tentativa != numero_secreto:
    tentativa = int(input("Adivinhe o número (1 a 100): "))

    if tentativa < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif tentativa > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print("Parabéns! Você acertou o número:", numero_secreto)

# Esse exemplo mostra como o while é ideal
# quando não sabemos quantas tentativas
# serão necessárias.

# ==================================================
# FIM DA AULA 10 — ESTRUTURAS DE REPETIÇÃO (while)
# ==================================================
