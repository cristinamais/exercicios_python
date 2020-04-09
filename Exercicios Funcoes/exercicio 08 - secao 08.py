"""
08 - Sejam a e b os catetos de um triangulo, onde a hipotenusa e obtida pela equacaoÇ
hipotenusa = raiz quadrada de a² + b². faca uma funcao que receba os valores de a e b e calcule o
valor da hipotenusa atraves da equacao.
"""

from statistics import sqrt

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

def hipotenusa(a, b):
    h = sqrt(a**2 + b**2)
    return h


print(hipotenusa(a, b))
