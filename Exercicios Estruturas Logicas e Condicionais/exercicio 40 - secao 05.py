"""
40 - O custo ao consumidor de um carro novo é a soma do custo de fábrica,
da comissão do distribuidor, e dos impostos. A comissão e os impostos são
calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo
de fábrica e escreva o custo ao consumidor.
--------------------------------------------------------------------------
    CUSTO DE FÁBRICA                % DO DISTRIBUIDOR       % DOS IMPOSTOS
    Até 12.000,00 ----------------->         5     -------->     isento
    Entre 12.000,00 e 25.000,00 --->        10     -------->       15
    Acima de 25.000,00 ------------>        15     -------->       20
---------------------------------------------------------------------------
"""
custo_fabrica = float(input("Digite o valor do custo de fábrica: "))

if custo_fabrica <= 12000:
    soma_valor_consumidor = (custo_fabrica * 5 / 100)
    custo_consumidor = custo_fabrica + soma_valor_consumidor
    print(f'O valor de fábrica é {custo_fabrica} e o custo ao consumidor é {custo_consumidor}')
elif custo_fabrica > 12000 and custo_fabrica <= 25000:
    soma_valor_consumidor = (custo_fabrica * 10 / 100) + (custo_fabrica * 15 / 100)
    custo_consumidor = custo_fabrica + soma_valor_consumidor
    print(f'O valor de fábrica é {custo_fabrica} e o custo ao consumidor é {custo_consumidor}')
else:
    custo_fabrica > 25000
    soma_valor_consumidor = (custo_fabrica * 15 / 100) + (custo_fabrica * 20 / 100)
    custo_consumidor = custo_fabrica + soma_valor_consumidor
    print(f'O valor de fábrica é {custo_fabrica} e o custo ao consumidor é {custo_consumidor}')
