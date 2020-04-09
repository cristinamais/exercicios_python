"""
18 - Faça um prpgrama que leia um vetor de 10 números. Leia um número x.
Conte os multiplos de um número inteiro x num vetor e mostre-os na tela.
"""
vet = []
cont = 0
for v in range(10):
    vet.append(int(input(f'Digite o vetor{[v]}: ')))
x = int(input('Digite um número para x: '))

print(vet)
print(f'multiplos do número {x} no vetor:')
for item in vet:
    if item % x == 0:
        print(item)
        cont += 1
print(f'Há {cont} números múltiplos.')

