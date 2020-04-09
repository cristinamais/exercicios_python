"""
20 - Ler uma sequencia de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de dados lidos 
e números de valores pares. O processo termina quando for digitado o número 1000.
"""
answer = 0
numerosLidos = []
numerosLidosPares = []


while answer != 1000:
    num = int(input(f'Enter the number: '))
    numerosLidos.append(num)

    if num % 2 == 0:
        print('par')
        numerosLidosPares.append(num)
    else:
        print('impar')
    answer = int(input('Type 1000 to stop the sequence or type 0 to continue: '))

print(numerosLidos)
print(numerosLidosPares)

#print(f'There are: {cont_even} Even numbers.', end=' ') # Números pares.
#print(f'\nThere are: {cont_odd} Odd numbers', end=' ') # Números ímpares
