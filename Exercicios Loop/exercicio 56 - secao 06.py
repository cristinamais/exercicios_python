"""
56 - Faça um programa que some todos os números primos abaixo de dois milhoes.
"""

listaPrimo = [True] * (2000000 + 1)
soma  = 0
p = 2
while p * p <= 2000000:  # Senão for alterado então é primo
    if listaPrimo[p] == True:  # Atualiza os multiplos
        i = p * 2
        while i <= 2000000:
            listaPrimo[i] = False
            i += p
    p += 1
for i in range(2, 2000000 + 1):  # Soma dos números primos
    if (listaPrimo[i]):
        soma += i
print(f'A soma de todos os números primos abaixo de dois milhoes é: {soma}')