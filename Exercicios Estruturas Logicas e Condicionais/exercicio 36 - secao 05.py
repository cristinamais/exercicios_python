"""
36 - Escreva um programa que, dado o valor da venda, imprima a comissão que
deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela
abaixo:
VENDA MENSAL                                             |    COMISSÃO
-----------------------------------------------------------------------------------
Maior ou igual a R$100.000,00                            |R$700,00 + 16% das vendas 
Menor que R$100.000,00 e maior ou igual a R$80.000,00    |R$650,00 + 14% das vendas
Menor que R$80.000,00 e maior ou igual  a R$60.000,00    |R$600,00 + 14% das vendas
Menor que R$60.000,00 e maior ou igual a R$40.000,00     |R$550,00 + 14% das vendas
Menor que R$40.000,00 e maior ou igual a R$20.000,00     |R$500,00 + 14% das vendas
Menor que 20.000,00                                      |R$400,00 + 14% das vendas
""" 

valorVenda = float(input("Digite o valor da venda colocando ponto somente para distinguir os centavos.: "))

if valorVenda >= 100000.00:
    comissao = 700 + (valorVenda * 16 / 100)
    print(f'A venda foi {valorVenda:,.2f} + 16% de comissão o seu salário é {comissao:,.2f}')
elif valorVenda >= 80000 and valorVenda < 100000:
    comissao = 650 + (valorVenda * 14 / 100)
    print(f'A venda foi {valorVenda:,.2f} + 14% de comissão o seu salário é {comissao:.2f}')
elif valorVenda < 80000 and valorVenda >= 60000:
    comissao = 600 + (valorVenda * 14 / 100)
    print(f'A venda foi {valorVenda:,.2f} + 14% de comissão o seu salário é {comissao:.2f}')
elif valorVenda < 60000 and valorVenda >= 40000:
    comissao = 550 + (valorVenda * 14 / 100)
    print(f'A venda foi {valorVenda:,.2f} + 14% de comissão o seu salário é {comissao:.2f}')
elif valorVenda < 40000 and valorVenda >= 20000:
    comissao = 500 + (valorVenda * 14 / 100)
    print(f'A venda foi {valorVenda:,.2f} + 14% de comissão o seu salário é {comissao:.2f}')
else:
    valorVenda < 20000
    comissao = 400 + (valorVenda * 14 / 100)
    print(f'A venda foi {valorVenda:,.2f} + 14% de comissão o seu salário é {comissao:.2f}')