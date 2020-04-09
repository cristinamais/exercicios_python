"""
16 - Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1 até N em ordem decrescente.
"""
n = int(input('Digite um número: '))

for num in range(n, 0, - 1):
    if num % 2 != 0:
        print(num)
