"""
57 - Faça um programa que conte quantos números primos existirem entre a e b, onde a e b são números informados pelo usuário.
"""
i, j, k = 0, 0, 0  # Declarando as variáveis

a = int(input('Digite um número para a: '))
b = int(input('Digite um número para b maior que a: '))

cont = 0
for i in range(a, b + 1):
    if i == 1:
        continue
    k = 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            k = 0
            break
    if k == 1:
        cont += 1
        print(i, end=" ")
print(f"--> estes são os números primos entre {a} e {b}, sendo assim existem {cont} números primos entre eles.", end=" ")


