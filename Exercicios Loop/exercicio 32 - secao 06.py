"""
32 - Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem
como saída o número de cada dado e a relação entre eles (>,<,=) de cada lançamento
"""
import random
cont = 0
n = 0
n = int(input('Quantas vezes você quer que o dado seja rodado? '))
while cont != n:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    cont += 1
    if d1 > d2:
        print(f'{d1} maior {d2}')
    elif d1 < d2:
        print(f'{d1} menor {d2}')
    else:
        d1 == d2
        print(f'{d1} igual {d2}')


