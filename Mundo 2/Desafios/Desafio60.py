# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input('Digite um número: '))
print(f'O valor dele em fatorial é: {num}! = {num}', end=' ')
soma = num
while num > 0:
	num -= 1
	soma = soma * num
	print(f'x {num}', end=' ')
print(f'= {soma}')