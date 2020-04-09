"""
20 - Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um vetor com 10 posições.
Preencha um segundo vetor apenas com os números ímpares do primeiro vetor. Imprima os dois vetores, 2 elementos por linha.
"""
vetor = []
vet = []
segundoVetor = []


for v in range(10):
    vetor.append(int(input('Digite um número em um intervalo de 0 a 50: ')))
    for i in vetor:
        if i <= 50:
            print(i)
print('Números ímpares do primeiro vetor:')
for vetores in vetor:
    if vetores % 2 == 1:
        segundoVetor.append(vetores)
        print(segundoVetor, sep='')



# Obs: Não consegui imprimir 2 elementos por linha.

"""
Olá Cristina,

Para imprimir 2 valores por linha basta colocá-los no mesmo print.

Exemplo:

valor1 = 4
valor2 = 8
 
print(f'{valor1} {valor2}')
Abraço!
"""