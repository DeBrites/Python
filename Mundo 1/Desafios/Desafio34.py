# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.Para salários superiores a R$1250,00, calcule um aumento de 10%.Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Qual é o seu salário? '))
if s > 1250:
    ns = s + (s*0.10)
else:
    ns = s + (s*0.15)
print(f'Seu novo salário é de \033[41mR${ns:.2f}\033[m')