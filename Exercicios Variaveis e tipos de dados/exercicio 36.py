"""
36 - Leia a altura e o raio de um cilindro circular e imprima o volume do
cilindro. O volume de um cilindro circular é calculado por meio da seguinte
fórmula: V = pi * raio² * altura, onde pi = 3.141592.
"""

altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

vo = ((3.141592 * (raio)**2) * (altura))

print(f"O cilindro de altura {altura} e raio {raio} tem {vo:.2f} de volume.")
