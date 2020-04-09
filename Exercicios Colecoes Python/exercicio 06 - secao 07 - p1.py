"""
06 - Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá
ser impresso o maior e o menor elemento do vetor.
"""
vetor = []
for i in range(10):
    vetor.append(int(input(f'Digite o {i} º número: ')))
print(f'Valores digitados: {vetor}')
print('Maior valor digitado:', max(vetor))
print('Menor valor digitado:', min(vetor))
