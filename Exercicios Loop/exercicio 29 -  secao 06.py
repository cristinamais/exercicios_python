"""
29 - Escreva um programa para calcular o valor da série, para 5 termos.
S = 0+1/2!+2/4!+3/6!
"""
from math import factorial

numero = 1
soma = 0
print('Digite zero para sair.')
while numero > 0:
    numero = int(input('Digite um número: '))
    for i in range(1, numero + 1):
        soma += 1 / factorial(i)
    print(f'A soma da série do número {numero} é: {soma:.2f}')
