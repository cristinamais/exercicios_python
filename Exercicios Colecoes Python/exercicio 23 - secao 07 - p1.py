"""
23 - Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles. Os conjuntos
têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar é dado por:
x1*y1 + x2*y2 + ...+xn*yn
"""
conj1 = []
conj2 = []

for a in range(5):
    conj1.append(int(input(f'Digite o {a}º número: ')))
for b in range(5):
    conj2.append(int(input(f'Digite o {b}º número: ')))

#print('Multiplicação dos números:')
#print([conj1[i]*conj2[i] for i in range(min(len(conj1), len(conj2)))])
print('Conjunto 1:', conj1)
print('Conjunto 2:', conj2)
print('Produto Escalar dos Números:')
print(sum([conj1[i]*conj2[i] for i in range(len(conj2))]))
