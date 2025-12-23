# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Me diga o primeiro número: '))
n2 = int(input('Me diga o segundo número: '))
n3 = int(input('Me diga o terceiro número: '))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'O maior número é \033[45m{maior}\033[m e o menor número é \033[45m{menor}\033[m.')