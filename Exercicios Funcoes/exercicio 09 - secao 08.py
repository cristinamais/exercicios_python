"""
09 - Faca uma funcao que receba a altura e o raio de um ciclindro circular e retorne o volume
do cilindro. O volume de um cilindro circular e calculado por meio da seguinte formula:
v = pi * raio² * altura, onde pi = 3.141592
"""


raio = float(input('Digite o raio do cilindro: '))
altura = float(input('Digite a altura do cilindro: '))

def raio_cilindro(raio, altura):
    v = 3.141592 * (raio ** 2) * altura
    return v


print(raio_cilindro(raio, altura))
