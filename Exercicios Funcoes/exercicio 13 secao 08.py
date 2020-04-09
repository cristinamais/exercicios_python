"""
13 - Faca uma funcao que receba dois valores numericos e um simbolo. Este simbolo representara a operaco que deseja
efetura com os numeros. Se o simbolo for + devera ser realizada uma adicao, se for - uma subtracao, se for / uma divisao
e se for * sera efetuada uma multiplicacao
"""

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
s = str(input(('Escolha uma opcao:\n+ para Adicao: \n- para Subtracao: \n/ para Divisao: \n* para multiplicacao: ')))

def valor_numerico(n1, n2, s):
    if s == "+":
        a = n1 + n2
        return f'A adicao dos numeros sao: {a}'
    if s == "-":
        su = n1 - n2
        return f'A subtracao dos numeros sao: {su}'
    if s == "/":
        d = n1 / n2
        return f'A divisao dos numeros sao: {d:.2f}'
    if s == "*":
        m = n1 * n2
        return f'A multiplicacao dos numeros sao: {m}'


print(valor_numerico(n1, n2, s))
