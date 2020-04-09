"""
35 - Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está
entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em
anos bissextos, e 28 dias em anos não bissextos.
"""
dia = int(input("Digite o dia : "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if mes < 1 or mes > 12:
    print(f'Data {dia}/{mes}/{ano} inválida')
elif dia <= 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11 and ano > 0):
    print(f'A data {dia}/{mes}/{ano} é válida')
elif (mes == 2 and dia <= 28):
    print(f'A data {dia}/{mes}/{ano} é válida')
elif mes  == 2 and dia > 28 and dia <= 29 and (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'A data {dia}/{mes}/{ano} é data válida')
elif dia >= 31 and (mes == 1 and mes == 3 and mes == 5 and mes == 7 and mes == 8 and mes == 10 and mes == 12):
    print(f'A data {dia}/{mes}/{ano} é válida')
else:
    print(f'A data {dia}/{mes}/{ano} inválida')
