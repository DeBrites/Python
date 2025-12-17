# Faça um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = float(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print(f'O número digitado foi {n}, seu dobro é {dobro}, seu triplo é {triplo} e sua raiz quadrada é {raiz:.2f}.')