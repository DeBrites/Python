# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
ang = float(input('Mê de um ângulo qualquer: '))
senn = sin(radians(ang))
coss = cos(radians(ang))
tann = tan(radians(ang))
print(f'\033[36mO seno do ângulo de {ang} é {senn:.2f}, o cosseno é {coss:.2f} e a tangente é {tann:.2f}\033[m.')