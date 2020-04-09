"""
22 - Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode
ou não se aposentar. As condições para aposentadoria são:
a) Ter feito pelo menos 65 anos;
b) Ou ter trabalhado pelo menos 30 anos;
c) Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""

idade = int(input("Qual a sua idade? "))
tempo_servico = int(input("Qual o tempo de contribuição? "))

if idade >= 65:
    print(f'Com a idade de {idade}, você está liberado(a) para aposentar-se.')
elif tempo_servico >= 30:
    print(f'Com a idade de {idade} e com o tempo de serviço de {tempo_servico} anos você está liberado(a) para aposentar-se.')
elif (idade >= 60 and tempo_servico >= 25):
    print(f'Com a idade de {idade} e com o tempo de serviço de {tempo_servico} anos você está liberado(a) para aposentar-se.')
else:
    print(f'Com a idade de {idade} e tempo de contribuição de {tempo_servico} você não está liberado para trabalhar.')
