"""
53 -Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado
Triângulo de Floyd. Para n = 6, temos:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
c = 1  # começando com 1 no canto superior esquerdo, ou qualquer caractere.
n = int(input('Digite um número: '))
for i in range(n + 1):  # Loop de linha --> percorre o intervalo do triângulo para loop de linha
    for j in range(1, i + 1):  # Loop de coluna --> passa pelo valor do 1º loop + 1.
        print(c, end=' ')  # imprima o valor do índice para imprimir triângulo
        c += 1
    print()


