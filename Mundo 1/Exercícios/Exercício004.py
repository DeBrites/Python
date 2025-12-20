# Crie um programa que leia o nome completo.

nome = input("Digite seu nome: ")
nome = nome.title()
nome = nome.split()
print(f'Olá, {nome[0]}! Muito prazer em te conhecer. Seu nome completo é {" ".join(nome)}.')
