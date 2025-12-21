# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
n = int(input('Digite um ano (0 para o ano atual): '))
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(f'O ano de {n} é bissexto.')
else:
    print(f'O ano de {n} não é bissexto.')  