# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
peso = float(input('Qual é o seu peso? '))
menor = peso
maior = peso
for numero in range(0,4):
	peso = float(input('Qual é o seu peso? '))
	if peso > maior:
		maior = peso
	elif peso < menor: 
		menor = peso
print(f'O menor peso lido foi de {menor}kg e o maior peso lido foi de {maior}kg.')