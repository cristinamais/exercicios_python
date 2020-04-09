"""
43 - Escreva um programa de ajuda para vendedores. A partir de um valor total
lido, mostre:
a) o total a pagar com desconto de 10%;
b) o valor de cada parcela, no parcelamento de 3x sem juros;
c) a comissão do vendedor, no caso de a venda ser a vista (5% sobre o valor com
desconto);
d) a comissão do vendedor, no caso da venda ser parcelada(5% sobre o valor total)
"""

valor_produto = float(input("Digite o valor do produto: "))

produto_desconto_10 = valor_produto - (valor_produto * 10 / 100)
print(produto_desconto_10)

parcelas = valor_produto / 3
print(parcelas)

comissao1 = produto_desconto_10 - (produto_desconto_10 * 5 / 100 )
print(comissao1)

comissao2 = valor_produto - (valor_produto * 5 / 100)
print(comissao2)


"""
Aqui professor eu não estou conseguindo mostrar o valor da comissão,
por exemplo se o produto vale 300 deveria mostrar 13,5 de comissão veja:
#comissao1 = produto_desconto_10 - (produto_desconto_10 * 5 / 100 )

deveria mostrar 13,50 no output, mas mostra 256,50, eu queria mostrar o valor da comissão
e não o valor 256.5 conforme o senhor pode ver abaixo.

e aqui também:
#comissao2 = valor_produto - (valor_produto * 5 / 100)

o que eu posso fazer aqui?
"""

#Aqui vai aparecer o valor da comissão
comissao1 = produto_desconto_10 * 0.05
print(comissao1)

comissao2 = valor_produto * 0.05 
print(comissao2)