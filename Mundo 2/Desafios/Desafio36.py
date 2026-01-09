# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Em quantos anos ele vai pagar? '))
prestacao = casa / (anos * 12)
if prestacao <= (salario * 0.3):
    print('Empréstimo aprovado! ', end='') # Impede a quebra de linha
    print(f'O valor da prestação será de R$ {prestacao:.2f} por mês.')
else:
    print('Empréstimo negado!', end='')
    print(f'O valor da prestação será de R$ {prestacao:.2f} por mês, o que excede 30% do seu salário.')