"""
7 - Faça um programa que receba dois números e mostre o maior. Se por acaso, os
dois números forem iguais, imprima a mensagem Números Iguais.
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
     print(f'Entre os números {numero1} e {numero2} o número {numero1} é maior.')
elif numero1 < numero2:
    print(f'Entre os números {numero1} e {numero2} o número {numero2} é maior.')
else:
    print('Números iguais')
    
"""
#else:
    numero1 == numero2
    print(f'Os números {numero1} e {numero2} são iguais.')
numero1 == numero2

Dado que você verifica na linha 9 se 'numero1' é maior que 'numero2' e verifica na linha 11 se 'numero1' é menor que 'numero2',
se não for nem uma coisa nem outra então os números só podem ser iguais.
"""