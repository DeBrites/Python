# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('zero','um', 'dois', 'três', 'quatro', 
           'cinco', 'seis', 'sete', 'oito', 'nove', 
           'dez', 'onze', 'doze', 'treze', 'catorze', 
           'quinze', 'dezesseis', ' dezessete', 'dezoito', 
           'dezenove', 'vinte')
while True:
    continuar = ' '
    escolha = int(input('Escolha um número de 0 a 20: '))
    if 0 <= escolha <= 20:
        print(f'O número que você escolheu foi {numeros[escolha]}.')
        while continuar not in 'SN':
            continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            break
    print('Tente mais uma vez.', end = ' ')
print(f'Programa finalizado. Muito obrigado!')