"""
37 - Escreva um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade seguinte:
a soma dos dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem elevada ao quadrado é igual ao próprio número.
Por exemplo: para o inteiro 3025, temos que:
30 + 25 = 55
55² = 3025
"""
# potencia = soma ** 2
# print(soma)
# print(potencia)
soma = 0

for i in range(1000, 10000):
    soma = ((i // 100) + (i % 100))  # divisão e o resto da divisão (operadores DIV e MOD)
    if ((soma * soma) == i):
        print(f'Os número entre 1000 e 9999 (inclusive) que possue a mesma propriedade são: {i}')
