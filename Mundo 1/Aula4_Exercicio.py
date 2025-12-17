import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é igual a {raiz}')
print(f'O mesmo valor arredondado para cima é {math.ceil(raiz)}')
print(f'O mesmo valor arredondado para baixo é {math.floor(raiz)}')
print('-----------------------------------')

import random
num = random.random()
print(f'Número aleatório entre 0 e 1: {num}')
num = random.randint(1, 10)
print(f'Número aleatório entre 1 e 10: {num}')
print('-----------------------------------')

import pip
pip main(['install', 'emoji'])
import emoji
print(emoji.emojize('Olá, Mundo! :earth_americas:', use_aliases=True))
print(emoji.emojize('Python é :thumbs_up:', use_aliases=True))  