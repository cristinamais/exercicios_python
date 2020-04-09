"""
19 - Faça um programa para verificar se um determinado número inteiro e
divisível por 3 ou 5, mas não simultaneamente pelos dois.
"""

num = int(input("Digite um número: "))

if num % 3 == 0:
    print(f'{num} é divisível por 3')
elif num % 5 == 0:
    print(f'{num} é divisível por 5.')
else:
    print(f'{num} não é divisível por 3 e 5.')
    