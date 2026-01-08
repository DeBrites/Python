# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
x = int(input('Qual é o seu ano de nascimento?' ))
y = date.today().year - x
if y < 18:
	f = 18 - y
	print(f'Você poderá se alistar daqui a {f} anos.')
elif y == 18:
	print('Meus parabéns, já pode se alistar e capinar a vontade.')
else:
	p = y - 18
	print(f'Seu tempo de alistamento já passou e foi há {p} anos atrás.')