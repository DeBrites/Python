No Python existem estruturas sequenciais e estruturas condicionais que permitem controlar o fluxo de execução do código com base em condições específicas. As principais estruturas condicionais são: if, elif e else.

Aqui estão alguns exemplos de como utilizar essas estruturas condicionais:

# Exemplo 1: Estrutura condicional simples
idade = 18
if idade >= 18: # Verifica se a idade é maior ou igual a 18
    print('Você é maior de idade.')

# Exemplo 2: Estrutura condicional com else
idade = 16
if idade >= 18:
    print('Você é maior de idade.')
else: 
    print('Você é menor de idade.')

# Exemplo 3: Estrutura condicional com elif
nota = 85
if nota >= 90:# Verifica se a nota é maior ou igual a 90
    print('Você recebeu um A.')
elif nota >= 80:
    print('Você recebeu um B.')
elif nota >= 70:
    print('Você recebeu um C.')
else:
    print('Você precisa melhorar.')

# Exemplo 4: Estrutura condicional aninhada
numero = 10
if numero > 0:
    if numero % 2 == 0: 
        print('O número é positivo e par.')
    else:
        print('O número é positivo e ímpar.')
else:
    print('O número é negativo ou zero.')
# Exemplo 5: Uso de operadores lógicos em condições
idade = 20
renda = 3000
if idade >= 18 and renda >= 2500:
    print('Você é elegível para o empréstimo.')
if idade < 18 or renda < 2500:
    print('Você não é elegível para o empréstimo.')

# Exemplo 6: Condição com operador not
tem_carteira_de_trabalho = False
if not tem_carteira_de_trabalho:
    print('Você precisa tirar a carteira de trabalho.')

# Exemplo 7: Usando condição ternária
idade = 22
status = 'Maior de idade' if idade >= 18 else 'Menor de idade'
print(status)

# Exemplo 8: Verificando se uma string está vazia
nome = ''
if not nome:
    print('O nome não pode estar vazio.')

# Exemplo 9: Verificando se um número está em um intervalo
numero = 15
if 10 <= numero <= 20:
    print('O número está entre 10 e 20.')

# Exemplo 10: Usando pass em uma condição
idade = 25
if idade < 18:
    pass  # Ainda não implementado
else:
    print('Você é maior de idade.')
    
