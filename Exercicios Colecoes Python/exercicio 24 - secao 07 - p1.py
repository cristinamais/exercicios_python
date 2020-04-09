"""
24 - Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representado a sua altura em metros. Encontre o aluno mais baixo e o mais alto. Mostre o número do aluno mais baixo
e do aluno mais alto, juntamente com suas alturas.
"""
data = {}

for i in range(10):
    numero = int(input('Digite o número do aluno: '))
    altura = float(input('Digite a altura: '))
    data[numero] = altura

# print(sorted(data.items())) -> Colocando os dados em ordem de maior para menor.

maximum = max(data, key=data.get)
print(f'O aluno mais alto está no número: {maximum} e a sua altura é {data[maximum]}')
minimum = min(data, key=data.get)
print(f'O aluno mais baixo está no número: {minimum} e a sua altura é: {data[minimum]}')

