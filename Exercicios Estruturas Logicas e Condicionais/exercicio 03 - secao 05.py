"""
3 - Leia um número real. Se o número for positivo imprima a raiz quadrada.
Do contrário, imprima o número ao quadrado.
"""
numero = float(input("Digite um número: "))

if numero > 0:
    numero = numero ** (1/2)
    print(f'A raiz quadrada desse número é {numero:.2f}.')
else:
    numero = numero ** 2
    print(f'Este número ao quadrado é: {numero}')

