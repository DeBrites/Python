# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
x = float(input('Valor da casa: R$ '))
y = float(input('Salário do comprador: R$ '))
z = int(input('Em quantos anos ele vai pagar? '))
prestacao = x / (z * 12)
if prestacao <= (y * 0.3):
    print('Empréstimo aprovado!')
    print(f'O valor da prestação será de R$ {prestacao} por mês.')
else:
    print('Empréstimo negado!')
    print(f'O valor da prestação será de R$ {prestacao} por mês, o que excede 30% do seu salário.')