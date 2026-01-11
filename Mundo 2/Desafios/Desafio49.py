# Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número para ver sua tabuada: '))
print('\033[31m-\033[m' * 12)
for c in range(0,11):
	print(f'\033[32m{c} x {n} = {n * c}\033[m')
print('\033[31m-\033[m' * 12)