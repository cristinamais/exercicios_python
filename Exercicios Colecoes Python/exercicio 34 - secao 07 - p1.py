"""
34 - Faca um programa para ler 10 numeros DIFERENTES  a serem armazenados em um vetor. Os dados deverao ser armazenados
no vetor na ordem que forem sendo lidos, sendo que caso o usuario digite um numero que ja foi digitado anteriormente, o
programa devera pedir para ele digitar outro numero. Note que cada valor digitado pelo usuario deve ser pesquisado no
vetor, verificando se ele existe entre os numeros que ja foram fornecedos. Exibir na tela o vetor final que foi digitado.

"""

n = []
cont = 0  # contador

while cont < 10:
    v = int(input(f'Informe o numero {cont + 1}/10: '))
    if v not in n:
        n.append(v)
        cont = cont + 1
    else:
        print(f'O numero {v} ja foi informado antes, por favor, insere outro numero.')

print(f'Os numeros informados foram: {n}')
