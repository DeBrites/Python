# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
menor = 0
maior = 0
from datetime import date
anoatual = date.today().year
for numero in range(0,7):
	nascimento = int(input('Qual é o ano de nascimento? '))
	idade = anoatual - nascimento
	if idade < 18:
		menor += 1
	else:
		maior += 1
print(f'{menor} pessoas não atingiram a maioridade e {maior} já atingiram a maioridade.')