# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: R$'))
desconto = preco * 0.05
novo_preco = preco - desconto
print(f'O novo preço do produto com 5% de desconto é \033[32mR${novo_preco:.2f}\033[m.')