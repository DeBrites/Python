# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print('Leitor de números inteiros!')
num = 0
soma = 0
qtd = 0
while num != 999:
	num = int(input('Qual numero inteiro? (Digiite 999 para parar) '))
	soma +=  num
	qtd += 1
if num == 999:
	soma -= 999
	qtd -= 1
print(f'Você escolheu {qtd} números inteiros e a soma entre eles deu {soma}.')
