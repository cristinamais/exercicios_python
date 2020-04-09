"""
08 - Crie um programa que lê 06 valores e, em seguida, mostre na tela os valores lidos na ordem inversa
"""
valoresLidos = []

for x in range(6):
    valor = int(input('Digite o número: '))
    valoresLidos.append(valor)
print('Estes são os valores lidos:')
for valores in valoresLidos:
    print(valores)
print('Valores lidos em reverso:')
for valor in sorted(valoresLidos, reverse=True):
    print(valor)

