# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 - O nome com todas as letras maiúsculas e minúsculas.
# 2 - Quantas letras ao todo (sem considerar espaços).
# 3 - Quantas letras tem o primeiro nome.

nome = input("\033[40;30;1mDigite seu nome completo: \033[m")
print(f"\033[41;32;3mSeu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
print(f"Seu primeiro nome tem {len(nome.split()[0])} letras\033[m")