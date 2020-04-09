"""
31 - Faca um programa que leia dois vetores de 10 elementos.
Crie um vetor que seja a uniao entre os 2 vetores, ou seja, que contem os numeros dos dois vetores.
Nao deve conter numeros repetidos.

"""

v1 = []
v2 = []

for x in range(1, 11):
    v1.append(int(input(f'Digite o numero {x}/10: ')))

for z in range(1, 11):
    v2.append(int(input(f'Digite o numero {z}/10: ')))

print(f'Lista 1: {v1}')
print(f'Lista 2: {v2}')

print('Uniao:', list(set(v1) | set(v2)))
