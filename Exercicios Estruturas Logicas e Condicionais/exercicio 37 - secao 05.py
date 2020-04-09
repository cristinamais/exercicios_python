"""
37 - As tarifas de certo parque de estacionamento são as seguntes:
1ª e 2 ª hora - R$1,00 cada
3ª e 4ª hora - R$1,40 cada
5ª hora e seguintes - R$2,00 cada
O número de horas a pagar é sempre inteiro e arredondado por excesso. 
Deste modo quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que paga ria se tivesse permanecido 120 minutos. 
Os momentos de chegada ao parque e partida deste são apresentados na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o par 12 50 representará "Dez para uma da tarde". 
Pretende-se criar um programa que que, lidos pelo teclado os momentos de chegada e de partida se dão com intervalo não superior a 24 horas.
Portanto, se uma dada hora de chegada for superior à da partida, isso não é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.

"""

# Recebe valor de saída
hora_entrada, minuto_entrada = [int(x) for x in (input("Digite a hora da entrada, com espaço entre a hora e o minuto hh  mm: ")).split()] # split divide o valor da hora
hora_saida, minuto_saida = [int(x) for x in (input("Digite a hora da saída, com espaço entre a hora e o minuto hh  mm: ")).split()] # split divide o valor da hora

horas = 0
minutos = 0
valor = 0

# Recebe valor minutos 
if minuto_entrada > minuto_saida:
    minutos = abs(minuto_entrada - minuto_saida)
if minuto_entrada < minuto_saida:
    minutos = abs(minuto_saida - minuto_entrada)
 # Recebe valor horas  
if hora_entrada > hora_saida:
    horas = abs(hora_entrada - hora_saida)
if hora_entrada <= hora_saida:
    horas = abs(hora_saida - hora_entrada)
#print(f'O total de horas estacionados foram {horas} hora(s) e {minutos} minuto(s)')


# Recebendo valores

if horas <= 1: # 1ª hora = 1,00
    valor = 1
    print(f'O total de horas estacionados foram {horas} hora(s) e {minutos} minuto(s) e o valor a ser pago é R$ {valor}')

elif horas > 1 and horas <= 2 : # 2ª hora = 2,00 (1 + 1 = 2)
    valor = 2 #+ (horas + minutos))
    print(f'Você ficou {horas} hora(s) e {minutos} minuto(s) o valor a ser pago é R$ {valor}')

elif horas > 2 and horas <= 3: # 3ª hora = 3,40 (2 + 1,40 = 3,40)
    valor = 2 + 1.40
    print(f'Você ficou {horas} horas e {minutos} minutos o valor a ser pago é R$ {valor}')
elif horas > 3 and horas <= 4: # 4ª hora = 4,80 (2 + (1,40 * 2 = 4,80))
    valor = 2 + (1.40 * 2)
    print(f'Você ficou {horas} horas e {minutos} minutos o valor a ser pago é R$ {valor}')
else:
    horas > 4  # 5ª hora em diante  = (2,00 o valor acima de 4 --> vezes a hora )+ (1,40 * 2)
    valor = (2 * horas) + (1.40 * 2)
    print(f'Você ficou {horas} horas e {minutos} minutos o valor a ser pago é R$ {valor}')
