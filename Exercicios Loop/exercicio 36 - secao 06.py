"""
36 - Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o
quadrado da soma. Ex:
    A soma do quadrado dos dez primeiros números naturais é: 1² + 2² + ... + 10² = 385
    O quadrado da soma dos dez primeiros números naturais é, (1 + 2 + ... + 10)² = 552 = 3025
    A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é 3025 - 385 = 2640.
"""
soma = 0
somaNumeros = 0
sQuadrado = 0
diferenca = 0
for i in list(range(1, 11)):
    q = i ** 2
    soma = soma + q
    somaNumeros += i  # soma dos valores da lista (1 + 2 + 3 + 4 ...)
    sQuadrado = somaNumeros * somaNumeros
    diferenca = sQuadrado - soma

print(f'A soma do quadrado dos primeiros números naturais é: 1² + 2² + ... + 100² = {soma}')
print(somaNumeros)
print(f'O quadrado da soma dos primeiros números naturais é: (1 + 2 + ... + 100)² = {sQuadrado}')
print(f'A diferença entre a soma dos quadrados dos primeiros números naturais e o quadrado da soma é: {sQuadrado} - {soma} = {diferenca}')
