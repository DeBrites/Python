# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas. 
d = float(input('Digite a distância da viagem em km: '))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print(f'O preço da passagem é de R${p:.2f}.')