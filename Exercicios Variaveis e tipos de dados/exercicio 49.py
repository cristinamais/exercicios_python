"""
49 - Faça um programa que leia o horário (hora, minuto, segundo) de início de
uma experiência biológica. O programa deve resultar com um novo horário
(hora, minuto e segundo) do termino da mesma.
"""

from datetime import datetime, date
from time import sleep

start = datetime.now()
print(f"Início de uma experiência biológica: {start}")
sleep(5)
start = datetime.now()
end = datetime(start.year, start.month, start.day, start.hour, start.minute, start.second)
print(f"Fim de uma experiência biológica: {end}")

#Então uma forma de resolução seria:

hora = int(input('Informe a hora de início: ')) # 8 por exemplo
 
minuto = int(input('Informe o minuto de início: ')) # 34 por exemplo
 
segundo = int(input('Informe o segundo de início: ')) # 23 por exemplo
 
tempo_em_segundos = int(input('Informe a duração do experimento em segundos: ')) # 7 por exemplo
 
# Aqui precisaria fazer validações, por exemplo se o segundo_final passar de 60 segundos, deve-se ficar com o resto e passar 1 para minuto...
segundo_final = segundo + tempo_em_segundos
 
print(f'O experimento finaliza em {hora}:{minuto}:{segundo_final}')  # 8:34:30