"""
6 - Escreva um programa que, dado dois números inteiros, mostre na tela o maior
deles, assim como a diferença existente entre ambos.
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    diferenca = numero1 - numero2
    print(f'O número maior é {numero1} e a diferença entre eles é: {diferenca}')
elif numero2 > numero1:
    diferenca = numero2 - numero1
    print(f'O número maior é {numero2} e a diferença entre eles é: {diferenca}') 

else:
    numero1 == numero2
    print(f'Os números {numero1} e {numero2} são iguais, portanto não existe diferença.')
