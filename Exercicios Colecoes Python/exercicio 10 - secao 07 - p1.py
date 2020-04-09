"""
10 - Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral.
"""
notasLidas = []

for alunos in range(15):
    notasLidas.append(float(input('Digite a notas dos 15 alunos de um por um: ')))
print(f'Estas foram as notas dos alunos: \n{notasLidas}')
print('A média geral dos alunos foi de:', sum(notasLidas) / len(notasLidas))
