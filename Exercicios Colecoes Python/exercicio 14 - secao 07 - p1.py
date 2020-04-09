"""
14 - Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e escreva na tela.
"""
from collections import defaultdict
vetores = []

for n in range(10):
    vetores.append(int(input(f'Digite o número: ')))
print(f'Estes foram os números digitados: {vetores}')
print('Foram digitados', len(vetores) - len(sorted(set(vetores))), 'números iguais.')

chaves = defaultdict(list)
for key, valor in enumerate(vetores):
    chaves[valor].append(key)
for valor in chaves:
    if len(chaves[valor]) > 1:
        print('Número repetido:', valor)


