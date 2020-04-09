"""
17 - Faca uma funcao que receba dois numeros inteiros positivos por parametros e retorne a soma dos N numeros inteiros
existente entre eles.
"""
print('Observacao o primeiro numero tem que ser menor que o segundo')
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))


def parametros(num1, num2):
    if num1 > 0 and num2 > 0:  # Aqui tem que colocar assim if num1 > 0 and num2 > 0, se colocar if num1 and num2 > 0, nao funciona
        c = sum(range(num1 + 1, num2))
        return f'A soma dos N numeros inteiros existente entre eles sao: {c}'
    return f'Para fazer o calculo todos os numeros deverao ser inteiros positivos'


print(parametros(num1, num2))
