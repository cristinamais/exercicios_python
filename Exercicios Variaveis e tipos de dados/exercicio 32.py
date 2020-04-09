"""
32 Leia um número inteiro e imprima a soma do sucessor de seu triplo com o
antecessor de seu dobro.
"""

numero = int(input("Digite um número: "))

soma = ((numero ** 3) + 1) + ((numero ** 2) - 1)

print(soma)
