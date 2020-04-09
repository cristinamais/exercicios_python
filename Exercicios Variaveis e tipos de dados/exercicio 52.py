"""
52 - Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser
repartido proporcionalmente ao valor que cada um deu para a realização da aposta
Faça um programa que leia quanto cada apostador investiu, o valor do prêmio
e imprima quanto cada um ganharia do prêmio com base no valor investido.
"""

valor_aposta = float(input("Digite o valor da aposta: "))

apost1 = int(input("Digite a porcentagem que você investiu: "))
apost2 = int(input("Digite a porcentagem que você investiu: "))
apost3 = int(input("Digite a porcentagem que você investiu: "))


premio1 = (valor_aposta * apost1) // 100
premio2 = (valor_aposta * apost2) // 100
premio3 = (valor_aposta * apost3) // 100

print(f"O primeiro apostador vai ganhar: {premio1}, o segundo vai ganhar: {premio2} e o terceiro ganhará: {premio3}.")
