"""
18 - Escreva um algorítmo que leia certa quantidade de números e imprima o maior deles e em quantas vezes o maior número foi lido. A quantidade de números a serem lidos dever ser fornecida pelo usuário.

"""
maior = 0
quant = 0  # quantidade do valor maior que aparecer digitado
total_maior = 0

resposta = 'S'

while resposta == 'S':

    numero = int(input('Digite um número: '))

    if quant == 1:
        maior = numero
    else:
        if numero > maior:
            maior = numero

    
    resposta = str(input('Digite S para continuar ou qualquer letra para terminar: ')).upper()
    
  
print(f'Dos números digitados o maior deles é {maior} e você o digitou {total_maior} vezes.')

print('\n>>>>>>>> Fim! <<<<<<<<<\n')
    