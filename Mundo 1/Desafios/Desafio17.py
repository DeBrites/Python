# Faça um programa que leia o comprimento de um cateto oposto e de um cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Dê o valor do cateto oposto: '))
ca = float(input('Dê o valor do cateto adjacente: '))
hip = hypot(co, ca)
print(f'A hipotenusa é {hip:.2f}')