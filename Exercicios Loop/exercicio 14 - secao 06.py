"""
14 - Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente.
"""
n = int(input('Digite um número: '))

for par in range(n, 0, -1):
    print(2 * par)
