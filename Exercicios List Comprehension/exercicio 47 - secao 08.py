"""
47 - Faca uma funcao que receba uma matriz 4 x 4 e retorne quantos valores maiores que 10 ela possui.
"""
linhas = []
colunas = []
matriz = []

for l in range(4):
    linhas.append(int(input('Digite os numeros da linhas: ')))
for c in range(4):
    colunas.append(int(input('Difite os numeros das colunas: ')))
matriz.append(linhas)
matriz.append(colunas)

print('Matriz:\n', matriz)

def funcao(matriz):  # funcao recebendo a matriz
    n = 10
    m = linhas + colunas
    count = len([i for i in m if i > n])
    return f'Existem " {count} " valores maiores que 10 na matriz'


print(funcao(matriz))











