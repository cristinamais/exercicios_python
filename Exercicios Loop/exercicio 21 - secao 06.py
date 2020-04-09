"""
21 - Faça um programa que receba dois números. Calcule e mostre:
a) A soma dos números pares desse intervalo de números, incluindo os números digitados;
b) A multiplicação dos números ímpares desse intervalo, incluindo os digitados.
"""

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
somaPares = 0
multiplicacaoImpar = 1

for i in range(numero1, numero2 + 1):
    if i % 2 == 0:
        somaPares = somaPares + i
    else:
        multiplicacaoImpar = multiplicacaoImpar * i

print(somaPares)
print(multiplicacaoImpar)
