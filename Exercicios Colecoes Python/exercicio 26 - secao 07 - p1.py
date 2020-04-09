"""
26 - Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 números, onde m é a média do vetor.
"""
import statistics
v = []
for n in range(1, 10 + 1):
    v.append(int(input(f'Digite o número {n}/10: ')))

print('Média do Vetor:', sum(v) / len(v))
print('Desvio Padrão:', statistics.stdev(v))

