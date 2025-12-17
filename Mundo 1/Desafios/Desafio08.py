# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'A medida de {m} metros corresponde a:')
print(f'{km} km')
print(f'{hm} hm')
print(f'{dam} dam')
print(f'{dm} dm')
print(f'{cm} cm')
print(f'{mm} mm')