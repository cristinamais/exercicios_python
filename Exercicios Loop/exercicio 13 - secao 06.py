"""
13 - Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente.
2 * par
2 * 0 = 0
2 * 1 = 2
2 * 2 = 4 
2 * 3 = 6...

"""
n = int(input('Digite um número: '))

for par in range(n + 1):
    print(2 * par)
