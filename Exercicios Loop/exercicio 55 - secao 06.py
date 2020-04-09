"""
55 - Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros primos
"""
n = int(input('Digite um número não negativo: '))

listaPrimo = [True] * (n + 1)
soma  = 0
p = 2
while p * p <= n:  # Senão for alterado então é primo
    if listaPrimo[p] == True:  # Atualiza os multiplos
        i = p * 2
        while i <= n:
            listaPrimo[i] = False
            i += p
    p += 1
for i in range(2, n + 1):  # Soma dos números primos
    if (listaPrimo[i]):
        soma += i
print(f'A soma dos n primeiros primos é: {soma}')



