"""
33 - Faca um programa que leia um vetor de 15 posicoes e o compacte, ou seja, elimine as posicoes com valor zero.
Para isso, todos os elementos a frente do valor zero, devem ser movidos uma posicao para tras no vetor.
"""

"""
vetor = []
count = 0

for x in range(1, 16):
    vetor.append(int(input(f'Digite o {x}/15: ')))

n = len(vetor)

for i in range(n):
    if vetor[i] != 0:
        vetor[count] = vetor[i]
        count += 1

while n > count:
    vetor[count] = 0
    count += 1
print(vetor)  # [5, 6, 9, 8, 10, 15, 33, 22, 66, 99, 10, 100, 0, 0, 0]
Este os zeros vao para tras
"""

from itertools import compress, repeat, chain

vetor = []

for x in range(1, 16):
    vetor.append(int(input(f'Digite o {x}/15: ')))

# usando list.count e itertools.compress
y = [0] * vetor.count(0)
y.extend(compress(vetor, vetor))
print(y)
