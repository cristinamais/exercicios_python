"""
11 - Faça um programa que leia um número inteiro positivo N e imprima todos os
números naturais de 0 até N em ordem crescente.

"""
"""
n = int(input('Digite um número inteiro: '))
print(f'Este é são os números em ordem crescentes.')
cont_crescente = 0
while cont_crescente < n:
    print(cont_crescente, end=' ')
    cont_crescente += 1 

Olá Cristina,

Para resolver este problema não bastaria fazer isso:
"""
numero = int(input('Informe um número: '))
 
for n in range(1, numero+1):  # for n in range(0, numero+1) coloca o 0 no lugar do 1, para começar a partir do 0
    print(f'{n}')
