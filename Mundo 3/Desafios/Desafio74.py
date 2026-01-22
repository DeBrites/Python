# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depos disso, mostre a listagem dos números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Todos os números sorteados foram: ', end=' ')
for c in numeros:
    print(f'{c} ', end=' ')
print(f'\nO maior número sorteado foi {max(numeros)}.')
print(f'O menor número sorteado foi {min(numeros)}.')