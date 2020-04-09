"""
14 - Faca uma funcao que receba a distancia em KM e a quantidade de litros de gasolina consumidos por um carro em um
percurso, calcule o consumo em KM / l e escreva uma mensagem de acordo com a tabela abaixo:
__________________________________
CONSUMO     (KM /l)     MENSAGEM
----------------------------------
menor que     8         Venda o carro
entre         8 e 12    Economico
maior que       14      Super Economico

"""
km = float(input('Digite a distancia percorrida em KM: '))
l = float(input('Digite a quantidade de litros consumidos: '))


def consumo(*args):
    if km / l < 8:
        return 'Venda o carro'
    elif (km / l > 8) and (km / l <= 12):
        return 'Economico'
    return 'Super Economico'


print(consumo())
