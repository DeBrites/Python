# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplo: "A sacada da casa", "A torre da derrota", "O lobo ama o bolo", "Anotaram a data da maratona".
palindromo = False
palin = False
text = input('Digite um palíndromo: ').strip()
texto = text.upper().replace(' ','')
inverso = ''
for letra in range(len(texto) -1, -1, -1):
    inverso += texto[letra]
if inverso == texto:
    palindromo = True
    palin = 'é'
else:
    palin = 'não é'
    palindromo = False
print(f'A frase "{text}" {palin} um palíndromo.')
print(f'A frase invertida fica "{inverso}".')