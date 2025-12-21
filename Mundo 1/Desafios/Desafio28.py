# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('=-='*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=-='*20)
sleep(3)
m = randint(0,5)
n = int(input('Adivinhe qual número eu escolhi:'))
print('PROCESSANDO...')
sleep(3)
if n == m:
    print('Parabéns! Você me ganhou hahah!')
else:
    print(f'Errou feio! Escolhi o número {m}.')