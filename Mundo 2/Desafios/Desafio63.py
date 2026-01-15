# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - ...
n = int(input('Digite quantos termos da Sequência de Fibonacci você quer ver: '))
t1 = 0
t2 = 1
print('~' * 30)
print('Sequência de Fibonacci:')
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Fim')
print('~' * 30)