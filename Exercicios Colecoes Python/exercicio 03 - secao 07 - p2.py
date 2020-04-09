"""
3 - Faça um programa que preencha uma matriz 4 x 4 com o produto do valor da linha da coluna de cada elemento.
Em seguida, imprima na tela.
"""
matriz = []
linha = []
coluna = []
for l in range(4):
    linha.append(int(input('Digite o número para a linha: ')))
    coluna.append(int(input('Digite o número para a coluna: ')))
for c in linha:
    produto = coluna
    matriz.append(produto)
    print('Matriz 4 x 4 com o produto do valor da linha da coluna de cada elemento\n', matriz)
    print()




