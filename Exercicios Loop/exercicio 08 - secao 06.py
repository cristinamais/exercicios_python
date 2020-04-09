"""
08 - Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""

maior = 0
menor = 0
listaNumerosLidos = []

for n in range(10):
    numeroLido = int(input(f"Digite dez valores {n}º: "))

    listaNumerosLidos.append(numeroLido)

listaNumerosLidos.sort()

maior = max(listaNumerosLidos)
menor = min(listaNumerosLidos)

print(f'\nMaior Valor: {maior}\n')
print(f'Menor Valor: {menor}')
