"""
27 - Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são primos e suas respectivas
posições no vetor.
"""
vetor = []

for n in range(10):
    vetor.append(int(input(f'Digite o numero: ')))

print('Leia 10 números inteiros e armazene em um vetor:\n', list(enumerate(vetor)))
print('\nElementos primos e suas respectivas posições:')

for i, numeros in enumerate(vetor):
    if numeros != 1 and numeros % 2 != 0 and numeros % 3 != 0:
        print(f'[{i}] = {numeros}')

# OBS: Professor por favor, como eu poderia eliminar o numero 1 aque nesse caso, porque ele nao e um numero primo.





