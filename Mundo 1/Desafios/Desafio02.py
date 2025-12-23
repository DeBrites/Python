# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre a mensagem com a data formatada.
nome = input('\033[90mQual é o seu nome?\033[m')
dia = input('\033[90mQual é o dia em que você nasceu?\033[m')
mes = input('\033[90mQual é o seu mês de nascimento?\033[m')
ano = input('\033[90mEm que ano você nasceu?\033[m')
print(f'Olá \033[31m{nome}\033[m,! Você nasceu no dia \033[31m{dia}\033[m de \033[31m{mes}\033[m de \033[31m{ano}\033[m. Correto?')
