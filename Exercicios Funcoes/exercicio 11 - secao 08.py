"""
11 - Elabore uma funcao que receba tres notas de um aluno como parametros e uma letra.
Se a letra for A, a funcao devera calcular a media aritmetica das notas do aluno;
se for P, devera calcular a media ponderada, com pesos 5, 3 e 2
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
letra = str(input('Escolha o que voce quer que calcule:\nA - para Media Aritmetica\nP - para Media Ponderada: ')).upper()

def notas(n1, n2, n3, letra):
    if letra == 'A':
        c1 = (n1 + n2 + n3) / 3
        return f'A sua Media Aritmetica e: {c1}'
    c2 = (n1 * 5 + n2 * 3 + n3 * 2) / 10
    return f'A sua Media Ponderada e: {c2}'


print(notas(n1, n2, n3, letra))





