"""
26 - Faça um algotítmo que encontre o primeiro multiplo de 11, 13 ou 17
após um número dado.
"""

print('O programa vai ficar rodando até que encontre o primeiro multiplo de 11, 13 ou 17')
x = 1
while (x % 11 != 0) and (x % 13 != 0) and (x % 17 != 0):
    x = int(input('Digite um número: '))
    if x % 11 == 0:
        print(f'Número {x} é multiplo de onze')
    if x % 13 == 0:
        print(f'Numero {x} é multiplo de treze')
    if x % 17 == 0:
        print(f'Número {x} é multiplo de dezessete')
