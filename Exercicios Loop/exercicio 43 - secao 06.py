"""
43 - Faça um programa que leia um determinado número de idades de indivíduos (pare quando for formado a idade 0),
e calcule a idade média desse grupo.
"""
cont = 0
soma = 0
idade = int(input('Digite a idade: '))
while idade > 0:
    soma += idade
    cont += 1
    idade = int(input('Digite a idade: '))

media = soma / cont
print(f'A média das idades é de {media}')
