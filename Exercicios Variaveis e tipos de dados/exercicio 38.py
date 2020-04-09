"""
38 - Leia um salário de um funcionário. Calcule e imprima o valor do novo salário
sabendo que ele recebeu um aumento de 25%.
"""

salario = float(input("Qual o seu salário? $: "))

aumento = salario + (salario * 25 /100)

print(f"Com o aumento de 25% o seu salário passou a ser: {aumento:.2f}")
