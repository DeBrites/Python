# Faça um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = float(input('\033[34mDigite um número: \033[m'))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print(f'O número digitado foi \033[33m{n}\033[m, seu dobro é \033[33m{dobro}\033[m, seu triplo é \033[33m{triplo}\033[m e sua raiz quadrada é \033[33m{raiz:.2f}\033[m.')