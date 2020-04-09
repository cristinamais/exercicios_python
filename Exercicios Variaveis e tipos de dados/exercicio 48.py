"""
48 - Leia um valor inteiro em segundos, e imprima-o
em horas, minutos e segundos.
"""

segundos = float(input("Digite um valor de segundos: "))

horas = segundos / 1200
minutos = segundos / 60
segundos = segundos / 1

print(f"{segundos} segundos tem: {horas:.2f} horas")
print(f"{segundos} segundos tem: {minutos:.2f} minutos")
print(f"{segundos} segundos tem: {segundos:.2f} segundos")
