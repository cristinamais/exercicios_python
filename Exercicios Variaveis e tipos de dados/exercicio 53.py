"""
53 - Faça um programa para ler as dimensões de um terreno
(comprimento c e largura l), bem como o preco do metro de rela p. Imprima
o custo para cercar este mesmo terreno com tela.
"""

c = float(input("Digite o comprimento do terreno: "))
l = float(input("Digite a largura do terreno: "))
preco_tela = float(input("Qual o valor do metro da tela? "))


custo_total = c * l * preco_tela

print(f"O tamanho da área {c} x {l} você irá pagar: {custo_total}")
