"""
33 - Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, cal
cule e escreva o preço novo, e escreva uma mensagem em função do preço novo ( de acordo
com a sua tabela).

PREÇO ANTIGO       PERC/AUME        PREÇO NOVO                     |MENSAGEM
------------------------------      -----------------------------------------
até $50            | 5%             até $80                        | Barato
entre $50 e $100   | 10%            entre $80 e $120(inclusive)    | Normal     
acima de $100      | 15%            entre $120 e $200(inclusive)   | Caro
                                    acima de $200                  | Muito caro
"""
valorAntigo = float(input("Digite o valor do preço antigo: "))

if valorAntigo <= 50:
    porcentagem = (valorAntigo * 5) / 100
elif valorAntigo > 50 and valorAntigo <= 100:
    porcentagem = (valorAntigo * 10) / 100
elif valorAntigo > 100:
    porcentagem = (valorAntigo * 15) / 100    
valorNovo = porcentagem + valorAntigo

if valorNovo <= 80:
    print('Barato: ')
elif valorNovo > 80 and valorNovo <= 120:
    print('Normal')
elif valorNovo > 120 and valorNovo <= 200:
    print('Caro')
else:
    print('Muito Caro')
