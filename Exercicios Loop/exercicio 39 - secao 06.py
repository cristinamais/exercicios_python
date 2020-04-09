"""
39 - Faça um programa que calcule a área de um triângulo retângulo, cuja base e altura são fornecidas
pelo usuário. Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas
menores ou iguais a 0.
"""

b, a = [int(x) for x in input('Digite um valor para a base e um para a altura: ').split()]
if b and a > 0:
    print('A área do triângulo retângulo é:', (b * a) // 2, 'cm')
else:
    print('Entrada de dados inválidos, umas das medidas ou todas são menores ou iguais a 0.')


