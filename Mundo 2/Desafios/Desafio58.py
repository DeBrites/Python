# Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
soma = 1
print('\033[31m=-=\033[m'*20)
print('\033[33mVou pensar em um número entre 0 e 10. Tente adivinhar...\033[m')
print('\033[31m=-=\033[m'*20)
sleep(3)
m = randint(0,10)
n = int(input('\033[33mAdivinhe qual número eu escolhi:\033[m'))
print('\033[33mPROCESSANDO...\033[m')
sleep(3)
while n != m:	
    print('\033[31;1mErrou feio! Tente de novo!.\033[m')
    if n < m:
        print('\033[34mPense mais...\033[m')
        soma += 1
    else:
        print('\033[34mPense menos...\033[m')
        soma += 1
    n = int(input('\033[33mAdivinhe qual número eu escolhi:\033[m'))
    print('\033[33mPROCESSANDO...\033[m')
    sleep(3)
if soma == 1:
    print(f'\033[34mCARACA, DE PRIMEIRA??!\033[m')
    print(f'\033[34mMeus Parabéns! Eu escolhi esse mesmo, o número {m}. Você me ganhou com uma só tentativa, INCRÍVEL!!!\033[m')
else:
    print(f'\033[34mMeus Parabéns! Eu escolhi esse mesmo, o número {m}. Você me ganhou com {soma} tentativas hahah!\033[m')

    