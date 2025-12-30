# ============================================
# AULA 4 — MÓDULOS E BIBLIOTECAS EM PYTHON
# Mundo 1 — Fundamentos
# ============================================

# Por padrão, o Python possui um conjunto enxuto de comandos.
# Isso torna a linguagem rápida, simples e fácil de aprender.
#
# Porém, para ampliar suas funcionalidades, o Python utiliza
# MÓDULOS (também chamados de bibliotecas).
#
# Um módulo é um arquivo que contém funções, constantes
# e ferramentas prontas para resolver tarefas específicas.

# --------------------------------------------
# IMPORTANDO UM MÓDULO INTEIRO
# --------------------------------------------

# Para importar um módulo, usamos a palavra-chave "import"
# seguida do nome do módulo.

import math  # Módulo matemático padrão do Python

# Após importar, acessamos suas funções usando:
# nome_do_modulo.funcao()

resultado = math.sqrt(16)  # Raiz quadrada de 16
print('Raiz quadrada de 16:', resultado)  # 4.0

# --------------------------------------------
# CONSTANTES DO MÓDULO MATH
# --------------------------------------------

# O módulo math também possui constantes prontas,
# como o valor de PI (π)

print('Valor de PI:', math.pi)

# --------------------------------------------
# IMPORTANDO APENAS FUNÇÕES ESPECÍFICAS
# --------------------------------------------

# Em vez de importar o módulo inteiro,
# podemos importar apenas o que vamos usar.

from math import pi, sin

area_circulo = pi * (5 ** 2)
print('Área do círculo:', area_circulo)

angulo_seno = sin(pi / 2)
print('Seno de 90 graus:', angulo_seno)

# Quando usamos "from modulo import funcao",
# não precisamos escrever o nome do módulo antes da função.

# --------------------------------------------
# OUTROS MÓDULOS PADRÃO DO PYTHON
# --------------------------------------------

# O Python já vem com vários módulos prontos, como:
# - random   → números aleatórios
# - datetime → datas e horas
# - os       → interação com o sistema operacional

# Exemplo com o módulo random:

import random

numero_aleatorio = random.randint(1, 10)
print('Número aleatório entre 1 e 10:', numero_aleatorio)

# --------------------------------------------
# MÓDULOS DE TERCEIROS (INSTALADOS COM PIP)
# --------------------------------------------

# Além dos módulos padrão, podemos instalar módulos externos.
# Para isso, utilizamos o gerenciador de pacotes "pip".
#
# No terminal (fora do Python), dentro da pasta do projeto:
# pip install emoji

# Após instalar, podemos importar normalmente:

import emoji

print(emoji.emojize('Olá, Mundo! :earth_americas:', use_aliases=True))
print(emoji.emojize('Python é :thumbs_up:', use_aliases=True))

# --------------------------------------------
# DICA IMPORTANTE
# --------------------------------------------

# Sempre que quiser descobrir novos módulos,
# consulte a documentação oficial do Python:
# https://docs.python.org/3/library/

# ============================================
# FIM DA AULA
# ============================================
