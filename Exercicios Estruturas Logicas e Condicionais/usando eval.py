"""
How do you write a Python program that prompts for 3 numbers then divides
the first number by the second number and adds the result to the third number?
"""

print("Digite o primeiro número: ")
primeiro = eval(input())
print("Digite o segundo número: ")
segundo = eval(input())
print("Digite o terceiro número: ")
terceiro = eval(input())

terceiro += primeiro / segundo

print(f'O resultado é: {terceiro:.2f}')

"""
eval é um método python que avalia o tipo de dados da sequência de entrada,
para que você possa dividir e adicionar os valores como números.
"""
