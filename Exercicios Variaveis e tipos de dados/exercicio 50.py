"""
50 - Implemente um programa que calcule o ano de um nascimento de uma pessoa
a partir de sua idade e do ano atual.
"""

idade = int(input("Quantos anos você tem? "))
data_atual = int(input("Em que ano estamos? "))

ano_nascimento = abs((idade - data_atual))

print(f"Você nasceu em {ano_nascimento}")

"""
Utilizamos a função abs para garantir que a quantidade de dias de diferença seja
sempre positiva, independente da ordem em que as datas foram subtraídas.
"""