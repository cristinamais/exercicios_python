"""
37 - Faça um programa que leia o valor de um produto e imprima o valor com
desconto, tendo em vista que o desconto foi de 12%.
20*12/100
"""
#(20-valor do produto)*(12porcentagem)/(100vai tirar de 100%) = 20*12/100
produto = float(input("Digite o valor do produto: "))

produto_desconto = produto - (produto * 12 / 100)

print(f"O produto com o valor de {produto} teve um desconto de 12%, ou seja, você pagou: {produto_desconto}.")
