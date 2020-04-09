"""
33 - Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescentes
os n primeiros naturais que são multiplos de i ou de j e ou de ambos. Exemplo:
Para n = 6, i= 2 e j = 3 a saída deverá ser: 0,2,3,4,6,8
"""
n = int(input('Digite um número para n: '))
i = int(input('Digite um número para i: '))
j = int(input('Digite um número para j: '))

natNumeros, x = [], 0

while len(natNumeros) < n:
    if (x % i == 0) or (x % j == 0):
        natNumeros.append(x)
    x += 1
print(natNumeros)
