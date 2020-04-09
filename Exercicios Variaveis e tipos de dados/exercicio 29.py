"""
29 - Leia quatro notas, calcule a média aritimética e imprima o resultado.
"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

soma = nota1 + nota2 + nota3 + nota4
media = soma // 4

print(f"A soma aritimética das notas {nota1}, {nota2}, {nota3}, {nota4} é: {media}.")
