# Faça um programa que leia o comprimento de um cateto oposto e de um cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('\033[43;1mDê o valor do cateto oposto: \033[m'))
ca = float(input('\033[43;1mDê o valor do cateto adjacente: \033[m'))
hip = hypot(co, ca)
print(f'\033[1;37;40mA hipotenusa é {hip:.2f}\033[m')