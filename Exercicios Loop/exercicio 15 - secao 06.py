"""
15 - Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N em ordem crescente.
"""

n = int(input('Digite um número: '))

for num in range(n + 1):
    if num % 2 != 0:
        print(num)
