"""
21 - Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula
de conversão é: K = L*0.45, sendo K a massa em quilograma e L a massa em libras.
"""

libras = float(input("Qual o valor da libra? "))
quilogramas = libras*0.45

print(f"{libras} libras em quilogramas é: {quilogramas:.2f}.")
