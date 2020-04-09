"""
47 - Leia um número inteiro de 4 dígitos (de 1.000 a 9.999) e imprima 1 dígito
por linha.
"""

inteiro = int(input("Digite um número inteiro de 1.000 a 9.999: "))

digito_0 = str(inteiro)[0]
digito_1 = str(inteiro)[1]
digito_2 = str(inteiro)[2]
digito_3 = str(inteiro)[3]
print(f"Este é o número que você digitou: {inteiro}")
print("E aqui é ele separado:")
print(digito_0)
print(digito_1)
print(digito_2)
print(digito_3)

# ou pode fazer assim:

digito = (inteiro // 1000 % 10), (inteiro // 100 % 10), (inteiro // 10 % 10), (inteiro // 1 % 10)  # milhar, centena, dezena e unidade, respectivamente.
print("\n Aqui o numero vai ser separado em uma mesma linha, começando do milhar e terminado com a unidade:")
print(digito)

# Recebendo o número
numero = input('Informe um número com 4 dígitos: ')
 
# Poderíamos checar se tem realmente 4 dígitos... len(numero)
 
# Imprimindo 1 número por linha
for n in numero:
    print(n)