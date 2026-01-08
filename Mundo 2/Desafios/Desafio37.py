# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
x = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'O número {x} em binário é {bin(x)[2:]}.')
elif opcao == 2:
    print(f'O número {x} em octal é {oct(x)[2:]}.')
elif opcao == 3:
    print(f'O número {x} em hexadecimal é {hex(x)[2:]}.')
else:
    print('Opção inválida! Por favor, escolha 1, 2 ou 3.')