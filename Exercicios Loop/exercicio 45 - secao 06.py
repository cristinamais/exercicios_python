"""
45 - Faça um lagorítmo que converta uma velocidade expressa em km/h para m/s e vice versa. Você deve criar um menu com duas  opções de conversão
e com uma opção para finalizar o programa. O usuário poderá fazer quantas conversões desejar, sendo que o programa só será finalizado quando a
opção de finalizar for escolhida.
"""
numero = int(input('Digite o valor a ser convertido: '))
print('Escolha a opção desejada:\n(Opção 1 - Converter  km/h para m/s)\n(Opção 2 - Converter m/s para Km/h)\n(Opção 3 - Finalizar)')
opcao = int(input())
while opcao != 3:
    if opcao == 1:
        conversaoKm = numero // 3.6
        print(f'{numero} km/h em m/s é: {conversaoKm}')
    elif opcao == 2:
        conversaoms = numero * 3.6
        print(f'{numero} m/s em km/h é: {conversaoms}')
    elif opcao == 3:
        break
    numero = int(input('Digite o valor a ser convertido: '))
    print('Escolha a opção desejada:\n(Opção 1 - Converter  km/h para m/s)\n(Opção 2 - Converter m/s para Km/h)\n(Opção 3 - Finalizar)')
    opcao = int(input())

