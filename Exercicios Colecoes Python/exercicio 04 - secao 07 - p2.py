"""
4 - Leia uma matriz 4 x 4, imprima a matriz e retore a localização (linha e a coluna) do maior valor.
"""
matriz = []

for l in range(4):
    valorl = int(input('Qual é o número da linha: '))
    linha = []
    for c in range(4):
        valor = int(input('Digite o valor do número da coluna: '))
        linha.append(valor)

    matriz.append(linha)
    print(matriz)
print('Os maiores valores de cada linha:')
for item in matriz:
    print(max(item))
