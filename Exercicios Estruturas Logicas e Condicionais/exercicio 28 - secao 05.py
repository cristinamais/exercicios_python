"""
28 - Faça um programa que leia três números inteiros positivos e efetue
o cálculo de uma das seguintes médias de acordo com um valor numérico digitado
pelo usuário:

Geométrica
Ponderada
Harmônica
Aritmética
"""

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))

opcao = 0

print('''\n( 1 ) Geométrica \n( 2 )Ponderada \n( 3 ) Harmônica \n( 4 )Aritmética''')
opcao = int(input('Escolha um dos valores numéricos acima para fazermos o cálculo: '))

if opcao == 1:
    geometrica = ((x * y * z) ** (1/3))
    print(f'\nTendo os valores de x = {x}, y = {y} e z = {z}. O cáculo da média geométrica é {geometrica:.2f}')
elif opcao == 2:
    ponderada = (x + (2 * y) + (3 * z)) / 6
    print(f'\nTendo os valores de x = {x}, y = {y} e z = {z}. O cáculo da média ponderada é {ponderada:.2f}')
elif opcao == 3:
    harmonica = (1 / (1 / x) + (1 / y) + (1 / z))
    print(f'\nTendo os valores de x = {x}, y = {y} e z = {z}. O cáculo da média harmônica é {harmonica:.2f}')
elif opcao == 4:
    aritmetica = (x + y + z) / 3
    print(f'Tendo os valores de x = {x}, y = {y} e z = {z}. O cáculo da média aritmética é {aritmetica:.2f}')

print('\n>>>>>>>>>>>> FIM DO PROGRAMA <<<<<<<<<<<<<<<<<<')

