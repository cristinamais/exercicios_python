"""
05 - Faça um programa que peça ao usuário 10 valores e some-os
"""
soma = 0

for num in range(1, 11):
    numero = int(input(f'Digite o {num}º de 10 valor: '))
    soma = soma + numero
print(f'A soma de todos os valores é: {soma}')
