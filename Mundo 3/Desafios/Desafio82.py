# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
listapar = lista[:]
listaimpar = lista[:]
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = input('Quer continuar [s/n] ? ')
    if resposta in 'Nn':
        break
print(f'A lista completa é {lista}')
for c, d in enumerate(lista):
    if d % 2 == 0:
        listapar.append(d)
    else:
        listaimpar.append(d)
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')