"""
54 - Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é primo ou não
"""
from math import sqrt
from itertools import count, islice  # iterador algebra

numero = int(input('Digite um número positivo maior que zero: '))
if numero < 2:
    print('Não primo')
if numero == 2 or numero == 3:
    print('Primo')
for i in islice(count(2), int(sqrt(numero) - 1)):
    if numero % i == 0:
        print('Não primo')
        break
    elif numero % i != 0:
        print('primo')
        break



