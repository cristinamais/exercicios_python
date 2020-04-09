"""
17 - Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais.
"""

n = int(input('Digite um número: '))
soma = 0
for num in range(n + 1):
    soma = soma + num
    #print(num)
print(f'A soma dos primeiros naturais são: {soma}')
