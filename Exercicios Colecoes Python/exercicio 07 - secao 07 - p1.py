"""
07 - Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.
"""
vetor = []

for n in range(10 + 1):
    vetor.append(int(input(f'Digite os números {n}/10: ')))
m = max(vetor)
for i, x in enumerate(vetor):
    if x == m:
        print(f'O maior número é {m} e a posição que ele se encontra é {i}')

# print(f'O maior número é {max(vetor)} e a posição que ele se encontra é {vetor.index(max(vetor))}')