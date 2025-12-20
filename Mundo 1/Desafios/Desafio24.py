# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

city = input('Digite o nome de uma cidade: ').strip().split()
print(city[0].upper() == 'SANTO')