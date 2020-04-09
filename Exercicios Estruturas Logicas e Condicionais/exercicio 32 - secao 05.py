"""
32 - Escreva um programa que leia o código do produto escolhido do cardápio de
uma lanchonete e a quantidade. O programa deve calcular o valor a ser pago por
aquele lanche. Considere que a cada execução somente será calculado um pedido.
O cardápio da lanchonete segue o padrão abaixo:

   ESPECIFICAÇÃO     |  CÓDIGO  |  PREÇO
   ----------------------------------------
   Cachorro-Quente   |   100    | 1.20
   Bauru Simples     |   101    | 1.30
   Bauru com ovo     |   102    | 1.50
   Hamburguer        |   103    | 1.20
   Cheeseburguer     |   104    | 1.70
   Suco              |   105    | 2.20
   Refrigerante      |   106    | 1.00
   
"""
codigo = int(input("Digite o código do cardápio: "))
quantidade = int(input("Digite a quantidade desejada: "))

if codigo == 100:
    calculo = quantidade * 1.20
    print(f'Você pediu {quantidade} Cachorro-Quente(s), valor a pagar {calculo}')
elif codigo == 101:
    calculo = quantidade * 1.30
    print(f'Você pediu {quantidade} Bauru(s) Simples, valor a pagar {calculo}')
elif codigo == 102:
    calculo = quantidade * 1.50
    print(f'Você pediu {quantidade} Bauru(s) com Ovo, valor a pagar {calculo}')
elif codigo == 103:
    calculo = quantidade * 1.20
    print(f'Você pediu {quantidade} Hamburguer(s), valor a pagar {calculo}')
elif codigo == 104:
    calculo = quantidade * 1.70
    print(f'Você pediu {quantidade} Cheeseburguer(s), valor a ser pago {calculo}')
elif codigo == 105:
    calculo = quantidade * 2.20
    print(f'Você pediu {quantidade} Suco(s), valor a ser pago {calculo}')
elif codigo == 106:
    calculo = quantidade * 1.00
    print(f'Você pediu {quantidade} Refrigerante(s), valor a ser pago {calculo}')
else:
    print('Código não cadastrado, por favor tente novamente. Obrigada!')