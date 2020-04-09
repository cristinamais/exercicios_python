"""
9 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido,
caso contrário imprima: Empréstimo concedido.
"""

salário = float(input("Qual o seu salário? "))
empréstimo = float(input("Digite o valor do empréstimo: "))

prestação = (salário * 20) / 100

if empréstimo > prestação:
    print(f'Com o salário de: {salário}, empréstimo não concedido, porque está acima de 20% do salário')
else:
    print(f'Com o salário de: {salário} você pode pegar: {empréstimo} como empréstimo.')
