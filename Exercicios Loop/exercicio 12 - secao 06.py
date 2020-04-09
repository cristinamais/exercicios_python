"""
12 - Faça um programa que leia um número inteiro positivo N e imprima todos os
números naturais de 0 até N em ordem decrescente.
"""

numero = int(input('Informe um número: '))
soma = 0
for n in range(numero + 1):
    soma = numero - n
    print(f'{soma}')

"""
#Essa é a solução que o professor deu:
numero = int(input('Informe um número: '))
for n in range(numero,0 , - 1):
    print(f'{n}')
    
"""