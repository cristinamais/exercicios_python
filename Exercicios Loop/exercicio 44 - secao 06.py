"""
44 - Leia um número positivo do usuário, então calcule e imprima a sequencia Fibonacci até o primeiro número superior ao número lido.
Exemplo: Se o usuário informou o número 30, a sequencia a ser impressa será 0 1 1 2 3 5 8 13 21 34.
"""
n1 = 0
n2 = 1

numero = int(input("Digite um número positivo: "))
if numero <= 0:
   print("Digite um número inteiro positivo")
elif numero == 1:
   print(f'Sequência de Fibonacci {numero}: ')
   print(n1)
else:
   print('Sequência de Fibonacci:', end=' ')
   while n2 <= numero:
       n = n1 + n2
       print(n, end=' ')
       n1 = n2
       n2 = n
