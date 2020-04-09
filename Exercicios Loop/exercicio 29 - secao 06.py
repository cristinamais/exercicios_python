"""
29 - Escreva um programa para calcular o valor da série, para 5 termos.
S = 0 + 1/ 2! + 2/4! + 3/6
"""
from math import factorial

soma = 0
for i in range(1, 5 + 1):
    soma += 1 / factorial(i)
print(f'A soma da série é: {soma:.2f}')