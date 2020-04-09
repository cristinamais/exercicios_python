"""
59 - Escreva um programa que leia o número de habitantes de uma determinada cidade, e o valor do kwh para cada habitante, entre com os seguintes
dados: consumo do mês e o código do consumidor (1 - Residencial, 2 - Comercial, 3 - Industrial).
No final imprima o maior, o menor e a média do consumo dos habitantes; e por fim o total do consumo de cada categoria de consumidor.
"""
numeroHabiatante = int(input("Digite a quantidade de habitantes: "))
calcResidencial, calcComecial, calcIndustrial, somaTotal = 0, 0, 0, 0
somaResidencial, somaComercial, somaIndustrial = 0, 0, 0

for n in range(numeroHabiatante):
        print('Digite a qual Código do Consumidor você pertence:\n1 - Residencial\n2 - Comercial\n3 - Industrial')
        codigo = int(input())
        print('Digite a quantidade de Kwh consumida no mês:')
        quantidadeKwhMes = int(input())
        if codigo == 1:
                calcResidencial = quantidadeKwhMes * (numeroHabiatante // 3)
                print(f'Você faz parte do Consumidor Residencial e você consumiu: {calcResidencial}')
        elif codigo == 2:
                calcComecial = quantidadeKwhMes * (numeroHabiatante // 3)
                print(f'Você faz parte do Consumidor Comercial e você consumiu : {calcComecial}')
        elif codigo == 3:
                calcIndustrial = quantidadeKwhMes * (numeroHabiatante // 3)
                print(f'Você faz parte do Consumidor Industrial e você consumiu {calcIndustrial}')

somaResidencial = somaResidencial + calcResidencial
somaComercial = somaComercial + calcComecial
somaIndustrial = somaIndustrial + calcIndustrial

listaConsumidores = [somaResidencial, somaComercial, somaIndustrial]

if max(listaConsumidores) == listaConsumidores[0]:
        print(f'O maior consumidor foi Residencial com o valor de: {somaResidencial}')
elif max(listaConsumidores) == listaConsumidores[1]:
        print(f'O maior consumidor foi Comercial com o valor de: {somaComercial}')
elif max(listaConsumidores) == listaConsumidores[2]:
        print(f'O maior consumidor foi Industrial com o valor de: {somaIndustrial}')

if min(listaConsumidores) == listaConsumidores[0]:
        print(f'O menor consumidor foi Residencial com o valor de: {somaResidencial}')
elif min(listaConsumidores) == listaConsumidores[1]:
        print(f'O menor consumidor foi Comercial com o valor de: {somaComercial}')
elif min(listaConsumidores) == listaConsumidores[2]:
        print(f'O menor consumidor foi Industrial com o valor de: {somaIndustrial}')

somaTotal = somaTotal + calcResidencial + calcComecial + calcIndustrial
media = somaTotal / numeroHabiatante
print(f'A média entre os consumidores foi de: {media}')
print(f'A soma Total entre os consumidores foi de: {somaTotal}')




