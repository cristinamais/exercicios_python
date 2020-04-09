"""
02 - Faca uma funcao que receba a data atual (dia, mes e ano em inteiro) e exiba-a na tela
no formato textual por extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro de 2000.
"""

from datetime import date
from datetime import datetime
import locale

def data_usando_date():
    data_atual = date.today()  # print(data_atual) --> 2020-03-07
    data_atual_brasil = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'
    return data_atual_brasil


print('Inteiro:', data_usando_date())


def data_usando_datetime():
    locale.setlocale(locale.LC_ALL, 'pt_pt.UTF-8')
    data_hoje = datetime.now()
    time_data_hoje = data_hoje.strftime("%d de %B de %Y")
    return time_data_hoje


print('Textual:', data_usando_datetime())

