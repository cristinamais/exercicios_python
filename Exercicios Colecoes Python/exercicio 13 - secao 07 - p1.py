"""
13 - Fazer um programa para ler 5 valores e, em seguida mostra a posição onde se encontra o maior e o menor.
"""

valoresLidos = []

for n in range(5):
    valoresLidos.append(int(input('Digite os valores: ')))
print('O maior valor está na posição:', valoresLidos.index(max(valoresLidos)))
print('O menor valor está na posição:', valoresLidos.index(min(valoresLidos)))
