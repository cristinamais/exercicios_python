"""
13 - Faça um algorítmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda prova tem peso 1 e a terceira tem peso 2. Ao final,
mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para a aprovação deve ser igual ou superior a 60 pontos.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

#peso1 = (nota1 * 1) + (nota2 * 1) esse eu fiz
peso2 = nota3 * 2

mp = (nota1 + nota2 + peso2) / 3

if mp >= 60:
    print(f'As suas notas foram: {nota1}, {nota2} e {nota3} e a sua média foi: {mp:.2f}, portanto você foi aprovado.')
else:
    print(f'As suas notas foram: {nota1}, {nota2} e {nota3} sua média foi {mp:.2f}, portanto você foi reprovado.')
#print(dir(nota1))

"""
Olá Cristina,

Sua solução está correta.

Só uma observação:

Quando é 60 * 1?

E quanto é 50 * 1?

Concorda que qualquer número multiplicado por 1 é ele mesmo?

Então faz sentido usar o processador para efetuar este cálculo?

Acredito que não, então na linha 12 daria para remover e então alterar a mp para:

mp = (nota1 + nota2 + peso2) / 3

Faça o teste e qualquer coisa poste aqui.

Abraço!
"""