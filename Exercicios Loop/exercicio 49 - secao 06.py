"""
49 - O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salário. Carlos gosta de fazer
aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela, pois está rendendo 2% ao mês. João aplicará seu salário
integralmente no fundo de renda fixa, que está rendendo 5% ao mês. Construa um programa que deverá calcular e mostrar a quantidade de meses
necessários para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores para as taxas.
"""
salarioCarlos = int(input('Digite o valor do salário de Carlos: '))
salarioJoao = salarioCarlos // 3
print(f'Salário de João: {salarioJoao}')
renda1 = 0.02
renda2 = 0.05
cont = 0
while salarioJoao <= salarioCarlos:
      salarioCarlos = salarioCarlos + (salarioCarlos * renda1)
      salarioJoao = salarioJoao + (salarioJoao * renda2)
      cont += 1

print(f'Salário Carlos + Aplicação: {salarioCarlos:.2f}\nSalário João + Aplicação: {salarioJoao:.2f}')
print(f'João levou {cont} meses para igualar ou ultrapassar Carlos.')
