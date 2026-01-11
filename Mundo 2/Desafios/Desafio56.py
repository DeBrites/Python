# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
idadevelho = 0
qtdnova = 0
idadetotal = 0
for c in range(1, 5):
	print('----- {}ª PESSOA -----'.format(c))
	nome = str(input('Nome: ')).strip()
	idade = int(input('Idade: '))
	sexo = str(input('Sexo [M/F]: ')).strip().upper()
	idadetotal += idade
	if sexo == 'M':
		if idade > idadevelho:
			idadevelho = idade
			nomevelho = nome
	elif sexo == 'F':
		if idade < 20:
			qtdnova += 1
media = idadetotal / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho, idadevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(qtdnova))