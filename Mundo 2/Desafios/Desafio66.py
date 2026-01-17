# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = qtd = 0
while True:
	num = int(input('Diga um número inteiro: (999 para parar) '))
	if num == 999:
		break
	soma += num
	qtd +=1
print(f'A soma deu {soma} com {qtd} números.')