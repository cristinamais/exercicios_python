"""
27 - Leia um valor de área em hectares e apresente-o convertido em
metros quadrados m². A formula de conversão é: M = H * 10.000, sendo M metros
quadrados e H a área do hectar.
"""

hectares = float(input("Digite o valor em hectares: "))
                         
metros_quadrados = hectares * 10000

print(f"{hectares} hectares em metros quadraos são: {metros_quadrados}.")
