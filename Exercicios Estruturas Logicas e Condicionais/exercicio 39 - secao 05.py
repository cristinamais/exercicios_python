"""
39 - Uma empresa decide dar aumento aos seus funcionários de acordo com uma tabela que considera o salário atual e o tempo de serviço de cada funcionário.
Os funcionários com menor salário terão um aumento proporcionalmente maior do que os funcionários com um salário maior, e conforme o tempo de serviço na
empresa, cada funcionário irá receber um bônus adicional de salário. Faça um programa que leia:
    a) o valor do salário atual do funcionário;
    b) O tempo de serviço desse funcionário na empresa(número de anos de trabalho na empresa).
Use a tabela abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final reajustado, ou uma mensagem caso o funcionário não
tenha direito a nenhum aumento.
-------------------------------------------------------------------------
SALÁRIO ATUAL       REAJUSTE(%)         TEMPO DE SERVIÇO           BÔNUS 
Até 500,00 -----------> 25%  ------------> Abaixo de 1 ano ----> Sem bônus
Até 1000,00-----------> 20%  ------------> De 1 a 3 anos ------> 100,00
Até 1500,00-----------> 15%  ------------> De 4 a 6 anos ------> 200,00
Até 2000,00-----------> 10%  ------------> De 7 a 10 anos -----> 300,00
Acima de 2000,00------> Sem reajuste-----> Mais de 10 anos ----> 500,00
---------------------------------------------------------------------------
"""
salario = float(input("Digite o valor do seu salário: "))
tempo_servico = float(input("Digite o tempo de serviço que você tem na empresa. Se for menor que 1 ano, digite 0.11 para considerar onze meses, por exemplo: "))

if salario <= 500 or tempo_servico < 1:
    reajuste = salario * 25 / 100
    salario_final = reajuste + salario
    print(f'O seu salário é R$ {salario} com 25% de reajuste agora é R$ {salario_final}.')
elif (salario > 500 and salario <= 1000) or (tempo_servico >= 1 and tempo_servico <= 3):
    reajuste = salario * 20 / 100
    salario_final = reajuste + salario + 100
    print(f'O seu salário é R$ {salario} com 20% de reajuste + 100.00 de bonus agora é R${salario_final}')
elif (salario > 1000 and salario <= 1500) or (tempo_servico > 3 and tempo_servico <= 6):
    reajuste = salario * 15 / 100
    salario_final = reajuste + salario + 200
    print(f'O seu salário é R$ {salario} com 15% de reajuste + 200.00 de bonus agora é R${salario_final}')
elif (salario > 1500 and salario <= 2000) or (tempo_servico > 6 and tempo_servico <= 10):
    reajuste = salario * 10 / 100
    salario_final = reajuste + salario + 300
    print(f'O seu salário é R$ {salario} com 10% de reajuste + 300.00 de bonus agora é R${salario_final}')
else:
    salario > 2000 or tempo_servico > 10
    salario_final = salario + 500
    print(f'O seu salário é de R$ {salario} + 500.00 de bônus agora é R$ {salario_final}')
