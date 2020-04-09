"""
25 - Calcule as raizes da equação de 2º grau.
lembrando que:
x = -b, + ou - raiz de delta / 2a. Onde:
raiz de delta = B² - 4ac.
E ax² + bx + c = 0 representa uma equação de 2º grau.

A variável de zero tem que ser diferente de zero. Caso seja igual, imprima a
mensagem "Não é equação de segundo grau."

Se Delta < 0, não existe real. Imprima não existe raiz.
Se Delta = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única.
Se Delta >= 0, imprima as duas raízes reais
"""
import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

#ax² + bx + c = 0 --> é o que queremos saber.

#valor de delta: B² - 4ac.
delta = (b * b) + (-4 * a * c)

if delta > 0:
    print(f'O valor de delta é {delta}')
    x1 = (- b + (math.sqrt(delta))) / 2 * a
    print(f'Essa é a primeira raiz quadrada, ou x1 {x1}')
    x2 = (- b - (math.sqrt(delta))) / 2 * a
    print(f'Essa é a segunda raiz quadrada, ou x2 {x2}')
elif delta == 0:
    print(f'A raiz de delta é {delta} sendo Raiz única.')
else:
    delta < 0
    print('Não existe raiz')
