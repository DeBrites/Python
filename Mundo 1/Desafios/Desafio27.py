# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ').strip().title().split()
print(f'Seu primeiro nome é {nome[0]} e o seu último nome é {nome[len(nome)-1]}')