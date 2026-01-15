# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
termo = int(input('Qual é o primeiro termo da PA? '))
razao = int(input('Qual é a razão dela? '))
print('Os 10 primeiros termos dessa PA são: ')
inicio = 1
final = 0
mais = 10
termos = 0
while mais != 0:
	final += mais
	while inicio <= final:
		inicio += 1
		print(f'{termo} →', end=' ')
		termo += razao
		termos += 1
	print('Pausa')
	mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Finalizando com {termos} termos mostrados.')