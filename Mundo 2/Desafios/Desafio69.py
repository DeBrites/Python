# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.
pessoas = mulheres = homens = 0
while True:
	idade = int(input('Qual é a sua idade? '))
	sexo = input('Qual é o sexo [M/F]? ').strip().upper()[0]
	while sexo not in 'MF':
		sexo = input('Dados inválidos. Por favor, informe o sexo [M/F]: ').strip().upper()[0]
	if idade > 18:
		pessoas += 1
	if sexo == 'M':
		homens += 1
	if sexo == 'F' and idade < 20:
		mulheres += 1
	print('-'*20)
	print(f'IDADE: {idade} ')
	print(f'SEXO: {sexo} ')  
	print('-'*20)
	pergunta = input('Que cadastrar mais uma pessoa [S/N]? ').strip().upper()[0]
	while pergunta not in 'SN':
		pergunta = input('Dados inválidos. Por favor, deseja cadastrar mais uma pessoa [S/N]? ').strip().upper()[0]
	if pergunta == 'N':
		break
print(f'FINALIZADO!')
print(f'Total de pessoas com mais de 18 anos: {pessoas}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres}')	