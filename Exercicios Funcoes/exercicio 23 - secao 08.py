"""
23 - Escreva uma funcao que gera um triangulo lateral de altura 2*n-1 e n largura. Por exemplo, a saida para 4 = seria
*
**
***
**
*
"""
n = int(input('Digite n numero: '))

def triangulo(*args):
    for i in range(0, n):
        for j in range(0, i + 1):
            print('*', end=' ')
        print("\n")
    for i in range(n, 0, -1):
        for j in range(0, i - 1):
            print('*', end=' ')
        print("\n")

triangulo()
