"""
05 - Faca uma funcao e um programa de teste para o calculo do volume de uma esfera.
Sendo que o raio e passado por parametro.
V = 4/3*pi*R³

# Gerar random intenger values:

from random import randint

for _ in range(10):
    valor = randint(0, 10)
    print(valor)

"""


x = float(input('Digite o volume da esfera: '))
z = float(input('Digite a medida do raio da esfera: '))
y = 3.14159

def teste():
    v = 4 / 3 * y * z ** 3
    return v
# 90 - 6

print(f'O volume desta esfera é: {teste():.2f} cm³')


