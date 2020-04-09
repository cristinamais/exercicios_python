antigo = float(input("Digite o valor do preço antigo: "))

porcentagem1 = (antigo * 5) / 100
porcentagem2 = (antigo * 10) / 100
porcentagem3 = (antigo * 15) / 100

# barato 5% = valor menor até 80
if antigo < 50:
    valorNovo1 = antigo + porcentagem1
    barato = valorNovo1 <= 80
    print(f'Barato! O preço que era {antigo}, agora com 5% de aumento está {barato:.2f}.')

# normal 10% = valor entre 80 and 120
elif antigo >= 50 or antigo <= 100:
    valorNovo2 = antigo + porcentagem2
    normal = valorNovo2 >= 80 and valorNovo2 <= 120
    print(f'Normal. O preço que era {antigo}, agora com 10% de aumento está {normal:.2f}.')

 # caro 15% = valor entre 120 and 200   
elif antigo > 100:
    valorNovo3 = antigo + porcentagem3
    caro = valorNovo3 >= 120 and valor_novo3 <= 200
    print(f'Caro! O preço que era {antigo}, agora com 15% de aumento está {caro:.2f}.')

# muito caro 15% = valor acima de 200
elif antigo > 100:
    valorNovo3 = antigo + porcentagem3
    muito_caro = valorNovo3 > 200
    print(f'Muito Caro! O preço que era {antigo}, agora com 15% de aumento está {muito_caro:.2f}.')
