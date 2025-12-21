# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r = float(input('Me diga o comprimento da reta 1: '))
s = float(input('Me diga o comprimento da reta 2: '))
t = float(input('Me diga o comprimento da reta 3: '))
if r < s + t and s < r + t and t < r + s:
    print(f'Com essas retas {r}, {s} e {t}, é possível formar um triângulo.')
else:
    print('Com essas retas não é possível formar um triângulo.')