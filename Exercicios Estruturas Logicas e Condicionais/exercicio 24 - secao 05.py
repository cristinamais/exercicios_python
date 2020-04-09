"""
24 - Uma empresa vende o mesmo produto para quatro diferentes estados.
Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%;
RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor e o estado
destino do produto e o programa retorne o preço final do produto acrescido do
imposto do estado em que ele será vendido. Se o estado digitado não for válido,
mostrar uma mensagem de erro.
"""

mg = 7
sp = 12
rj = 15
ms = 8

estado = str(input("Qual é o estado de destino, MG; SP; RJ or MS? "))
produto = float(input("Digite o valor do produto: "))

if estado.lower() == 'mg':
    produto1 = (produto * 7) / 100
    produto2 = produto + produto1
    print(f'Para o estado de MG esse produto tem {mg}% de imposto, sendo assim o valor a ser pago é de: {produto2}')
elif estado.lower() == 'sp':
    produto1 = (produto * 12) / 100
    produto2 = produto + produto1
    print(f'Para o estado de SP esse produto tem {sp}% de imposto, sendo assim o valor a ser pago é de: {produto2}')
elif estado.lower() == 'rj':
    produto1 = (produto * 15) / 100
    produto2 = produto + produto1
    print(f'Para o estado do RJ esse produto tem {rj}% de imposto, sendo assim o valor a ser pago é de: {produto2}')
elif estado.lower() == 'ms':
    produto1 = (produto * 8) / 100
    produto2 = produto + produto1
    print(f'Para o estado do MS esse produto tem {ms}% de imposto, sendo assim o valor a ser pago é de: {produto2}')
else:
    print(f"Erro, estado {estado} não identificado.")
    
#print(dir(estado))
