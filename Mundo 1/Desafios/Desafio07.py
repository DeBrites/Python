# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A média entre \033[31m{n1:.1f}\033[m e \033[31m{n2:.1f}\033[m é \033[31m{media:.1f}\033[m.')