"""
47 - Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
Adicao (opção 1) ..subtracao (opção 2)... multiplicacao (opção 3).. divisao (opção 4).. saida (opção 5)
O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções.
O programa só termina quando for escolhido a opção de saída (opção 5)
"""
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print('Escolha uma das opções para fazer o cálculo: \nAdição (opção 1)\nSubtração (opção 2)\nMultiplicação (opção 3)\nDivisao (opção 4)\nSair (opção 5)')
escolha = int(input())
while escolha != 5:
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma dos números {n1} + {n2} = {soma}')
    elif escolha == 2:
        subtracao = n1 - n2
        print(f'A subtração entre os números {n1} - {n2} = {subtracao}')
    elif escolha == 3:
        multiplicacao = n1 * n2
        print(f'A multiplicação entre os números {n1} x {n2} = {multiplicacao}')
    elif escolha == 4:
        divisao = n1 / n2
        print(f'A divisão entre os números {n1} / {n2} = {divisao:.2f}')
    elif escolha == 5:
        break
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print('Escolha uma das opções para fazer o cálculo: \nAdição (opção 1)\nSubtração (opção 2)\nMultiplicação (opção 3)\nDivisao (opção 4)\nSair (opção 5)')
    escolha = int(input())
