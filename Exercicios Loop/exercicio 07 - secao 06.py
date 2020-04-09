"""
07 - Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
"""
soma = 0
media = 0
numero = 0
for num in range(1, 11):
        numero = int(input(f'Digite dez números {num}º: '))
        soma = soma + numero
        while numero <= 0:
            print('Número precisa ser positivo. Reinforme número: ')
            numero = int(input(f'Digite dez números {num}º: '))
media = soma / num
print(f'Esta é a soma dos valores: {soma}')
print(f'Esta é a média dos valores: {media}')
