# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
termo = int(input('Qual é o primeiro termo da PA? '))
razao = int(input('Qual é a razão dela? '))
print('Os 10 primeiros termos dessa PA são: ')
c = 1
while c <= 10:
	c += 1
	print(f'{termo} →', end=' ')
	termo += razao
print('FIM')
# Saída:
# Gerador de PA
# Primeiro termo: 5
# Razão da PA: 3
# 5 → 8 → 11 → 14 → 17 → 20 → 23 → 26 → 29 → 32 → FIM