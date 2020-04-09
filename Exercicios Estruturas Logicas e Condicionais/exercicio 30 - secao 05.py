"""
30 - Faça um programa que receba três números e mostre-os em ordem crescentes.

"""
numA = int(input("Digite o primeiro número: "))
numB = int(input("Digite o segundo número: "))
numC = int(input("Digite o terceiro número: "))

# Menor valor:
menor = numA

if (numB < numA) and (numB < numC):
    menor = numB
if (numC < numA) and (numC < numB):
    menor = numC
print(f'Menor valor é {menor}')

# Maior valor:
maior = numA

if (numB > numA) and (numB > numC):
    maior = numB
if (numC > numA) and (numC > numB):
    maior = numC

print(f'Maior valor é {maior}')
