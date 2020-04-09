"""
21 - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a
operação escolhida. Escreva uma mensagem de erro se a operação for inválida.

Escolha a opção:
1-Soma de dois números
2- Diferença entre dois números (maior pelo menor)
3-Produto entre dois númneros.
Produto é o resultado da operação de multiplicação
4- Divisão entre 2 números ( O denominador não pode ser zero.)
Opção.
"""
import time
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

opcao = 0

while (opcao != 5):
    print('Escolha uma opção: ')    
    opcao = int(input('''( 1 )Soma \n( 2 )Diferença entre dois números (maior pelo menor) \n( 3 )Multiplicação \n( 4 )Divisão \n( 5 )Sair\n'''))
    
    if opcao == 1:
        soma = num1 + num2
        print(f'\nA soma entre os números {num1} + {num2} é: {soma}\n')
    elif opcao == 2:
        diferenca1 = (abs(num1 - num2) or abs(num2 - num1))
        print(f'\nA diferença entre os números {num1} e {num2} é: {diferenca1}')
    elif opcao == 3:
        multiplicacao = num1 * num2
        print(f'\nO produto entre os números {num1} x {num2} é: {multiplicacao:.2f}\n')
    elif opcao == 4:
        divisao = num1 / num2
        print(f'\nA divisão entre os números {num1} / {num2} é: {divisao:.2f}\n')
    elif opcao == 5:
        print('>>>>>>> Saindo do programa <<<<<<<<<')
    else:
        print('\nErro. Aguarde 5 segundos para escolher outra opção.\n')
    time.sleep(10)
