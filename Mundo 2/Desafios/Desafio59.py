# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
opcao = 0
while opcao != 5:
    print("""Escolha uma opção:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa""")
    opcao = int(input("Qual é a sua opção: "))
    if opcao == 1:
        print(f"A soma de {n1} + {n2} é {n1 + n2}.")
    elif opcao == 2:
        print(f"A multiplicação de {n1} * {n2} é {n1 * n2}.")
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        else:
            maior = "ambos são iguais"
        print(f"O maior valor é: {maior}.")
    elif opcao == 4:
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Saindo do programa...")
        sleep(3)
    else:
        print("Opção inválida! Tente novamente.")
    print("-=" * 20)
print("Programa finalizado. Volte sempre!")