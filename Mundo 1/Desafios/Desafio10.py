# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('\033[33mDigite quanto dinheiro você tem na carteira: R$\033[m'))
dolar = real / 5.40
print(f'Com \033[31mR${real:.2f}\033[m você pode comprar \033[31mUS${dolar:.2f}\033[m.')