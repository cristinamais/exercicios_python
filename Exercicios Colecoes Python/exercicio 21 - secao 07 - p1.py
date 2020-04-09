"""
21 - Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada. Crie um novo vetor
denominado C calculando C = A-B. Mostre na tela os dados do vetor C.
"""
vetorA = []
vetorB = []
vetorC = []

for a in range(10):
    vetorA.append(int(input(f'Digite {a}º número para o vetor A: ')))
for b in range(10):
    vetorB.append(int(input(f'Digite {b}º número para o vetor B: ')))

print('Vetor A:', vetorA)
print('Vetor B:', vetorB)

vetorC = [vetorA[i]-vetorB[i] for i in range(min(len(vetorA), len(vetorB)))]

print(f'Vetor C:', vetorC)



