"""
23 - Leia um valor de comprimento em metros e apresente-o convertido em jardas.
A fórmula de conversão é: J= M/0.91, sendo J o comprimento em jardas e
M o comprimento em metros.
"""

metros = float(input("Digite o valoe em metros: "))
jardas = metros/0.91

print(f"{metros} metros em jardas são: {jardas:.2f}.")
