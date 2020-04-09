"""
12 - Ler um número inteiro. Se o número lido for negativo, escreva a mensagem
'Número inválido'. Se o número for positivo, calcule o logarítmo deste número.
"""

from math import log

num = int(input("Digite um número inteiro: "))

if num > 0:
    print(f'Logarítmo de número {log(num)}.')

else:
    print('Número inválido.')
