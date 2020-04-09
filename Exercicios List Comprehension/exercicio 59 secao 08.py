"""
59 - Faca uma funcao que recebe, por parametro, 2 vetores de 10 elementos inteiros e calcule e retorne, tambem por
parametro, o  vetor uniao dos dois primeiros.
"""
v1 = []
v2 = []
cont = 0
while cont < 10:
    v1.append(int(input('Digite os elementos do 1 vetor: ')))
    v2.append(int(input('Digite os elementos do 2 vetor: ')))
    cont += 1


def funcao_uniao(v1, v2):  # funcao recebendo os vetores
    print(set(v1), set(v2))
    uniao = set(v1).union(set(v2))
    return f'Uniao: {uniao}'


print(funcao_uniao(v1, v2))
