# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
termo = int(input('Qual é o primeiro termo da PA? '))
razao = int(input('Qual é a razão dela? '))
print('Os 10 primeiros termos dessa PA são: ')
for c in range(0,10):
	print(termo, end=' ')
	termo += razao
