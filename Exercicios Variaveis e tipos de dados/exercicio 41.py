"""
41 - Faça um programa que leia o valor da hora de trabalho em reais e número
de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário,
adicionando 10% sobre o valor calculado.
"""

vh_trabalhada = float(input("Digite o valor da hora trabalhada: "))
horas_trabalhadas = float(input("Quantas horas você trabalhou? "))

valor_a_pagar = vh_trabalhada * horas_trabalhadas

salario_total = valor_a_pagar + (valor_a_pagar * 10 / 100)

print(f"Você trabalhou {horas_trabalhadas} horas tendo um valor total de salario a receber de: {salario_total}.")
