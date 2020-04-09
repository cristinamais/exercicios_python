"""
48 - Faça um programa que some os termos de valor par da sequencia de Fibonacci, cujos valores não ultrapassem quatro milhões
"""

a, b = 0, 1
while b < 3000000:
    if b % 2 == 0:
        print(b)
    a, b = b, a+b
print(f'Soma dos valores pares da sequancia de Fibonacci que não ultrapassam quatro milhões: {b}')

