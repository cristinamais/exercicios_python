"""
38 - Faça um programa que calcule o terno pitagórico a, b, c para o qual a + b + c = 1000.
Um terno pitagórico é um conjunto de três números naturais a, b, c, para a qual, a² + b² = c²
    Por exemplo: 3² + 4² = 9 + 16 = 25 = 5²;  5² + 12² = 25 + 144 = 169 = 13²
                7² + 24² = 49 + 576 = 625 = 25² ...
"""

a, b, c = [int(x) for x in input("Digite um terno pitagórico para a b c: ").split()]
for i in list(range(a, b, c)):
    potenciaa = a ** 2
    potenciab = b ** 2
    somaAB = potenciaa + potenciab

print(f'{a}² + {b}² = {potenciaa} + {potenciab} = {somaAB} => {c}²')
