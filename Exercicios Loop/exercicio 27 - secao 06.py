"""
27 - Em matemática, o número harmônico designado por H(n) defini-se como sendo a soma da série harmônica:
    H(n) = 1 + 1 / 2 + 1 / 3 + 1/ 4 + ...+1 / n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
O loop for é usado para encontrar a soma da série e o número é incrementado para cada iteração.
Os números são adicionados à variável sum e isso continua até que o valor de i atinja o número de termos.

soma = 0
constante = 1

numero = int(input('Digite um número: '))

for i in range(1, numero + 1):
    soma += constante / i

print(f'O valor de H({numero}) é {soma:.2f}')
"""

numero = int(input("Digite um número: "))
soma = 0

for i in range(1, numero + 1):
    soma = soma + (1/i)
print(f"O valor de H(n) desse número {numero} é: {soma:.2f} ")