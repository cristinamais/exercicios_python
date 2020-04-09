"""
09 - Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa.
"""

numeros = []

for n in range(6):
    numeros.append(int(input('Digite o número: ')))
print('Valores lidos na ordem inversa')
for n in sorted(numeros, reverse=True):
    print(n)
