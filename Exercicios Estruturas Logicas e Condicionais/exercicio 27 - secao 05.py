"""
27 - Escreva um programa que, dada a idade de um nadaddor, classifique-o em
uma das seguintes categorias:
    CATEGORIA    | IDADE
    -----------------------------
    Infantil A   | 5 a 7
    Infantil B   | 8 a 10
    Juvenil A    | 11 a 13
    Juvenil B    | 14 a 17
    Sênior       | maiores de 18 anos
"""

idade = int(input("Digite a idade: "))

if (idade >= 5) and (idade <= 7):
    print(f'A idade de {idade} anos é Categoria Infantil A')
elif (idade >= 8) and (idade <= 10):
    print(f'A idade de {idade} anos é Categoria Infantil B')
elif (idade >= 11) and (idade <= 13):
    print(f'A idade de {idade} anos é Juvenil A')
elif (idade >= 14) and (idade <= 17):
    print(f'A idade de {idade} anos é Juvenil B')
elif idade >= 18:
    print(f'A idade de {idade} anos é Sênior')
else:
    idade < 5
    print('Não autorizado a nadar.')
          
