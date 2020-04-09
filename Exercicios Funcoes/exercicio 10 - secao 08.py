"""
10 - Faca uma funcao que receba dois numeros e retorne qual deles e o maior.
"""

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))


def maior(n1, n2):
    if n1 > n2:
        return f'O maior numero e: {n1}'
    return f'O maior numero e: {n2}'


print(maior(n1, n2))

