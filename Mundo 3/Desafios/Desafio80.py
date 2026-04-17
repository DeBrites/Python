# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
minhalista = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0 or n > minhalista[-1]:
        minhalista.append(n)
        print('Adicionando à última posição da lista...')
    else:
        pos = 0
        while pos < len(minhalista):
            if n <= minhalista[pos]:
                minhalista.insert(pos, n)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1 
print(minhalista)

# Programa com infinitos valores numéricos
#minhalista = []
#pergunta = 's'
#c = int(input('Digite um número: '))
#while pergunta == 's':
#    print(c)                                        
#    if minhalista == []:
#        minhalista.append(c) 
#        maior = c
#    else: 
#        if c in minhalista:
#            print('Valor duplicado! Não será adicionado...')
#        else:
#            inserido = False
#            for d, v in enumerate(minhalista):
#                if v >= c:
#                    minhalista.insert(d,c)
#                    inserido = True
#                    break
#            if not inserido:
#                minhalista.append(c) 
#    print(minhalista)
#    pergunta = input('Quer continuar s/n? ')
#    if pergunta == 's':
#        c = int(input('Digite um número: '))