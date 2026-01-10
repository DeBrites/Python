# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
print('-=' * 20)
print('LOJAS GUANABARA')
print('-=' * 20)
produto = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque (10% de desconto)
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20% de juros)''')
escolha = int(input('Escolha a forma de pagamento: '))
if escolha == 1:
    total = produto - (produto * 10 / 100)
elif escolha == 2:
    total = produto - (produto * 5 / 100)
elif escolha == 3:
    total = produto
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS.')
elif escolha == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = produto + (produto * 20 / 100)
    parcela = total / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R$ {parcela:.2f} COM JUROS.')
else:
    total = produto
    print('Opção de pagamento inválida. Tente novamente.')
print(f'Sua compra de R$ {produto:.2f} vai custar R$ {total:.2f} no final.')