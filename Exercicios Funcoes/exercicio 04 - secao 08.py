"""
04 - Faca uma funcao para verificar se um numero e um quadrado perfeito. Um quadrado perfeito e um numero inteiro nao
negativo que pode ser expresso como o quadrado de outro numero inteiro. EX: 1, 4, 9.

"""

numero = int(input('Digite um numero: '))

def quadrado_perfeito():
    if numero > 0:
        return numero * numero
    return f'Nao podemos calcular o quadrado perfeito desse numero: {numero}'

print(quadrado_perfeito())
