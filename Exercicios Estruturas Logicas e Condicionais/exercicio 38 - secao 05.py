"""
38 - Leia uma data de nascimento de uma pessoa fornecida através de três números
inteiros: Dia, mês e ano. Teste a validade desta data para saber se esta é uma
data válida.
Teste se o dia fornecido é um dia válido: dia > 0, dia <= 28 para mês de
fevereiro (29 se o mês for bissexto), dia <= 30 em abril, junho, setembro e no
vembro, dia <= 31 nos outros meses. Tese a validade do mês > 0 e mês < 31.
Teste a validade do ano: ano <= ano atual (use uma constante definida com valor
igual a 2008). Imprimir:'data válida' ou 'data inválida' no final da execução
do programa.
"""

dia = int(input("Digite o dia do seu aniversário: "))
mes = int(input("Digite o mês do seu aniversário: "))
ano = int(input("Digite o ano que você nasceu: "))

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
