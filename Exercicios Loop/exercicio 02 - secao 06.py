""" 
3 - Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve usar a estrutura de repetição for, a segunda while.
"""
print('Aqui é na repetição for')

for _ in range(3):
    for num in range(1, 101):
        print(num, end='..')

print('\nAqui é na repetição while')

for _ in range(3):
    numero = 1
    while numero <= 100: # Dessa forma começa a contagem com o zero.
        print(numero, end=' ')
        numero = numero + 1

# Professor aqui no while como que se faz para começar com o numero um a contagem? Poque se colocar desse jeito a contagem começa com o zero.
# Procurei para ver se conseguia encontrar alguma coisa. Mas não consegui.

"""
No seu while, como você declarou a variável 'numero' iniciada em 0 então tudo começa no 0. Se você quiser que comece em 1 basta inicializa-la em 1 por exemplo.
"""