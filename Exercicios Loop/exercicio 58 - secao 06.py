"""
58 - Faça um programa que some os números primos existente entre a e b, onde a e b são números informados pelo usuário.
"""
i, j, k = 0, 0, 0  # Declarando as variáveis
soma = 0
a = int(input('Digite um número para a: '))
b = int(input('Digite um número para b maior que a: '))

for i in range(a, b + 1):
    if i == 1:
        continue
    k = 1

    for j in range(2, i // 2 + 1):
        if i % j == 0:
            k = 0
            break
    if k == 1:
        soma = soma + i
print(f'A soma dos números primos entre {a} e {b} é: {soma}')
