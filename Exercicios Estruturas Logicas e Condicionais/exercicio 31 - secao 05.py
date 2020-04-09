"""
31 - Faça um programa que receba a altura e o peso de uma pessoa. De acordo
com a tabela a seguir, verifique e mostra qual a classificação dessa pessoa.

ALTURA                           PESO
                |  Até 60 | Entre 60 e 90(Inclusive) | Acima de 90
-------------------------------------------------------------------
Menor que 1,20  |    A    |             D            |     G
-------------------------------------------------------------------
De 1,20 a 1,70  |    B    |             E            |     H
-------------------------------------------------------------------
Maior que 1,70  |    C    |             F            |     I
-------------------------------------------------------------------

"""

altura = float(input("Qual a sua altura? "))
peso = float(input("Qual o seu peso? "))

if altura < 1.20 and peso <= 60:
    print(f'Altura {altura} e peso {peso}. Você esta na classificação A')
    
elif (altura >= 1.20 and altura <= 1.70) and peso <= 60 :
   print(f'Altura {altura} e peso {peso}. Você está na classificação B')
   
elif altura > 1.70 and peso <= 60:
    print(f'Altura {altura} e peso {peso}. Você está na classificação C')
    
elif altura < 1.20 and (peso > 60 and peso <= 90):
    print(f'Altura {altura} e peso {peso}. Você está na classificação D')
    
elif (altura >= 1.20 and altura <= 1.70) and (peso > 60 and peso <= 90):
    print(f'Altura {altura} e peso {peso}. Você está na classificação E')
    
elif altura > 1.70 and (peso > 60 and peso <= 90):
    print(f'Altura {altura} e peso {peso}. Você está na classificação F')

elif altura < 1.20 and peso > 90:
    print(f'Altura {altura} e peso {peso}. Você está na classificação G')

elif (altura >= 1.20 and altura <= 1.70) and peso > 90:
    print(f'Altura {altura} e peso {peso}. Você está na classificação H')
else:
    altura > 1.70 and peso > 90
    print(f'Altura {altura} e peso {peso}. Você está na classificação I')

