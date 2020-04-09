"""
61 - Escreva uma funcao que retorne verdadeiro, caso uma string seja anagrama da outra, e falso, caso contrario
Counter vai retornar um dicionario struturado que contem caracters do input e as chaves das frequencias que correspondem
aos v alores
"""
from collections import Counter

stringA = str(input('Digite uma palavra: '))
stringB = str(input('Digite uma palavra: '))


def strings_anagramas(stringA, stringB):
    anagram = Counter(stringA) == Counter(stringB)
    return anagram


print(strings_anagramas(stringA, stringB))
