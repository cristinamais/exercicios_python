"""
60 - Escreva uma funcao que retorne a primeira posicao de uma sub-string dentro de uma string. Caso a sub-string nao seja
encontrada, a funcao deve retornar -1.
substring e chamado tambem de slicing
"""

string = str(input('Digite uma palavra: '))

def substring(string):
    sub_string = [(string[0]) if string[0] == 'a' else -1]  # A condicao deve estar entre parenteses.
    return sub_string


print(substring(string))

