"""
50 - Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centímetros por ano.
Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.
"""
chico = float(input('Digite o tamanho de chico de Chico: '))
ze = float(input('Digite o tamanho de Zé: '))
cont = 0

while ze < chico:
    chico = (chico + 0.02)
    ze = (ze + 0.03)
    cont += 1

print(chico)
print(ze)
print(f'Zé levará {cont} anos para alcançar Chico.')
