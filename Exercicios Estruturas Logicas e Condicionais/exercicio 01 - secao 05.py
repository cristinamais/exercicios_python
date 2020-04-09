"""
1 - Faça um programa que receba dois números e mostre qual deles é o maior.
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


if numero1 > numero2:
    print(f"Entre os números {numero1} e {numero2} .O número maior é: {numero1}")
elif numero1 == numero2:
    print(f"Entre os números {numero1} e {numero2} .O número maior é: {numero1}")
else:
    print(f"Entre os números {numero1} e {numero2} .O número maior é: {numero2}")
