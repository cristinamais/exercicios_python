"""
12 - Fazer um programa para ler 5 valores, e em seguida, mostrar todos os valores lidos juntamente
com o maior, o menor e a média dos valores.
"""

valores = []

for n in range(5):
    valores.append(int(input('Digite o valor: ')))
print(f'Números lidos: {valores}')
print('Maior número:', max(valores))
print('Menor número:', min(valores))
print('Média dos números:', sum(valores) / len(valores))
