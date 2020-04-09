"""
41 - Faça um algorítmo que calcule o IMC de uma pessoa e mostre sua classificação
de acordo com a tabela abaixo:

          IMC                  | Classificação
     ------------------------------------------------------------     
        < 18,5 ----------------> Abaixo do peso
      18,5 - 24,9 -------------> Saudável
      25,0 - 29,9 -------------> Peso em excesso
      30,0 - 34,9 -------------> Obsidade Grau I
      35,0 - 39,9 -------------> Obesidade Grau II(severa)
        >= 40,0 ---------------> Obesidade Grau III(mórbida)
    -------------------------------------------------------------
"""

imc = float(input("Digite o seu imc: "))

if imc < 18.5:
    print(f'O seu imc é {imc} você está: Abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print(f'O seu imc é {imc} você está: Saudável')
elif imc > 24.9 and imc <= 29.9:
    print(f'O seu imc é {imc} você está com Peso em excesso')
elif imc > 29.9 and imc <= 34.9:
    print(f'O seu imc é {imc} você está com Obsidade Grau I')
elif imc > 34.9 and imc <= 39.9:
    print(f'O seu imc é {imc} você está com Obesidade Grau II (severa)')
else:
    imc >= 40.0
    print(f'O seu imc é {imc} você está com Obsidade Grau III (móbida)')

          
