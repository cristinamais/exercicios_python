"""
09 - Faça um programa que leia um número inteiro N e depois imprima os N
primeiros números naturais ímpares.
"""
# o número que eu coloca em n ele vai ler daqui pra baixo. 


n = int(input('Digite um número inteiro: '))

cont_impar = 0 # vai contar os ímpares

while cont_impar < n:
    print(2 * cont_impar + 1 )
    cont_impar += 1
