# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
idadevelho = 0
qtdnova = 0
idadetotal = 0
for c in range(1,5):
	nome = input(f'Qual é o nome da {c}º pessoa? ')
	idade = int(input('Qual é a idade dessa pessoa? '))
	print('''E qual é o sexo dela?
		1 - Homem
		2 - Mulher''')
	sex = int(input('Escolha uma das opções acima: '))
	if sex == 1:
		if idadevelho < idade:
			nomevelho = nome
	elif sex == 2:
		if idade < 20:
			qtdnova += 1
	idadetotal += idade
	media = idadetotal/4
print(f'A média de idade do grupo é de {media}, o nome do homem mais velho é {nomevelho}, e existem {qtdnova} mulheres com menos de 20 anos.')