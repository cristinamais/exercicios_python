"""
25 - Faça um programa que leia some todos os numeros naturais abaixo de 1000
que são multiplos de 3 ou 5
"""
listaNumero = []

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        listaNumero.append(i)  # Se eu não colocar na lista ele vai pegar o número repetido em 3 e 5.
print(sum(listaNumero))




