# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
jogadas = vitoria = numero = adv = derrota = 0
print('Jogo do par ou ímpar!')
pergunta = input('Quer jogar par ou impar? [S/N] ').strip().upper()
while pergunta == 'S':
	jogador = int(input('Escolha um número: '))
	adv = randint(0,10)
	jogada = input('Escolhe par ou ímpar? ').strip().upper()[0]
	while jogada not in 'PI': # O while not in é usado para validar a entrada do usuário, garantindo que ele escolha entre 'P' ou 'I'.
		jogada = input('Escolhe par ou ímpar? [par/impar]').strip().upper()[0]
	jogadas += 1
	numero = (jogador + adv)%2
	if jogada == 'P':
		if numero == 0:
			print(f'Meus parabéns, você ganhou... dessa vez. Eu escolhi {adv} e você escolheu {jogador}, deu {jogador+adv}, ou seja, Par.')
			vitoria += 1
		else:
			print(f'AAAAAH EU ESCOLHI {adv} E VOCÊ ESCOLHEU {jogador}, DANDO {jogador+adv}, OU SEJA, ÍMPAR! SEU FRANGOTE!! HAHAEHUA')
			derrota += 1
			break
	if jogada == 'I':
		if numero == 1:
			print(f'Meus parabéns, SORTUDO! Quero ver na próxima... Eu escolhi {adv} e você escolheu {jogador}, deu {jogador+adv}, ou seja, Ímpar.')
			vitoria += 1
		else:
			print(f'HAHAHA EU ESCOLHI {adv} E VOCÊ ESCOLHEU {jogador}, DANDO {jogador+adv}, OU SEJA, PAR! SEU PERDEDOR DE MERDA!! HAHAH')
			derrota += 1
			break
	pergunta = input('Quer  continuar jogando par ou impar? [S/N] ').strip().upper()
print(f'Você realizou {jogadas} jogadas, ganhou {vitoria} vezes e perdeu {derrota}!')