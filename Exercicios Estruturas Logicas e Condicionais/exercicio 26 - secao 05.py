"""
26 - Leia a distância em KM e a quantidade de litros de gasolina consumidos por
um carro em um percurso, calcule o consumo em km/l e escreva uma mensagem de
acordo com a tabela abaixo:
    ----------------------------------------
      CONSUMO     | (Km/l) |    MENSAGEM     
    ----------------------------------------
     menor que    |   8    | Venda o carro!
    ----------------------------------------
     entre        | 8 e 11 | Econômico!
    ----------------------------------------
    maior que     |   12   | Super Econômico!
    ------------------------------------------
"""

km = float(input("Digite a distancia percorrida: "))
litros = float(input("Digite a quantidade de litros consumido: "))

consumo = km / litros

if consumo < 8:
    print(f'Venda o carro! O consumo foi de {consumo:.2f} Km/h')
elif consumo >= 8 and consumo <= 11:
    print(f'Econômico! O consumo foi de {consumo:.2f} Km/h')
elif consumo > 12:
    print(f'Super Econômico! O consumo foi de {consumo:.2f} Km/h')
else:
    print(f'Cuidado o seu carro não está sendo econômico, consumo foi de {consumo:.2f} Km/h')
