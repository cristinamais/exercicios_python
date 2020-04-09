"""
1 - Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
"""
linha = []
coluna = []
n = 10
for l in range(4):
    linha.append(int(input(f'Digite o {l}/4 número para as linhas: ')))
for c in range(4):
    coluna.append(int(input(f'Digite o {c}/4 número para as colunas: ')))

print(f'Números da linha: {linha}. Números da coluna: {coluna}')

matriz = linha + coluna
count = len([i for i in matriz if i > n])
print(f'Números maiores que 10 são: {count}')
