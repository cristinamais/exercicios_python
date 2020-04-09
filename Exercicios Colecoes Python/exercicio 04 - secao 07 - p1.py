"""
04 - Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores
X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá escrever
a soma dos valores encontrados nas respectivas posições X e Y.

vet = {'a': 2, 'b:': 5, 'y': 44, 'z': 12, 'x': 78, 'c': 15, 'p': 33, 's': 66}
print(vet)
print('A soma dos vetores X e Y são: ', vet['x'] + vet['y'])
"""

vet = {}
vet['a'] = int(input('Digite um número para a posição A: '))
vet['b'] = int(input('Digite um número para a posição B: '))
vet['c'] = int(input('Digite um número para a posição C: '))
vet['x'] = int(input('Digite um número para a posição X: '))
vet['z'] = int(input('Digite um número para a posição B: '))
vet['d'] = int(input('Digite um número para a posição D: '))
vet['y'] = int(input('Digite um número para a posição Y: '))
vet['i'] = int(input('Digite um número para a posição I: '))
print(f'Os números digitados foram: {vet}')
print('A soma dos vetores: X =', vet['x'], '+', ' Y =', vet['y'], 'igual', vet['x'] + vet['y'])

# Abaixo resposta do professor, mas que está dando erro.
"""
# Declarando o vetor
vetor = []

# Recebendo os 8 valores e adicionando no vetor
for n in range(8):
    vetor.append(int(input(f'Informe o valor {n+1}/8: ')))

# Recebendo o x (uma posição do vetor)
x = int(input('Informe a posição X do vetor entre 0 a 8 para efetuar a soma: '))

# Recebendo o y (outra posição do vetor)
y = int(input('Informe a posição Y do vetor entre 0 a 8 para efetuar a soma: '))

# Imprimindo a soma dos valores das duas posições do vetor informadas
print(f'A soma de vetor[{x}] com vetor[{y}] é {vetor[x] + vetor[y]}')
"""
