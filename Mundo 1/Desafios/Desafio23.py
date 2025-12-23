# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

ano = input("\033[44;33;4mDigite um número de 0 a 9999: ")
print(f"""
      O ano digitado foi {ano}
      Unidade: {ano[3]}
      Dezena: {ano[2]}
      Centena: {ano[1]}
      Unidade de Milhar: {ano[0]}\033[m
""")