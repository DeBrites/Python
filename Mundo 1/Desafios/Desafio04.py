#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.
valor = input('\033[31mDigite algo: \033[m')
print('\033[34mO tipo primitivo desse valor é', type(valor))
print('Só tem espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabético?', valor.isalpha())
print('É alfanumérico?', valor.isalnum())
print('Está em maiúsculas?', valor.isupper())
print('Está em minúsculas?', valor.islower())
print(f'Está capitalizada? {valor.istitle()}\033[m')

