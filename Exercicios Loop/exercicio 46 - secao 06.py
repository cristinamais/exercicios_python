"""
46 - Faça um programa que gere um número aleatório de 1 a 1000. O usuário deve tentar acertar qual número foi gerado,
a cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. O program acaba quando o usuário
acertar o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.
"""
import random

numeroEscolher = int(input('Tente adivinhar qual número será gerado de 1 até 1000: '))

numeroGerado = 0
cont = 0
while numeroEscolher != numeroGerado:
        numeroGerado = random.randint(1, 1000)
        if numeroEscolher < numeroGerado:
            print(f'O chute é menor que o número sorteado. Veja: chute {numeroEscolher}  sorteado {numeroGerado}')
        elif numeroEscolher > numeroGerado:
            print(f'O chute é maior que o número sorteado. Veja: chute {numeroEscolher}  sorteado {numeroGerado}')
        else:
            print(f'Você acertou: {numeroEscolher} = {numeroGerado}')
        numeroEscolher = int(input('Tente acertar qual número será gerado. Digite aqui: '))
        cont += 1
print(f'Você acertou! O número digitado foi {numeroEscolher} e o número gerado foi {numeroGerado}')
print(f'Você teve {cont} tentativa(s).')
