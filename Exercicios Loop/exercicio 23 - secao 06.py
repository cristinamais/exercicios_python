"""
23 - Faça um algorítmo que leia um número positivo e imprima seus divisores.
"""

numero = -1
print('Digite um número positivo para imprimir os seus divisores')
print('Digite zero para sair.')
while numero != 0:
    numero = int(input('Digite um numero: '))

    if numero > 0:
        lista = [i for i in range(1, numero // 2 + 1) if numero % i == 0]
        lista.append(numero)
        print(lista)
    else:
        print('Digite apenas números positivos.')

