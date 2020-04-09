"""
18 - Faça um programa que mostre ao usuário um menu com 4 opções de operações
matemáticas (as básicas por exemplo). O usuário escolhe umas das opções e o seu
programa então pede dois valores numéricos e realiza a operação, mostrando o re
sultado e saindo.
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo múmero: "))

opcao = 0
while opcao != 6:
    print('''\n( 1 ) Somar \n( 2 ) Subtrair \n( 3 ) Multiplicar \n( 4 ) Dividir \n( 5 ) Colocar números novos \n( 6 ) Sair''')
    opcao = int(input("Escolha uma das opções acima: "))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma entre os números {num1} + {num2} é: {soma}')
    elif opcao == 2:
        sutrair = num1 - num2
        print(f'A subtração entre os números {num1} - {num2} é: {sutrair}')
    elif opcao == 3:
        multiplicar = num1 * num2
        print(f'A multiplicação entre os dois números {num1} x {num2} é: {multiplicar}')
    elif opcao == 4:
        dividir = num1 / num2
        print(f'A divisão entre os números {num1} / {num2} é: {dividir:.2f}')
    elif opcao == 5:
        print('Digite números novos')
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo múmero: "))
    elif opcao == 6:
        print('Sair do programa')
              
    print('>>>>>> Fim do programa <<<<<<')
            
  
