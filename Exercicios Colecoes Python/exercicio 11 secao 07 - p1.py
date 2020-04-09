"""
11 - faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a
soma dos números positivos desse vetor.
"""

numeros = []
pos, neg = 0, 0
for n in range(5):  # Estou usando 5 números só pra fazer o teste
    num = int(input('Digite o número: '))
    numeros.append(num)
for num in numeros:
    if num >= 0:
        pos += num
    else:
        neg += 1
print("Números negativos na lista: ", neg)
print("Soma dos positivos da lista: ", pos)
print(type(num))
