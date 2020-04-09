"""
34 - Faça um programa que calcule o menor número possível por cada um dos números de 1 a 20
Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto
"""
# gcd() retorna o maior divisor comum dos inteiros a e b.
# lcm vai retornar o menor múltiplo comum entre a e b.

from math import gcd
a = list(range(1, 20))
lcm = a[0]
for i in a[1:]:
  lcm = lcm*i // gcd(lcm, i)
print(f'o menor número possível por cada um dos números de 1 a 20 é {lcm}')
