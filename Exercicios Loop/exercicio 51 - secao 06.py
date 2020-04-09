"""
51 - Um funcionário recebe aumento anual. Em 1995 foi contratado por 2.000 reais. Em 1996 recebeu um aumento de 1.5%. A partir de 1997,
os aumentos sempre correspondem ao dobro do ano anterior. Faça um programa que determine o salário atual do funcionário.
"""
anoInicial = 2005
anoFinal = 2015
salarioInicial = 2000
aumento = (2000 * 1.5) / 100
valorRecebe = 0
novoSalario = 2000 + aumento

while anoInicial < anoFinal:
    aumento = aumento * 2
    valorRecebe = novoSalario + (2 * aumento) + valorRecebe
    anoInicial += 1
print(valorRecebe)
