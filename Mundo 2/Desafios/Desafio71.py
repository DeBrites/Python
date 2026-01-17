# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. As cédulas disponíveis serão de R$50, R$20, R$10 e R$1.
print('=' * 30)
print('{:^30}'.format('BANCO CAGIOTA'))
print('=' * 30)
saque = int(input('Qual valor você quer sacar? R$ '))
nota = 50
cedula = 0
print(f'Você vai sacar R$ {saque} reais.')
while True:
    if saque >= nota:
        saque -= nota
        cedula += 1
    else:
        if cedula > 0:
            print(f'Total de {cedula} cédulas de R$ {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        cedula = 0
        if saque == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CAGIOTA! Tenha um bom dia!')
print('=' * 30)