# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
maior = menor = ' '
lista = [int(input('Digite um valor para a Posição 0: '))]
for c in range(1, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
for c in range(0, len(lista)):
    if maior == ' ' and menor == ' ':
        maior = menor = lista[c]
    if maior < lista[c]:
        maior = lista[c]
    if menor > lista[c]:
        menor = lista[c]
print('-='*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, v in enumerate(lista):
    if v == maior:
        print(f'{c}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for c, v in enumerate(lista):
    if v == menor:
        print(f'{c}... ', end='')