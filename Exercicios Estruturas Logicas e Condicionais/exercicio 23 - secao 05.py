"""
23 - Determine se um determinado ano lido é bissexto.
Sendo que um ano é bissexto se for divisível por 400 ou se for divisível
por 4 e não divisível por 100. Por exemplo: 1988. 1992, 1996.
"""

ano = int(input("Digite o ano desejado: "))

if ano % 400 == 0:
    print(f'O ano {ano} é ano bissexto')
elif (ano % 4 == 0) and (ano % 100 != 0):
   print(f'O ano {ano} é bissexto')
else:
    print(f'Este ano {ano} não é bissexto')

