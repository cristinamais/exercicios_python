"""
28 - Leia 10 numeros inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2.
Copie os valores impares de v para v1, e os valores pares de v para v2. Note que cada um
dos vetores v1 e v2 tem no maximo 10 elementos, mas nem todos os elementos sao tulizados.
No final escreva os elementos UTILIZADOS de v1 e v2.
"""

v = []  #  Leia 10 numeros inteiros e armazene em um vetor v

for n in range(10):
    v.append(int(input(f'Digite o n {n}/10: ')))


# Crie dois novos vetores v1 e v2

v1 = []
v2 = []

for x in v:
    if x % 2 != 0:
        v1.append(x)
    else:
        v2.append(x)

print(f'elementos UTILIZADOS de v1: {v1}\nelementos UTILIZADOS de v2: {v2}')
