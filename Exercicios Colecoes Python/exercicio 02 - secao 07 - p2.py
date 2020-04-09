"""
2 - Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos.
Escreva ao final a matriz obtida.
"""
matriz = 5
for linha in range(0, matriz):
    for coluna in range(0, matriz):
        if linha == coluna:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
