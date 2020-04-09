"""
30 - Faca um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a
interseccao entre os 2 vetores amteriores, ou seja, que contem apenas os numeros que
estao em ambos os vetores. Nao deve conter numeros repetidos.

"""

v1 = []
v2 = []

for a in range(1, 11):
    v1.append(int(input(f'Digite o {a}/10: ')))

for b in range(1, 11):
    v2.append(int(input(f'Digite o {b}/10: ')))

print(f'Este e o vetor 1: {v1}')
print(f'Este e o vetor 2: {v2}')

dicionario1 = {}.fromkeys(v1, 'a')
dicionario2 = {}.fromkeys(v2, 'b')

#print(f'Este e o vetor 1: {dicionario1}'), aqui printa o dicionario
#print(f'Este e o vetor 2: {dicionario2}'), aqui printa o dicionario

setA = set(dicionario1)
setB = set(dicionario2)

print('Interseccao entre dicionario1 e dicionario2:')
print(setA.intersection(setB))
