No Python é possível manipular textos de diversas formas utilizando métodos embutidos nas strings. A seguir, apresento alguns exemplos comuns de manipulação de textos:

Na frase 'Curso em Vídeo de Python', podemos aplicar os seguintes métodos:

Um deles é o Fatiamento (Slicing), que permite acessar partes específicas de uma string utilizando índices. Por exemplo:

texto = 'Curso em Vídeo de Python'
# Possui 27 caracteres e índices de 0 a 26
print(texto[9])  # Saída: V
print(texto[9:14])  # Saída: Vídeo
print(texto[:5])  # Saída: Curso
print(texto[::5])  # Saída: C eVd y, pegando de 5 em 5 caracteres
print(texto[10:])  # Saída: ídeo de Python
print(texto[9::3])  # Saída: VePh, pegando de 3 em 3 caracteres a partir do índice 9
print(texto[9:21:2])  # Saída: Vdo ePto, pegando de 2 em 2 caracteres
print(texto[::-1])  # Saída: nohtyP ed oédiV me osruC, invertendo a string

Outro método útil é o Análise de Texto, que permite obter informações sobre a string. Por exemplo:
print(len(texto))  # Saída: 27, número de caracteres
print(texto.count('o'))  # Saída: 3, número de ocorrências da letra 'o'
print(texto.count('o', 0, 13))  # Saída: 1, contando 'o' apenas até o índice 12
print(texto.find('Vídeo'))  # Saída: 9, índice onde começa a palavra 'Vídeo'
print(texto.find('Android'))  # Saída: -1, indicando que a palavra não foi encontrada
print('Curso' in texto)  # Saída: True, verificando se 'Curso' está na string
print('Android' in texto)  # Saída: False, verificando se 'Android' está na string

Também podemos utilizar Métodos de Transformação para modificar a string. Por exemplo:
print(texto.replace("Python", "Android"))  # Saída: Curso em Vídeo de Android
print(texto.upper())  # Saída: CURSO EM VÍDEO DE PYTHON
print(texto.lower())  # Saída: curso em vídeo de python
print(texto.capitalize())  # Saída: Curso em vídeo de python
print(texto.title())  # Saída: Curso Em Vídeo De Python
print(texto.strip())  # Remove espaços extras no início e no fim
print(texto.rstrip())  # Remove espaços extras à direita
print(texto.lstrip())  # Remove espaços extras à esquerda
print(texto.split())  # Divide a string em uma lista de palavras
print("-".join(texto))  # Junta os caracteres da string com '-' entre eles. Exemplo: C-u-r-s-o- -e-m- -V-í-d-e-o- -d-e- -P-y-t-h-o-n

Para combinar os métodos, podemos fazer o seguinte:
print(texto.split()[2].upper())  # Saída: VÍDEO, pegando a terceira palavra e convertendo para maiúsculas

É possível fazer um print com três aspas para textos longos ou com quebras de linha:
print("""Curso em Vídeo de Python
Aprenda Python de forma fácil e divertida!
Domine a programação com exemplos práticos.""")