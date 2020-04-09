"""
4 - Faça um programa que leia um número e, caso ele seja positivo, calcule
e mostre:
O número digitado ao quadrado
A raiz quadrada do número digitado.
"""

numero = float(input("Digite um número: "))

if numero > 0:
    numero1 = numero ** 2
    print(f"Este número ao quadrado é {numero1}")
    numero2 = numero ** (1/2)
    print(f"E a raiz quadrada dele é {numero2:.2f}")
else:
    print(f"Este é um número negativo ({numero})")
