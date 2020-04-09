"""
35 - Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = (raiz quadrada de a² + b²). Faça um programa que receba os valores de a e b
e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa
operação.

"""

valor_a = float(input("Digite o valor do cateto a: "))
valor_b = float(input("Digite o valor do cateto b: "))

rq_a = valor_a ** 2
rq_b = valor_b ** 2

hipotenusa = (rq_a + rq_b) ** (1/2)

print(f"A raiz quadrada de {valor_a}² + {valor_b}² tem a seguinte hipotenusa: {hipotenusa:.2f}.")

