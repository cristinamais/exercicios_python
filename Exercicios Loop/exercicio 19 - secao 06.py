"""
19 - Escreva um algorítmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarísmos que
compõem o número.
"""

number = 0
answer = ''
while answer != 'no':
    number = int(input('Type one number between 100 to 999: '))
    if number <= 100 or number >= 999:
        print('Number is not between 100 to 999, type another number please.')
        continue
    u = (number // 1 ) % 10 # units - unidades
    t = (number // 10) % 10 # tens - dezenas
    h = (number // 100) % 10 # hundreds - centenas
    print(f'The number {number} have: {h} hundreds {t} tens {u} units')
    answer = str(input('Would you like to continue? Type yes or no: '))

