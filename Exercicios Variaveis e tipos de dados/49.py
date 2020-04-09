"""
49 - Faça um programa que leia o horário (hora, minuto, segundo) de início de
uma experiência biológica. O programa deve resultar com um novo horário
(hora, minuto e segundo) do termino da mesma.
"""

import datetime
d = datetime.date(2018, 8, 28)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)
print(tday.weekday())
"""
>>>2
faltam dois dias para o fim de semana
hoje são quarta-feira
segunda é zero e domingo é 6
"""
print(tday.isoweekday())
"""
>>>3
faltam três dias para o fim de semana contando de hoje
segunda é um e domingo é 7
"""

