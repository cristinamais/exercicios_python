"""
16 - Usando o switch, escreva um programa que leia um número inteiro entre
1 e 12 e imprima o mês correspondente a este número. Isto é, janeiro se 1,
fevereiro se 2, e assim por diante.
"""

numero_mes = int(input("Digite um número entre 1 e 12: "))

if numero_mes:
    if numero_mes == 1:
        print(f'No calendário {numero_mes} corresponde ao mês de Janeiro')
    elif numero_mes == 2:
        print(f'No calendário {numero_mes} corresponde ao mês de Fevereiro')
    elif numero_mes == 3:
        print(f'No calendário {numero_mes} corresponde ao mês de Março')
    elif numero_mes == 4:
        print(f'No calendário {numero_mes} correspondre ao mês de Abril')
    elif numero_mes == 5:
        print(f'No calendário {numero_mes} corresponde ao mês de Maio')
    elif numero_mes == 6:
        print(f'No calendário {numero_mes} corresponde ao mês de Junho')
    elif numero_mes == 7:
        print(f'No calendário {numero_mes} corresponde ao mês de Julho')
    elif numero_mes == 8:
        print(f'No calendário {numero_mes} corresponde ao mês Agosto')
    elif numero_mes == 9:
        print(f'No calendário {numero_mes} corresponde ao mês de Setembro')
    elif numero_mes == 10:
        print(f'No calendário {numero_mes} corresponde ao mês de Outubro')
    elif numero_mes == 11:
        print(f'No calendário {numero_mes} corresponde ao mês de Novembro')
    elif numero_mes == 12:
        print(f'No calendário {numero_mes} corresponde ao mês de Dezembro')

    else:
        print('Não existe mês com esse número.')
