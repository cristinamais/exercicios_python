"""
42 - Receba o salário-base de um funcionário. Calcule e imprima o salário a
receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre salá
rio-base. Além disso ele paga 7% de imposto sobre o salário-base.
"""

salario_base = float(input("Qual o seu salário-base? "))
gratificação = salario_base * 5 / 100
imposto = salario_base * 7 / 100
salario_receber = salario_base + gratificação - imposto

print(f"O seu salário é de: {salario_receber}")
