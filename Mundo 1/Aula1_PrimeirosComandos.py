"""
==================================================
AULA 01 — PRIMEIROS COMANDOS EM PYTHON
Mundo 1 — Fundamentos da Linguagem
==================================================

Nesta aula você vai aprender:
- O que são strings (textos)
- Diferença entre texto e números
- Uso do print()
- Operações simples
- Variáveis
- Entrada de dados com input()
- Comentários no código
"""

# ------------------------------------------------
# 1. STRINGS (TEXTOS)
# ------------------------------------------------
# Strings são textos.
# Em Python, textos devem ser delimitados por:
# - Aspas simples: 'texto'
# - Aspas duplas: "texto"
#
# A comunidade Python costuma usar aspas simples.

print('Olá, Mundo!')
print("Python é incrível!")

# ------------------------------------------------
# 2. PRINT() — FUNÇÃO DE SAÍDA
# ------------------------------------------------
# print() é uma função.
# Funções em Python SEMPRE usam parênteses.

print('Essa mensagem aparece no terminal')

# ------------------------------------------------
# 3. NÚMEROS VS TEXTOS
# ------------------------------------------------
# Números NÃO usam aspas.
# Eles são reconhecidos automaticamente como valores numéricos.

print(7 + 4)  # Soma matemática → 11

# Quando colocamos números entre aspas,
# eles passam a ser apenas TEXTO.

print('7+4')  # Não soma, apenas mostra o texto

# ------------------------------------------------
# 4. CONCATENAÇÃO DE STRINGS
# ------------------------------------------------
# Quando usamos + entre strings, ocorre concatenação (junção).

print('7' + '4')  # Resultado: 74

# ------------------------------------------------
# 5. VARIÁVEIS
# ------------------------------------------------
# Variáveis servem para armazenar dados.
# Em Python, toda variável é um objeto.
#
# O sinal "=" significa ATRIBUIÇÃO (recebe).

nome = 'Guanabara'
idade = 18
peso = 80.5

# Para mostrar o conteúdo das variáveis, usamos print()

print(nome, idade, peso)

# ------------------------------------------------
# 6. ENTRADA DE DADOS COM INPUT()
# ------------------------------------------------
# input() permite receber dados digitados pelo usuário.
# Tudo que o usuário digita é recebido como TEXTO (string).

nome = input('Qual é o seu nome? ')
idade = input('Quantos anos você tem? ')
peso = input('Qual é o seu peso? ')

print('Dados informados:')
print(nome, idade, peso)

# ------------------------------------------------
# 7. COMENTÁRIOS NO CÓDIGO
# ------------------------------------------------
# Comentários começam com o símbolo #
# Tudo que estiver após o # é ignorado pelo Python.
#
# Comentários servem para:
# - Explicar o código
# - Organizar o raciocínio
# - Ajudar quem está aprendendo (inclusive você no futuro!)

# Exemplo de comentário:
# print('Esta linha não será executada')

"""
==================================================
FIM DA AULA 01
==================================================
"""
