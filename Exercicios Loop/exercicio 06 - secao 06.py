"""
06 - Faça um programa que leia 10 inteiros e imprima sua média.
        PARA ENCONTRAR A MÉDIA:
Determine o conjunto de valores que você deseja medir. Esses números podem ser altos, ou baixos, e pode haver quantos você quiser. ...
Some os valores para encontrar a soma. ...
Conte a quantidade de valores no grupo. ...
Divida a soma dos números pela quantidade de números do conjunto.
"""
soma = 0
media = 0

for n in range(1, 11):
    numero = int(input(f'Digite dez números {n} / 10: '))
    soma = soma + numero
media = soma / n
print(soma)
print(media)
