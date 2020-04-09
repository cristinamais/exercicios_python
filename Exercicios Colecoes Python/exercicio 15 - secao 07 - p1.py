"""
15 - Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos
"""

vetores = []

for n in range(20):
    vetores.append(int(input(f'Digite o número: ')))
print(f'Estes foram os números digitados: {vetores}')
print('Estes são os números sem repetição:', sorted(set(vetores)))
