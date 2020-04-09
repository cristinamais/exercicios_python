"""
32 - Faca uma funcao chamada 'simplifica' que recebe como parametro o numerador e o denominador de uma fracao.
Esta funcao deve simplificar a fracao recebida dividindo numerador e o denominador por 12. A funcao deve modificar as
variaveis passadas como parametro.
"""
# OBS: A funcao deve modificar as variaveis passadas como parametro, como assim?

n= int(input('Digite o valor do numerador: '))
d = int(input('Digite o valor do denominador: '))

def simplifica(n, d):
    simp_n = n / 12
    simp_d = d / 12
    return f'{simp_n:.2f}\n{simp_d:.2f}'


print(simplifica(n, d))


