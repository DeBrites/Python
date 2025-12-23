# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário do funcionário: R$'))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f'O novo salário do funcionário com 15% de aumento é \033[32mR${novo_salario:.2f}\033[m.')