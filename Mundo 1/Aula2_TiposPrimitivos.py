Cada variável que "recebe" um valor, esse valor possui um tipo de dado. 
Os tipos de dados mais comuns no Python são:
- int (inteiro)
- float (número decimal)
- bool (booleano - True ou False)
- str (string - sequência de caracteres)

Exemplos:
n1 = 5          # int
n2 = 3.14       # float
ligado = True   # bool
nome = 'Maria'  # str

Podemos verificar o tipo de dado de uma variável utilizando a função type().

Exemplos:
print(type(n1))      # Saída: <class 'int'>
print(type(n2))      # Saída: <class 'float'>
print(type(ligado))  # Saída: <class 'bool'>
print(type(nome))    # Saída: <class 'str'>

Além disso, podemos converter entre tipos de dados utilizando funções como int(), float(), str(), etc

Exemplos:
idade_str = '25'
idade_int = int(idade_str)  # Converte string para inteiro
altura_float = float('1.75') # Converte string para float
peso_str = '70.5'
peso_float = float(peso_str)  # Converte string para float
print(idade_int, type(idade_int))      # Saída: 25 <class 'int'>
print(altura_float, type(altura_float))# Saída: 1.75 <class 'float'>
print(peso_float, type(peso_float))    # Saída: 70.5 <class 'float'>

Essas conversões são úteis quando recebemos dados do usuário, pois a função input() sempre retorna uma string.

Exemplo:
idade = int(input('Digite sua idade: '))  # Converte a entrada para inteiro
altura = float(input('Digite sua altura: '))  # Converte a entrada para float
print('Idade:', idade, 'Altura:', altura)

Além disso, podemos formatar strings utilizando f-strings para incluir variáveis dentro de mensagens.
Exemplo:
nome = 'Ana'
idade = 30
print(f'Nome: {nome}, Idade: {idade}')  # Saída: Nome: Ana, Idade: 30

Ou com o método format() que é uma sintaxe mais antiga:
print('Nome: {}, Idade: {}'.format(nome, idade))  # Saída: Nome: Ana, Idade: 30

