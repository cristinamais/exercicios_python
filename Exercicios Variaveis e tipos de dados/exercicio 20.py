"""
20 - Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é: L= K/0.45, sendo K a massa em quilogramas e L
a massa em libras.
"""

kg = float(input("Qual o valor do Kg: "))
libras = kg/0.45

print(f"{kg} quilo(s) em libras é de {libras:.2f}.")
