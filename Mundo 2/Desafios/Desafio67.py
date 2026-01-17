# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
c = 0
while True:
	num = int(input('Quer ver a tabuada de qual número? '))
	if num < 0:
		break
	print('-'*20)
	print(f'Tabuada de {num}')
	print('-'*20)
	for c in range(0,11):
		print(f'{num} x {c} = {c*num}')
	print('-'*20)
print('Programa encerrado. Volte sempre!')