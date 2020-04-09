"""
Faca um programa que receba 6 numeros inteiros e mostre:
- Os  numeros pares digitados;
-A soma dos numeros pares digitados;
-Os numeros impares digitados;
-A quantidade de numeros impares digitados;

"""

x = []
soma = 0
quant = 0

for z in range(6):
   x.append(int(input('Digite um numero: ')))

print('Numeros pares digitados:')
for i, y in enumerate(x):
    if y % 2 == 0:
        print(f'[{i}] = {y}')
        soma = soma + y

print('Numeros impares digitados:')
for a, b in enumerate(x):
    if b % 2 != 0:
        print(f'[{a}] = {b}')
        quant += 1

print(f'A soma dos numeros pares digitados: {soma}')
print(f'A quantidade de numeros impares digitados: {quant}')


