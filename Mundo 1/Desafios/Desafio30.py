# Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('\033[47mDigite um número inteiro: \033[m'))
if n % 2 == 0:
    print(f'O número {n} é PAR.')
else:
    print(f'O número {n} é ÍMPAR.')