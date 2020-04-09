"""
20 - Dados três valores, A, B, C, verifique se eles podem ser valores dos lados
de um triângulo e, se forem, se é um triângulo escaleno, equilátero ou isósceles
considerando os seguintes conceitos:

a) O primeiro de cada lado de um triângulo é menor do que a soma dos outros dois
lados.
b) Chama-se equilátero o triângulo que tem três lados iguais.
c) Denomina-se isósceles o triângulo que tem o comprimento de dois lados iguais.
d) Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

"""

a = float(input("Informe o valor de A do triângulo: "))
b = float(input("Informe o valor de B do triângulo: "))
c = float(input("Informe o valor de C do triângulo: "))

if a < (b + c) and b < (a + c)  and c < (a + b):
    if (a == b and b == c):
        print('Triângulo Equilátero')
    elif (a == b or b == c or a == c):
        print('Triangulo Isóceles')
    else:
        (a != b and b != c and a != c)
        print('Triângulo Escaleno')
else:
    print('Não formou um triângulo, pois a soma de quaisquer 2 lados tem que ser maior que o outro lado.')
  
