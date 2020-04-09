"""
10 - Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mos
tre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à
altura):

Homens: (72.7 * h) - 58
Mulheres: (62.1 * h) - 44.7
"""

sexo = input("Qual o seu sexo? ")
altura = float(input("Digite a sua altura: "))

masculino = (72.7 * altura) - 58
feminino = (62.1 * altura) - 44.7

if sexo.title().upper() == masculino:
    print(f'O seu peso ideal é de: {masculino:.2f}')
else:
    sexo.title().upper() == feminino
    print(f'O seu peso ideal é de: {feminino:.2f}')

#print(dir(sexo))  
    
    
