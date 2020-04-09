"""
25 - Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que não são múltiplos de 7 ou
que terminam com 7.
"""
vetor = []
for v in range(100):
    vetor.append(v)
print('Números de 0 a 100 que não são múltiplos de:')
for v in vetor:
    if v % 7 != 0:
        print(v)
print('Números de 0 a 100 que não terminam com 7:')
for c in vetor:
    if '7' not in str(c):  # Se quisesse que aparecesse só os nºs com o 7 seria: if '7' in str(c)
        print(c)  # Tem essa opção aqui também: c % 10 != 7

