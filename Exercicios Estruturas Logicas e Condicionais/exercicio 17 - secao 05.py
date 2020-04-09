"""
17 - Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = ((basemaior + basemenor) * altura) / 2. Lembre-se a base maior e a base menor
devem ser números maiores que zero.
"""

base_maior = float(input("Digite o valor da base maior: "))
base_menor = float(input("Digite o valor da base menor: "))
altura = float(input("Digite o valor da altura: "))

if base_maior <= 0:
    print('A base maior não pode ser calculada.')

elif base_menor <= 0:
    print('A base menor não pode ser calculada.')

else:
    area_trapezio = ((base_maior + base_menor) * altura) / 2
    print(f'A área desse trapézio é de: {area_trapezio}.')
    
