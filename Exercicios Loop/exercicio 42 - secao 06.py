"""
42 - Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores lidos,
o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.
"""

import math

a, b, c = [int(x) for x in input('Digite três valores: ').split()]
while a and b and c > 0:
    q = a * a
    cubo = b ** 3
    r = math.sqrt(c)
    print(f'O Quadrado do número {a} é {q}, o Cubo do número {b} é {cubo} e a Raiz Quadrada do número {c} é {r:.2f}')
    a, b, c = [int(x) for x in input('Digite três valores: ').split()]
print('<<<Finalizando!! Você digitou um valor negativo ou zero.>>>')

