"""
22 - Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequencia
arbitrária de notas (válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente
média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa,
o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação.
"""
soma = 0
cont = 0
mediaAritimetica = 0
nota = 10

while nota >= 10 and nota <= 20:
    nota = float(input('Digite a nota: '))
    if nota < 10 or nota > 20:
        break
    soma = soma + nota
    cont += 1

mediaAritimetica = soma / cont
print(mediaAritimetica)
