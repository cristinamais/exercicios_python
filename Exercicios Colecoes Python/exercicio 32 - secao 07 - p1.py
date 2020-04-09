"""
32 - Leia dois vetores inteiros x e y, cada um com 5 elementos (assuma que o usuario nao informa elementos repetidos).
Calcule e mostre os vetores resultantes em cada caso abaixo:

-Soma entre x e y: soma de cada elemento de x com o elemento da mesma posicao em y;
-Produto entre x e y: multiplicacao de cada elemento de x com o elemento da mesma posicao em y;
-Diferenca entre x e y: todos os elementos de x que nao existam em y;
-Intersecao entre x e y: apena os elementos que aparecem nos dois vetores.
-Uniao entre x e y: todos os elementos de x, e todos os elementos de y que nao estao em x.
"""

x = []
y = []
z = []
lista_dif = []
for k in range(1, 6):
    x.append(int(input(f'Digite o numero {k}/5: ')))

for j in range(1, 6):
    y.append(int(input(f'Digite o numero {j}/5: ')))

# assuma que o usuario nao informa elementos repetidos:

print(f'Vetor x: {list(enumerate(x))}\nVetor y: {list(enumerate(y))}')


for elemX, elemY in zip(x, y):
    z.append(elemX + elemY)  # adicionar em z a soma dos elementos de cada lista
print('Soma x e y:', z)


print('Produto x e y:')
for a, b in zip(x, y):
    print(a * b, end=' ')

print('\nDiferenca x e y:\n', list(set(x) - set(y)))
print('\nIntersecao x e y:\n', list(set(x).intersection(set(y))))
print('\nUniao x e y:\n', set(x) | set(y))

