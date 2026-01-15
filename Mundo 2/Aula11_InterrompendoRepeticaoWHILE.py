# ==================================================
# AULA 11 — INTERROMPENDO REPETIÇÕES (while)
# Mundo 2 — Fundamentos do Python
# ==================================================
#
# Normalmente, as linguagens de programação possuem
# três tipos principais de estruturas de repetição:
#
# - for
# - while
# - do...while (ou repeat)
#
# O Python NÃO possui a estrutura do tipo do...while.
#
# O do...while tem a seguinte característica:
# - O bloco de código é executado PELO MENOS UMA VEZ
# - Depois disso, a condição é verificada
#
# Em Python, podemos SIMULAR esse comportamento
# utilizando:
# - while True
# - e o comando break
#
# ==================================================
# O COMANDO break
# ==================================================
#
# O comando break serve para ENCERRAR um laço
# de repetição imediatamente, mesmo que a condição
# do while ainda seja verdadeira.
#
# Ele pode ser usado tanto em laços while quanto for.
#
# ==================================================
# EXEMPLO 1 — SIMULAÇÃO DO DO...WHILE
# ==================================================

# Este laço começa com a condição True,
# ou seja, ele sempre será executado ao menos uma vez
while True:
    numero = int(input("Digite um número (ou 0 para sair): "))

    # Condição de parada
    if numero == 0:
        print("Saindo do programa.")
        break  # Encerra o laço

    # Executado se o usuário não digitar 0
    print(f"Você digitou o número {numero}")

# Aqui o programa continua após o loop
print("Programa encerrado.")

# Esse padrão simula exatamente o comportamento
# de um do...while.

# ==================================================
# EXEMPLO 2 — USO DO break PARA VALIDAR ENTRADA
# ==================================================

while True:
    idade = int(input("Digite sua idade (ou um número negativo para sair): "))

    # Se a idade for negativa, encerramos o laço
    if idade < 0:
        print("Saindo do programa.")
        break

    # Caso contrário, exibimos a idade
    print(f"Sua idade é {idade} anos.")

# Esse tipo de estrutura é muito usada
# para controlar quando o programa deve parar.

# ==================================================
# EXEMPLO 3 — MENU COM SAÍDA CONTROLADA
# ==================================================

while True:
    resposta = input("Deseja continuar? (s/n): ").lower()

    if resposta == 'n':
        print("Encerrando o programa.")
        break
    elif resposta == 's':
        print("Continuando o programa...")
    else:
        print("Resposta inválida! Digite 's' ou 'n'.")

# O laço só termina quando o usuário
# escolhe explicitamente sair.

# ==================================================
# EXEMPLO 4 — VALIDAÇÃO DE NÚMERO POSITIVO
# ==================================================

# Pedimos ao usuário um número positivo
while True:
    numero = int(input("Digite um número positivo: "))

    # Se o número for válido, encerramos o laço
    if numero >= 0:
        print(f"Obrigado! Você digitou o número: {numero}")
        break
    else:
        print("Número inválido! Tente novamente.")

# Esse padrão é MUITO comum em programas reais,
# pois garante que o usuário só avance
# quando fornecer dados corretos.

# ==================================================
# QUANDO USAR while True + break?
# ==================================================
#
# Esse padrão é indicado quando:
# - Não sabemos quantas vezes o laço deve repetir
# - O controle de saída depende de uma condição interna
#
# Exemplos práticos:
# - Validação de dados
# - Menus interativos
# - Jogos
# - Sistemas que aguardam eventos
#
# ==================================================
# FIM DA AULA 11 — BREAK E DO...WHILE
# ==================================================
