"""
16 - Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro. Se o código for
diferente de zero, finalize o programa; se for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na ordem
inversa. Caso, o código for diferente de 1 e 2 escreva uma mensagem informando que o código é inválido.
"""
print('Será perguntado cinco vezes.')
vet = []
for x in range(5):
    vetor = float(input('Digite o número: '))
    vet.append(vetor)

print('Escolha a opção desejada:')
cod = int(input('Código 0 - Finalizar o programa\nCódigo 1 - Mostra o vetor na ordem direta\nCódigo 2 - Mostre o vetor na ordem inversa\n'))
while cod != 0:
    if cod == 0:
        break
    elif cod == 1:
        print(f'Vetor na ordem direta: {vet}')
        break
    elif cod == 2:
        vet.reverse()
        print('Vetor na ordem inversa:', vet)
        break
    elif cod != 0 or cod != 1 or cod != 2:
        print('Código é inválido')
        break
