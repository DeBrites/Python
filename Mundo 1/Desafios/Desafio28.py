# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('\033[31m=-=\033[m'*20)
print('\033[33mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[31m=-=\033[m'*20)
sleep(3)
m = randint(0,5)
n = int(input('\033[33mAdivinhe qual número eu escolhi:\033[m'))
print('\033[33mPROCESSANDO...\033[m')
sleep(3)
if n == m:
    print('\033[34mParabéns! Você me ganhou hahah!\033[m')
else:
    print(f'\033[31;1mErrou feio! Escolhi o número {m}.\033[m')