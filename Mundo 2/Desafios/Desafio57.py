# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    print("Sexo inválido!")
    sexo = input("Por favor, digite 'M' para masculino ou 'F' para feminino: ").strip().upper()[0]
print("Sexo registrado com sucesso:", sexo)