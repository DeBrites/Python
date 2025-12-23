# Escreva um programa que converta uma temperatura digitada em graus Celsius para graus Fahrenheit.
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (celsius * 9/5) + 32
print(f'A temperatura de \033[31m{celsius:.1f}°C\033[m corresponde a \033[31m{fahrenheit:.1f}°F\033[m.')