"""
18 - Escreva um algorítmo que leia certa quantidade de números e imprima o maior deles e em quantas vezes o maior número foi lido.
A quantidade de números a serem lidos deve ser fornecida pelo usuário.

"""
maior = 0
total_maior = 0
quantidadeLoop = int(input('Digite a quantidade de números a serem lidos: '))
listaNumeros = []

for i in range(quantidadeLoop):
    numero = int(input('Digite um número: '))
    listaNumeros.append(numero)

print('\n\n')

maior = max(listaNumeros)

total = listaNumeros.count(max(listaNumeros))

print(f'Dos números digitados o maior deles é {maior} e você o digitou {total} veze(s).\n')
