"""
8 - Faça um programa que leia 2 notas de um aluno, verifique se as notas
são válidas e exiba na tela a média destas notas. Uma nota válida deve ser,
obrigatoriamente, um valor entre 0.00 e 10.00, onde caso a nota não possua um
valor válido, este fato deve ser informado ao usuário e o programa termina.
"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 <= 0.00 or nota1 >= 10.00:
    print('A primeira nota é inválida')
        
elif nota2 <= 0.00 or nota2 >= 10.00:
    print('A segunda nota é inválida')

else:
    media = (nota1 + nota2) / 2
    print(f'A sua média é {media}')

"""Uma observação somente:

Pense no seguinte: Uma das notas, ou ambas, foram informadas inválidas.
Faz sentido calcular a média e desta forma utilizar processamento ainda assim?
"""
# O programa já dá o alerta que a nota é inválida.
