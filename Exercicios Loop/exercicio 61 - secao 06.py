"""
61 - Faça um programa que calcule o maior número palíndromo a partir do produto de dois números de 3 dígitos.
Exemplo o maior palíndromo feito a partir do produto de dois dígitos é 9009 = 91 * 99
"""
maiorNumero = int(input('Digite o primeiro número com dois dígitos: '))
menorNumero = int(input('Digite o segundo número, sendo menor que o primeiro, mas com dois digitos: '))
menorLimite = 0

for x in range(1, menorNumero, maiorNumero + 1):
    menorLimite = menorLimite * 10
    menorLimite = menorLimite + 9

maiorLimite = 1 + menorLimite // 10
maxProduto, numero = 0, 0

for i in range(menorLimite, maiorLimite - 1, -1):
    for j in range(i, maiorLimite - 1, -1):
        produto = i * j
        if produto < maxProduto:
            break
        numero = produto
        reverse = 0
        while numero != 0:
            reverse = reverse * 10 + numero % 10
            numero = numero // 10
        if produto == reverse and produto > maxProduto:
            maxProduto = produto
print(f'O maior número palíndromo a partir do produto dos números {maiorNumero} * {menorNumero} = {maxProduto}')

