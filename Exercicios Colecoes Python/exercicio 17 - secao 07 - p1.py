"""
17 - Leia um vetor de 10 posições e atribuia valor 0 para todos os elementos que possuírem valores negativos.
"""
valores = []
for i in range(10):
    valores.append(int(input(f'Digite o {i}/10 número: ')))
print(f'Valores digitados: {valores}')
print('Estes são os valores já substituídos:')
for key, valor in enumerate(valores):
    if valor < 0:
        valor = 0
    print('chave', key, 'valor', valor)
