"""
11 - Escreva um programa que leia um número inteiro maior que zero e devolva
na tela, a soma de todos seus algarismos. Por exemplo, ao número 251 correspon
derá o valor 8(2 + 5 + 1). Se o número lido não for maior que zero, o programa
terminará com a mensagem 'Número inválido'.
"""

num = int(input("Digite um número inteiro: "))

if num > 0:
    digito = (num // 1000 % 10) + (num // 100 % 10) + (num // 10 % 10) + (num // 1 % 10)
    digito1 = (num // 1000 % 10)
    digito2 = (num // 100 % 10)
    digito3 = (num // 10 % 10)
    digito4 = (num // 1 % 10)
    print(f'O número {num} corresponde ao valor {digito}({digito1} + {digito2} + {digito3} + {digito4}).')
   
else:
    print('Número inválido')

