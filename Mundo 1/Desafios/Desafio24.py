# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

city = input('\033[45;3mDigite o nome de uma cidade: \033[m').strip().split()
print(city[0].upper() == 'SANTO')