"""
26 - Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A formula de conversão é: H = M* 0.0001, sendo M a área em metros quadrados e
H a área em hectares.
"""

metros_quadrados = float(input("Qual a quantidade do metro quadrado? "))
hectar = metros_quadrados * 0.0001

print(f"{metros_quadrados} metros quadrados em hectares são: {hectar:.4f}.")
