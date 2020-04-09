"""
29 - Faça uma prova de matemática para crianças que estão aprendendo a somar
números inteiros menores do que 100. Escolha números aleatórios entre 1 e 100
e mostre na tela a pergunta: qual é a soma de a + b, onde a e b são números alea
tórios. Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as per
guntas e as respostas corretas, além de quantas vezes o aluno acertou.

Funções:
random.random() - gera um número aleatório entre 0 e 1
                -gerar numero inteiro entre 1 e 10, 100 etc:
                a = random.randint(1, 100)
random.choice([lista_itens])- escolhe quais itens da lista.
"""
import random

corretas = 0
erradas = 0
quant = 0
while (quant < 5):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print(f'Qual é a soma de: {a} + {b} ?')
    resposta = int(input("Digite a sua resposta: "))
    soma = a + b
    #resp = resposta
    if resposta == soma:
        print(f'Você acertou pois {a} + {b} = {soma}\n')
        corretas = corretas + 1
    else:
        print(f'Você errou pois {a} + {b} = {soma}\n')
        erradas = erradas + 1
    quant = quant + 1
print(f'\nVocê acertou: {corretas} respostas e errou {erradas} respostas\n\n')
      