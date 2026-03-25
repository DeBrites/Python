# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
listanumerica = []
print(listanumerica)
s = 's'
while s == 's':
    c = int(input('Cadastre um valor numérico: '))
    if c in listanumerica:
        print('Valor duplicado! Não vou adicionar...')
    else:
        listanumerica.append(c)
    s = input('Você quer cadastrar mais um número [s/n]? ')
listanumerica.sort()
print('-='*20)
print(f'A lista completa foi {listanumerica}')
