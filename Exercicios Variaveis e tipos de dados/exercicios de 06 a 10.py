"""
Leia uma temperatura em graus Celsius e apresente-a convertida em
graus Fahrenheit. A fórmula de conversão é de: F = C*(9.0/5.0) + 32.0, sendo
F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

temperatura_celsius = float(input("Digite uma temperatura em graus Celsius: "))
fahrenheit = temperatura_celsius*(9.0/5.0) + 32.0
print(fahrenheit)

"""
7 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus
Celsius. A fórmula de conversão é: C = 5.0*(F - 32.0)/9.0, sendo C a temperatura
em Celsius e F a temperatura em Fahrenheit.
"""

temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5.0*(temperatura_fahrenheit - 32.0)/9.0

print(celsius)


"""
8 - Leia uma temperatura em graus Kelvin e apresente-a convertida em graus
Celsius. A fórmula de conversão é: C = K - 273.15, sendo C a temperatura em
Celsius e K a temperatura em Kelvin.
"""
temperatura_kelvin = float(input("Digite a temperatura em graus Kelvin: "))
celsius = temperatura_kelvin - 273.15

print(f"Este é o grau Kelvin {temperatura_kelvin} em graus ºC é: {celsius:.2f}")

"""
9 - Leia uma temperatura em graus Celsius e apresente_a convertida em graus
Kelvin. A fórmula de conversão é: K = C + 273.15, sendo C a temperatura em
celsius e K a temperatura em Kelvin.
"""

temp_celsius = float(input("Digite a temperatura em graus Celsius: "))
kelvin = temp_celsius + 273.15

print(f"Esta é a tempretura de graus Celsius {temp_celsius} em Kelvin: {kelvin}")

"""
10 - Leia uma velocidade em Km/h (quilômetro por hora) e apresente-a convertida
em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a
velocidade em Km/h e M m/s.
"""

velocidade_km = float(input("Digite uma velocidade em Km/h: "))
metros_segundo = velocidade_km /3.6

print(f"O quilômetro: {velocidade_km:.2f} em metros por segundo é: {metros_segundo:.2f}")

