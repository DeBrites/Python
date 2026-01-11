# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
soma = 0
numero = int(input('Digite um número inteiro: '))
for c in range(1, numero + 1):
	if numero % c == 0:
		soma += 1
if soma == 2:
	print(f'O número {numero} é um número primo.')
else:
	print(f'O número {numero} não é um número primo.')