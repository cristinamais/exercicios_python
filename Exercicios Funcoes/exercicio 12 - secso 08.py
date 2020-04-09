"""
12 - Escreva uma funcao que receba um numero inteiro maior que zero e retorne a soma de todos os seus algarismos.
Por exemplo, ao numero 251 correspondera o valor 8(2 + 5 + 1). Se o numero lido nao for maior do que zero, o programa
terminara com a mensagem "Numero invalido"
"""

n = int(input('Digite um numero: '))

def inteiro(n):
    if n > 0:
        m = n // 1000 % 10
        c = n // 100 % 10
        d = n // 10 % 10
        u = n // 1 % 10
        soma = m + c + d + u
        return soma
    return 'Numero invalido'

print(inteiro(n))