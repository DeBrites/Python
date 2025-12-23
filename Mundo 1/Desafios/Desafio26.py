# Faça um programa que leia uma frase pelo teclado e mostre:
# 1 - Quantas vezes aparece a letra "A".
# 2 - Em que posição ela aparece a primeira vez.
# 3 - Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip().upper()
print(f'A letra "A" aparece \033[31m{frase.count("A")}\033[m vezes na frase.')
print(f'A letra "A" aparece pela primeira vez na posição \033[31m{frase.find("A") + 1}\033[m.')
print(f'A letra "A" aparece pela última vez na posição \033[31m{frase.rfind("A") + 1}\033[m.')