# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('\033[46mQual é o seu nome completo? \033[m').strip().upper()
print('SILVA' in nome)