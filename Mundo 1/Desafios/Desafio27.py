# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ').strip().title().split()
print(f'Seu primeiro nome é \033[47m{nome[0]}\033[m e o seu último nome é \033[47m{nome[len(nome)-1]}\033[m')