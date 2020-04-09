"""
07 - Faca uma funcao que receba uma temperatura em graus Celsius e retorne-a convertida
em graus Fahrenheit. A formua de conversao e: F = C * (9.0/5.0)+32.0, sendo F a temperatura
em Fahrenheit e C a temperatura em Celsius.
"""

def temperatura():
    c = float(input('Digite a temperatura: '))
    f = c * (9.0/5.0) + 32.0
    return f


print(f'A temperatura em graus Celsius convertida em Fahrenheit e: {temperatura()}')
