"""
11 - Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em Km/h
(quilômetros por hora). A fórmula par conversão é: K = M * 3.6, sendo K a
velocidade em Km/h e M m/s.
"""

velocidade_metros = float(input("Digite a velocidade em m/s: "))
quilometros_hora = velocidade_metros * 3.6

print(f"{velocidade_metros} metros por segundo em quilômetros por hora é: {quilometros_hora}")

"""
12 - Leia uma distância em milhas e apresente-a em convertida em quilômetros.
A fórmula de conversão é: K = 1.61 * M, sendo K a distância em quilômetros
e M em milhas.
"""

distancia_milhas = float(input("Digite a distância em milhas: "))
quilometros = 1.61 * distancia_milhas

print(f"A distância de {distancia_milhas} milhas é {quilometros} quilômetros.")

"""
13 - Leia uma distância em quilômetros e apresente-a convertida em milhas.
A fórmula de conversão é: M = K/1.61, sendo K a distância em quilômetros
e M em milhas.
"""

distancia_km = float(input("Digite a distância em Km: "))
milhas = distancia_km/1.61

print(f"{distancia_km} quilômetro em milhas é de {milhas:.2f}.")

"""
14 - Leia um ângulo em graus e apresente-o convertido em radianos.
A fórmula de conversão é: R = G * pi.14/180, sendo G o ângulo em graus
e R em radianos e pi = 3.14
"""

angulo = float(input("Digite o valor do ângulo: "))
radianos = angulo * 3.14/180

print(f"O ângulo {angulo} em graus convertido em radiano é: {radianos:.2f}")

"""
15 - Leia um ângulo em radianos e apresente-o em convertido em graus.
A fórmula de conversão é: G = R * 180/pi, sendo G o ângulo em graus e
R em radianos e pi = 3.14.
"""

angulo_radiano = float(input("Digite o ângulo radiano: "))
graus = angulo_radiano * 180/3.14

print(f"Esse ângulo radiano {angulo_radiano} em graus é: {graus:.2f}")

"""
16 - Leia um valor de comprimento em polegadas e apresente-o convertido
em centímetros. A fórmula de conversão é: C = P * 2.54, sendo C o comprimento
em centímetros e P o comprimento em polegadas.
"""

comprimento_polegadas = float(input("Digite o comprimento em polegads: "))
centimetro = comprimento_polegadas * 2.54

print(f"A polegada de número {comprimento_polegadas} é {centimetro} em centímetros.")

"""
17 - Leia um valor de comprimento em centímetros e apresente-o convertido em
polegadas. A fórmula de conversão é: P = c/2.54, sendo C o comprimento em
centímetros e P o comprimento em polegadas.
"""

centimetro = float(input("Digite o valor em centímetros: "))
polegadas = centimetro/2.54

print(f"{centimetro} centímetros em polegadas é {polegadas:.2f}.")

"""
18 - Leia um valor de volume em metros cúbicos m³ e apresente-o convertido
em litros. A fórmula de conversão é: L = 1.000 * M, sendo L o volume em litros
e M o volume em metros cúbicos
"""

volume_cubico = float(input("Digite o valor em m³: "))
litros = 1.000*volume_cubico

print(f"{volume_cubico} metros cúbicos em litros é: {litros:.3f}")


"""
19 - Leia um valor de volume em litros e apresente-o convertido em metros
cúbicos m³. A fórmula de conversão é: M = L/1.000, sendo L o volume em litros
e M o volume em metros cúbicos.
"""

volume_litros = float(input("Digite o valor em litros: "))
metros_cúbicos = volume_litros/1.000

print(f"{volume_litros} litros em metros cúbicos é: {metros_cúbicos:.3f}.")
