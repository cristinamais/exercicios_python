"""
52 - Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão
necessárias para atender ao saque com a menor quantidade de notas possíveis. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
"""
saque = int(input('Digite o valor do saque: '))

notas = [100, 50, 20, 10, 5, 2, 1]
contarNotas = [0, 0, 0, 0, 0, 0, 0]

print('Serão utilizadas:')
for a, b in zip(notas, contarNotas):  # zip, é um iterador de tuplas em que o primeiro item em cada iterador passado é emparelhado e, em seguida,
    if saque >= a:                    #  o segundo item em cada iterador passado é emparelhado etc.
        b = saque // a
        saque = saque - b * a
        print(b, ':', a)
