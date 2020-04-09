"""
40 - Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que
solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida
que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.
"""

dias_trabalhados = int(input("Digite a quantidade de dias trabalhados: "))
hora_dia = 30.00
salario = dias_trabalhados * hora_dia

liquido_receber = salario - (salario * 8 / 100)

print(f"Você trabalhou {dias_trabalhados} dias o liquido a recber é: {liquido_receber}, já descontado 8% do imposto de renda.")
