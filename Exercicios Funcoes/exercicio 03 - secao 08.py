"""
03 - Faca uma funcao para verificar se um numero e positivo ou negativo. Sendo que o valor
de retorno sera 1 se positivo, -1 se negativo e 0 se for igual a 0.
"""

numero = int(input('Digite um numero: '))

def numeros(n):  # Se eu nao passar nada aqui
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    return 0


print(numeros(numero))  # Aqui eu nao vou precisar passar nada.
