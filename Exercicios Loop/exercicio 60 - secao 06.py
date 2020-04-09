"""
60 - Faça um programa que leia vários números, calcule e mostre:
a) A soma dos números digitados
b) A quantidade de números digitados
c) A média dos números digitados
d) O maior número digitado
e) O menor número digitado
f) A média dos números pares
Finalize a entrada de dados caso o usuário informe o valor 0.
"""
print('Quando quiser sair do programa digite o número ZERO.')
soma, somal, contl = 0, 0, 0
listaNumeros = []

numero = int(input('Digite um número: '))
while numero != 0:
    soma = soma + numero
    listaNumeros.append(numero)
    numero = int(input('Digite um número: '))
for i in listaNumeros:
    if i % 2 == 0:
        # print(i, end' ')
        somal = somal + i
        contl += 1

media = sum(listaNumeros) / len(listaNumeros)  # len aqui está funcionando como se fosse o contador.
medial = somal / contl

# print(listaNumeros)
print(f'A soma dos números digitados é:', sum(listaNumeros))
print(f'A quantidade de números digitados é:', len(listaNumeros))
print(f'A média dos números digitados é: {media}')
print(max(listaNumeros), '<-- Este é o maior número digitado')
print(min(listaNumeros), '<-- Este é o menor número digitado')
print(f'A média dos números pares é {medial}')
