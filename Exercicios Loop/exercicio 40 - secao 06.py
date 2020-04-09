"""
40 - Elabore um programa que faça leitura de vários números inteiros, até que se digite um número
negativo. O programa tem que retornar o maior e o menor número lido.
"""
lista = []

numero = int(input(f'Digite o número: '))
while numero >= 0:
    lista.append(numero)
    numero = int(input(f'Digite o número: '))
print('O maior valor da lista é:', max(lista), '\nO menor valor da lista é:', min(lista))


