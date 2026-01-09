# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print('-=' * 20)
print('JOKENPÔ')
print('-=' * 20)
print(''' VAMOS JOGAR!
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA
      Escolha uma opção: ''')
sleep(3)
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(2)
print('E TESOU...')
sleep(3)
print('RA!!!')
jogador = int(input('Qual é a sua jogada? '))
rival = randint(0, 2)
if jogador == 0:
    print('Você escolheu PEDRA')
    if rival == 0:
        print('O computador escolheu PEDRA')
        print('EMPATE!')
    elif rival == 1:
        print('O computador escolheu PAPEL')
        print('VOCÊ PERDEU!')
    elif rival == 2:
        print('O computador escolheu TESOURA')
        print('VOCÊ VENCEU!')
elif jogador == 1:
    print('Você escolheu PAPEL')
    if rival == 0:
        print('O computador escolheu PEDRA')
        print('VOCÊ VENCEU!')
    elif rival == 1:
        print('O computador escolheu PAPEL')
        print('EMPATE!')
    elif rival == 2:
        print('O computador escolheu TESOURA')
        print('VOCÊ PERDEU!')
elif jogador == 2:
    print('Você escolheu TESOURA')
    if rival == 0:
        print('O computador escolheu PEDRA')
        print('VOCÊ PERDEU!')
    elif rival == 1:
        print('O computador escolheu PAPEL')
        print('VOCÊ VENCEU!')
    elif rival == 2:
        print('O computador escolheu TESOURA')
        print('EMPATE!')
else:
    print('Jogada inválida! Tente novamente.')