Os programas de Python por padrão tem um conjunto limitado de comandos para que a linguagem seja rapida e fácil de aprender. Porém, existem diversos módulos (bibliotecas) que estendem as funcionalidades da linguagem, permitindo que você utilize funções prontas para realizar tarefas específicas.

Para utilizar um módulo em Python, você pode usar a palavra-chave `import` seguida do nome do módulo. Por exemplo, para importar o módulo `math`, que fornece funções matemáticas avançadas, você faria o seguinte:
import math

Depois de importar o módulo, você pode acessar suas funções e constantes usando a sintaxe `modulo.funcao`. Por exemplo, para calcular a raiz quadrada de um número usando o módulo `math`, você faria:
resultado = math.sqrt(16)
print(resultado)  # Saída: 4.0

Além disso, você pode importar apenas funções específicas de um módulo usando a sintaxe `from modulo import funcao`. Por exemplo:
from math import pi, sin
area_circulo = pi * (5 ** 2)
print(area_circulo)  # Saída: 78.53981633974483
angulo_seno = sin(pi / 2)
print(angulo_seno)  # Saída: 1.0

Existem muitos módulos padrão em Python, como `random` para gerar números aleatórios, `datetime` para manipulação de datas e horas, e `os` para interagir com o sistema operacional. Você também pode instalar módulos adicionais usando o gerenciador de pacotes `pip`.

Aqui está um exemplo de como usar o módulo `random` para gerar um número aleatório entre 1 e 10:
import random
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio) # Saída: um número aleatório entre 1 e 10

Existem muitos outros módulos disponíveis, e você pode explorar a documentação oficial do Python para descobrir mais sobre eles: https://docs.python.org/3/library/

E para importar módulos de terceiros, como o `emoji`, você pode instalá-los usando pip no terminal do seu computador em uma pasta de projeto:
pip install emoji
Depois de instalado, você pode importar e usar o módulo `emoji` assim:
import emoji
print(emoji.emojize('Olá, Mundo! :earth_americas:', use_aliases=True))
print(emoji.emojize('Python é :thumbs_up:', use_aliases=True))