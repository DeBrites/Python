# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.00.
# C) Qual é o nome do produto mais barato.
soma = caro = menor = 0
print('-'*20)
print('LOJA SUPER BARATA')
print('-'*20)
while True:
	produto = input('Nome do produto: ').strip().upper()
	preco = float(input('Preço: '))
	soma += preco
	if menor == 0 or preco < menor:
		menor = preco
		nome = produto
	if preco > 1000:
		caro += 1	
	continuar = ' '
	while continuar not in 'SN':
		continuar = input('Quer continuar [S/N]? ').strip().upper()[0]
	if continuar == 'N':
		break
print('-'*20)
print(f'O total gasto na compra foi R${soma:.2f}.')
print(f'Temos {caro} produtos que custam mais de R$1000.00.')
print(f'O produto mais barato é {nome} que custa R${menor:.2f}.')