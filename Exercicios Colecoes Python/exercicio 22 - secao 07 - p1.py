"""
22 - Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo, nas posições pares os valores
do primeiro e nas posições impares os valores do segundo.
"""
vetor1 = []
vetor2 = []
vetor3 = []

for a in range(10):
    vetor1.append(int(input(f'Digite {a}º número para o primeiro vetor: ')))
for b in range(10):
    vetor2.append(int(input(f'Digite {b}º número para o segundo vetor: ')))
print('Valores do primeiro vetor:')
for itens in vetor1:
    if itens % 2 == 0:
        vetor3.append(itens)
print('Valores do segundo vetor:')
for item in vetor2:
    if item % 2 != 0:
        vetor3.append(item)

print('Pares 1º vetor; Ímpares 2º vetor:', vetor3)
