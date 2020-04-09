"""
5 - Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""
vetor = []
cont = 0
for i in range(10 + 1):
    vetor.append(int(input(f'Digite o {i}º número: ')))
print(f'Valores Digitados: {vetor}')

for n in vetor:
    if n % 2 == 0:
        cont += 1
print(f'Neste vetor foram digitatos {cont} valores pares.')
# Eu não usei o len no lugar do contador porque dá erro. Pelo que li Você não pode subtrair uma lista de um int.