"""
06 - Faca uma funcao que receba 3 numeros inteiros como parametro, respresentando horas,
minutos e segundos, e os converta em segundos.
"""

def segundos():
    n = str(input('Por favor digite as horas como no modelo 1:23:45: ')).split(':')
    h, m, s = n
    return int(h) * 3600 + int(m) * 60 + int(s)


print('Horas minutos e segundos convertidos em segundos:\n', segundos())

