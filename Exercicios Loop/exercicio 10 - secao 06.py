"""
10 - Faça um programa que calcule e mostre a soma dos 50 primeiros pares.
"""
print('Este são os 50 primeiros números pares: \n')
soma = 0
for n in range(101):
    if n % 2 == 0:
        print(n, end=', ')
        soma = soma + n
print(f'\nA soma dos números pares são: {soma}')
  
