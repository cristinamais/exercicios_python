"""
8 - Faça um programa que leia 2 notas de um aluno, verifique se as notas
são válidas e exiba na tela a média destas notas. Uma nota válida deve ser,
obrigatoriamente, um valor entre 0.00 e 10.00, onde caso a nota não possua um
valor válido, este fato deve ser informado ao usuário e o programa termina.
"""
sair = 0
print('\nAs perguntas serão feitas 5 vezes.\n')

while (sair < 5):
    
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2



    if nota1 <= 0.00 or nota1 >= 10.00:
        print('A primeira nota é inválida')

    elif nota2 <= 0.00 or nota2 >= 10.00:
        print('A segunda nota é inválida')

    elif media < 7.00:
        print(f'Voê não foi aprovado a sua média foi: {media}')

    else:
        print(f'A sua média é {media}')

    sair = sair + 1# Sem esse código, a condição de parada não será atingida,
    #gerando o que é chamado de loop infinito.
    
