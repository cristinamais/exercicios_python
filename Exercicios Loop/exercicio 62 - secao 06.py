"""
62 - Se os números de 1 a 5 são escrios em palavras: um, dois, três, quatro, cinco, então há 2 + 4 + 4 + 6 + 5 = 22 letras usadas no total.
Faça um programa que conte quantas letras seriam utilizadas se todos os números de 1 a 1000(mil) fossem escritos em palavras.
OBS: Não conte espaços ou hífens.
"""

from num2words import num2words
total = ''

for i in range(1, 1001):
    num = num2words(i, lang='pt-BR')
    total += num.replace(' ', '')
print(f'Total de letras entre 1 a 1000 é: {len(total)}')
