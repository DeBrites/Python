nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Que nome bonito você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
if média >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')
print(f'Sua média foi {média:1f}')
