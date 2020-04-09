"""
24 - Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número,
com excessão dele próprio. Ex: a soma dos divisores do número 66 é 1+2+6+11+22+33 = 78
"""

numero = -1
print('Digite zero para sair.')
while numero != 0:
    numero = int(input('Digite um numero: '))

    if numero > 0:
        lista = [i for i in range(1, numero // 2 + 1) if numero % i == 0]
        print(f'Este são os número divisíveis por {numero} : {lista}')
        soma = sum(lista)
        print(f'A soma de todos os divisores do número {numero} são: {soma}')
