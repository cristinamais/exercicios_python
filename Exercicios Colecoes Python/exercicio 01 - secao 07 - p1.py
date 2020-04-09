"""
01 - Faça um programa que possua um vetor denominado A que armazene 6 números inteiros.
O programa deve executar os seguintes passos:
a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7
b) Armazene em uma variável inteira (simples) a soma entre os valores das posições
A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
d)Mostre na tela cada valor do vetor A, um em cada linha .

"""
variavelInteira = []
a = [1, 0, 5, -2, -5, 7]
variavelInteira.append(a[0])
variavelInteira.append(a[1])
variavelInteira.append(a[5])

print(f'A soma entre os valores das posições A[0], A[1] e A[5] é: {sum(variavelInteira)}')

a.insert(4, 100)
print(f'O vetor 4 que antes tinha o valor -5 , foi atribuindo o valor 100. Veja: {a}')

print('Mostre na tela cada valor do vetor A, um em cada linha . ')
for indice, a in enumerate(a):
    print('Vetor:', indice, 'valor:', a)


