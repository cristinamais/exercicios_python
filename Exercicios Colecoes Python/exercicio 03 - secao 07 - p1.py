"""
03 - Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado dos componentes deste vetor,
armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.
"""

vet = []
resultVet = []

for i in range(10):
    i = float(input('Digite o número: '))  # Ler um conjunto de números reais
    vet.append(i)
    resultVet.append(i * 2)
print(vet)
print(resultVet)
