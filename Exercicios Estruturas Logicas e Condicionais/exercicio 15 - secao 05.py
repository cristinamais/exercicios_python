"""
15 - Usando o switch, escreva um programa que leia um inteiro entre 1 e 7
e imprima o dia da semana correspondente a este número. Isto é, domingo se 1,
segunda-feira se 2, e assim por diante.
"""
numero_dias = int(input("Digite um número de 1 a 7 para corresponder o dia da semana: "))

if numero_dias:
    if numero_dias == 1:
        print(f'Este dia {numero_dias} corresponde ao dia de domingo')
    elif numero_dias == 2:
        print(f'Este dia {numero_dias} corresponde ao dia de segunda-feira')
    elif numero_dias == 3:
        print(f'Este dia {numero_dias} corresponde ao dia de terça-feira')
    elif numero_dias == 4:
        print(f'Este dia {numero_dias} corresponde ao dia de quarta-feira')
    elif numero_dias == 5:
        print(f'Este dia {numero_dias} corresponde ao dia de quinta-feira')
    elif numero_dias == 6:
        print(f'Este dia {numero_dias} corresponde ao dia de sexta-feira')
    elif numero_dias == 7:
        print(f'Este dia {numero_dias} corresponde ao dia de sábado')
    else:
        print('Dia não existente!')

"""
Eu pesquisei muito sobre esse tal de swuitch, e foi até na documentação em inglês e não achei nada
Todos falam que o swuitch é o if, elif e o else...Por isso fiz dessa forma.
"""