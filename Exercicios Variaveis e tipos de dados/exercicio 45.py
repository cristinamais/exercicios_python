"""
45 - Faça um programa para converter uma letra maiúscula em letra minúscula.
Use a tabela ASCII/ para resolver o problema. 
"""

# Receba a letra
letra_minuscula = input("Informe uma letra minúscula: ")

#Converte para decimal da tabela ASCII
ascii = ord(letra_minuscula)

# Transforma em maiúscula usando a tabela ASCII
maiuscula = ascii - 32

# Imprime a letra maiúscula
print(f"A letra minúscula {letra_minuscula} depois de convertida é o número: {maiuscula}")
