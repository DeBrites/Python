# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = input('Quer continuar [s/n] ? ')
    if resposta in 'Nn':
        break
print('-='*20)
print(f'Você digitou {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}.')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')