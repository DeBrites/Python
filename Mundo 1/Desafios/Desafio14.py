# Escreva um programa que converta uma temperatura digitada em graus Celsius para graus Fahrenheit.
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (celsius * 9/5) + 32
print(f'A temperatura de {celsius:.1f}°C corresponde a {fahrenheit:.1f}°F.')