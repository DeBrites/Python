Os operadores aritméticos em Python são utilizados para realizar operações matemáticas básicas. Aqui estão os principais operadores aritméticos:

- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Exponenciação (**)
- Divisão (/)
- Divisão inteira (//)
- Módulo (%)

Exemplos de uso:
a = 10
b = 3
soma = a + b          # Adição: resultado é 13
subtracao = a - b     # Subtração: resultado é 7
multiplicacao = a * b  # Multiplicação: resultado é 30
exponenciacao = a ** b # Exponenciação: resultado é 1000 (10 elevado a 3)
divisao = a / b       # Divisão: resultado é 3.3333...
divisao_inteira = a // b # Divisão inteira: resultado é 3
modulo = a % b        # Módulo: resultado é 1 (resto da divisão de 10 por 3)

O operando pode ser um número inteiro (int) ou um número decimal (float) e até uma string (str) em alguns casos, como na adição (concatenação).

Exemplos com diferentes tipos de dados:
x = 5          # int
y = 2.5        # float
z = 'Hello'    # str
soma_int_float = x + y        # Resultado é 7.5 (int + float)
concat_str = z + ' World'     # Resultado é 'Hello World' (str + str)
print('Soma int e float:', soma_int_float)
print('Concatenação de strings:', concat_str)
type_soma = type(soma_int_float)
type_concat = type(concat_str)
print('Tipo da soma (int + float):', type_soma) # Saída: <class 'float'>
print('Tipo da concatenação (str + str):', type_concat) # Saída: <class 'str'>

A ordem de precedência dos operadores aritméticos em Python é a seguinte:

1. Parênteses ()
2. Exponenciação (**) ou pow(a, b) # Eleva 'a' à potência de 'b'
3. Multiplicação (*), Divisão (/), Divisão inteira (//), Módulo (%)
4. Adição (+), Subtração (-)

Exemplo de precedência:
resultado = 3 + 5 * 2 ** 2 - (4 / 2)
# Passo a passo:
# 1. Exponenciação: 2 ** 2 = 4
# 2. Multiplicação: 5 * 4 = 20
# 3. Divisão: 4 / 2 = 2.0
# 4. Adição e Subtração: 3 + 20 - 2.0 = 21.0
print('Resultado da expressão:', resultado) # Saída: 21.0

Outro exemplo:
calculo = (10 + 2 * 3 ** 2) / 4 - 10 % 3
# Passo a passo:
# 1. Exponenciação: 3 ** 2 = 9
# 2. Multiplicação: 2 * 9 = 18
# 3. Adição: 10 + 18 = 28
# 4. Módulo: 10 % 3 = 1
# 5. Divisão: 28 / 4 = 7.0
# 6. Subtração: 7.0 - 1 = 6.0
print('Resultado do cálculo:', calculo) # Saída: 6.0

O igual "==" é um operador de comparação utilizado para verificar se dois valores são iguais. Ele retorna um valor booleano: True se os valores forem iguais e False se não forem. Enquanto isso, o sinal de igual simples "=" é um operador de atribuição usado para atribuir um valor a uma variável.

Exemplos de uso do operador de comparação "==":
a = 5
b = 5
c = 10
print(a == b)  # Saída: True, porque 5 é igual a 5
print(a == c)  # Saída: False, porque 5 não é igual a
print(b == c)  # Saída: False, porque 5 não é igual a 10

No caso de operador aritmético com strings, o operador de adição "+" é usado para concatenar (juntar) duas ou mais strings.

xemplos de concatenação de strings:
str1 = "Olá, "
str2 = "mundo!"
mensagem = str1 + str2
print(mensagem)  # Saída: Olá, mundo!
nome = "Ana"
saudacao = "Bem-vinda, " + nome + "!"
print(saudacao)  # Saída: Bem-vinda, Ana!
idade = 25
info = "Idade: " + str(idade) + " anos"
print(info)  # Saída: Idade: 25 anos

É possível também usar o operador de multiplicação "*" com strings para repetir uma string um determinado número de vezes.

Exemplos de repetição de strings:
repeticao = "Python! " * 3
print(repeticao)  # Saída: Python! Python! Python!
linha = "-" * 10
print(linha)  # Saída: ----------
titulo = "Capítulo 1\n" * 5
print(titulo)  # Saída: Capítulo 1 (repetido 5 vezes, cada um em nova linha)

Há outra forma de replicar informações em Python:

Exemplo:
nome = input('Qual é o seu nome? ')
print(('Prazer em te conhecer, {:<20}!' .format(nome)))
# O código acima alinha o nome à esquerda em um campo de 20 caracteres.
print(('Prazer em te conhecer, {:^20}!' .format(nome)))
# O código acima centraliza o nome em um campo de 20 caracteres.
print(('Prazer em te conhecer, {:>20}!' .format(nome)))
# O código acima alinha o nome à direita em um campo de 20 caracteres.
print(('Prazer em te conhecer, {:*^20}!' .format(nome)))
# O código acima centraliza o nome em um campo de 20 caracteres, preenchendo os espaços vazios com asteriscos (*).
