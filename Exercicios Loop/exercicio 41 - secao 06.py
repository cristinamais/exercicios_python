"""
41 - Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos pelo ususário via teclado.
O programa fica pedindo estes valores calculando até que o ususário entre com um valor para resistência igual a zero.
        R = R1 * R2 / R1 + R2
"""
print('O programa irá rodar até que encontre um valor de uma das resistências igual zero.')
r = 1
r1 = int(input('Digite um valor para R1: '))
r2 = int(input('Digite um valor para R2: '))
while r1 != 0 and r2 != 0:
    r = ((r1 * r2) / (r1 + r2))
    print(f'A associação paralela entre os dois resistores R1: {r1} e R2: {r2} é {r}')
    r1 = int(input('Digite um valor para R1: '))
    r2 = int(input('Digite um valor para R2: '))

