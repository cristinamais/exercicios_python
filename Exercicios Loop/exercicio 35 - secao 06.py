"""
35 - Faça um programa que some os números impares contidos em um intervalo definido pelo usuário.
O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa deve
somar todos os números ímpares contidos neste intervalo (começando por um valor maior que o valor final)
deve ser escrito uma mensagem de erro na tela, "Intervalo de valores inválido" e o programa termina.
Exemplo de tela de saída:
 Digite o valor inicial e valor final: 5 10
 Soma dos ímpares neste intervalo: 21
"""
impar = 0

inicial, final = [int(x) for x in input("Digite o valor inicial e valor final: ").split()]

for i in list(range(inicial, final)):
    if i % 2 != 0:
        impar = impar + i
print(f'A soma dos ímpares neste intervalo é {impar}')
