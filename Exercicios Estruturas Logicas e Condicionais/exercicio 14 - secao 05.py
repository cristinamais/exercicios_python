"""
14 - A nota final de um estudante é calculada a partir de três notas atribuídas
entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a
uma avaliação semestral e a um exame final. A média das três notas mencionadas
anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação
Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o
aluno está reprovado(média entre 0 e 2,9), de recuperação(entre 3 e 4,9) ou se
foi aprovado. Faça todas as verificações necessárias.
"""
#trab_laboratorio = 2
#ava_semestral = 3 
#exam_final = 5

trab_laboratorio = float(input("Qual foi a sua nota no Trabalho de Laboratório? "))
ava_semestral = float(input("Qual foi a sua nota na Avaliação Semestral? "))
exam_final = float(input("Qual foi a sua nota no Exame Final? "))

nota_final = ((trab_laboratorio * 2) + (ava_semestral * 3) + (exam_final * 5)) / 10

if nota_final >= 0 and nota_final <= 2.9:
    print(f'As suas notas foram: {trab_laboratorio}, {ava_semestral} e {exam_final}, tendo como média final {nota_final:.2f},portanto você foi reprovado')
elif nota_final > 2.9 and nota_final <= 4.9:
    print(f'As suas notas foram: {trab_laboratorio}, {ava_semestral} e {exam_final}, tendo como média final {nota_final:.2f},portanto você está de recuperação')
else:
    nota_final > 4.9
    print(f'As suas notas foram: {trab_laboratorio}, {ava_semestral} e {exam_final}, tendo como média final {nota_final:.2f},portanto você foi aprovado')


"""
Exemplo com média ponderada
A melhor forma de entender é mostrar um exemplo de como funciona.

Um professor resolveu aplicar um peso em todas as provas de uma disciplina durante o ano letivo. Foram realizadas 4 provas durante o período letivo e os pesos em cada prova foram assim distribuídos:

Prova 1: peso 2
Prova 2: peso 2
Prova 3: peso 3
Prova 4: peso 3

João tirou na prova 1, nota 5, na prova 2, nota 7, na prova 3, nota 6 e na prova 4 deu uma relaxada e tirou nota 3. Ele foi aprovado?

Dessa forma, basta multiplicar cada nota tirada nas provas por João e multiplicar pelo peso definido pelo professor em cada prova. Somar tudo e dividir pela soma total dos pesos. Veja!

média ponderada
Onde:

p1: prova 1

p2: prova 2

p3: prova 3

p4: prova 4

Média final de João:

média ponderada
média ponderada
Considerando que o colégio adota a média final como 5 para ser aprovado, nesse caso o aluno João foi aprovado com 5,1 de média final.
"""