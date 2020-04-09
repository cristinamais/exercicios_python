"""
46 - Faça um programa que leia um número inteiro positivo de três dígitos
(de 100 a 999). Gere outro numero formado pelos dígitos invertidos do
número lido. Exemplo:
NumeroLido = 123
NumeroGerado = 321
"""

numero = int(input("Digite um número de 100 a 999: "))

invertido = str(numero)[::-1]

print(f"Esse é o número que você digitou: {numero} e este é o número invertido: {invertido}")