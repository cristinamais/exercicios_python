"""
22 - Crie uma funcao que receba como parametro um valor inteiro e gere como saida n linhas com pontos
de exclamacao, conforme o exemplo abaixo (para n= 5)
!
!!
!!!
!!!!
!!!!!
"""
n = int(input('Digite um numero: '))

def parametro_n(*args):
    for i in range(n + 1):
        print('!' * i)


parametro_n()


"""
O errado ai é que sua função parametro_n já tem um print no final, então não tem porque executá-la dentro de um print
conforme você está fazendo.
"""


