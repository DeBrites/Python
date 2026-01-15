# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
print('Leitor de números inteiros!')
num = 0
soma = 0
qtd = 0
maior = 0
menor = 0
resposta = 'S'
while resposta in 'Ss':
    num = int(input('Qual numero inteiro? '))
    soma +=  num
    qtd += 1
    if qtd == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / qtd
print(f'Você escolheu {qtd} números inteiros, a média entre eles deu {media:.2f}, o maior valor foi {maior} e o menor foi {menor}.')