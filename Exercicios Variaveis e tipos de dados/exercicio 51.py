"""
51 - Escreva um programa que leia as coordenadas x e y de pontos do R²
e calcule sua distância da origem(0,0).
"""

from math import sqrt

co_xa = float(input("Digite a coordenada de x no ponto a: "))
co_xb = float(input("Digite a coordenada de x no ponto b: "))


co_yb = float(input("Digite a coordenada de y no ponto a: "))
co_yb = float(input("Digite a coordenada de y no ponto b: "))


distancia = sqrt((co_xa - co_xb)**2) + ((co_yb - co_yb)**2)


print(f"A distância entre os dois pontos é de: {distancia}")
